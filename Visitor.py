from GrammarVisitor import GrammarVisitor
import GrammarLexer
from antlr4 import InputStream, CommonTokenStream
import GrammarParser
import ast
import copy
from memory import global_memory
from memory import memory

# helper function for stdlib
def get_type(var):
    if type(var) is int:
        return "int"
    elif type(var) is bool:
        return "bool"
    elif type(var) is float:
        return "float"
    elif type(var) is list:
        return "list"

class Visitor(GrammarVisitor):
    def __init__(self, filename, path):
        self.filename = filename
        self.function_file = filename
        self.path = path
        self.was_true = False
        memory.register_file(filename)

    def parse_file(self, path, filename):
        with open(f'{str(path)}/{filename}.twl', 'r') as f:
            text = '\n'.join(f.readlines())
        chars = InputStream(text)
        lexer = GrammarLexer.GrammarLexer(chars)
        tokens = CommonTokenStream(lexer)
        parser = GrammarParser.GrammarParser(tokens)

        parser.buildParseTrees = True
        tree = parser.prog()
        Visitor(filename.split('.')[0], path).visit(tree)

    # From https://stackoverflow.com/questions/33409207/how-to-return-value-from-exec-in-function
    def convertExpr2Expression(self, Expr):
        Expr.lineno = 0
        Expr.col_offset = 0
        result = ast.Expression(Expr.value, lineno=0, col_offset = 0)
        return result

    def exec_with_return(self, code):
        code = code.encode().decode('unicode_escape')
        code_ast = ast.parse(code)

        init_ast = copy.deepcopy(code_ast)
        init_ast.body = code_ast.body[:-1]

        last_ast = copy.deepcopy(code_ast)
        last_ast.body = code_ast.body[-1:]

        exec(compile(init_ast, "<ast>", "exec"), globals())
        if type(last_ast.body[0]) == ast.Expr:
            return eval(compile(self.convertExpr2Expression(last_ast.body[0]), "<ast>", "eval"),globals())
        else:
            exec(compile(last_ast, "<ast>", "exec"),globals())
    
    # -------------Statement-------------- #
    def visitFileStatement(self, ctx):
        file='/'.join(ctx.getText().split('(')[0].split('.')[:-1])
        temp = copy.copy(self.function_file)
        self.function_file = file
        r = self.visitChildren(ctx)
        self.function_file = temp
        return r

    def visitImp(self, ctx):
        file = ctx.getText()[6::].replace('.', '/')
        self.parse_file(self.path, file)

    # -------------Data Types-------------- #
    def visitIntExpr(self, ctx):
        return int(ctx.atom.text)
    
    def visitBoolExpr(self, ctx):
        return ctx.atom.text == 'True'
    
    def visitStrExpr(self, ctx):
        return ctx.getText()[1:-1]
    
    def visitFloatExpr(self, ctx):
        return float(ctx.atom.text)
    
    def visitNullExpr(self, ctx):
        return None

    # -------------Math Operations-------------- #
    def visitOpExpr(self, ctx):
        left = self.visit(ctx.lhs)
        right = self.visit(ctx.rhs)
        if isinstance(left, str) and not isinstance(right, str):
            right = str(right)
        elif isinstance(right, str) and not isinstance(left, str):
            left = str(right)
        op = str(ctx.op.text)
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
        elif op == '%':
            return left % right
        
    def visitNegExpr(self, ctx):
        return -int(ctx.getText())
        
    def visitParensExpr(self, ctx):
        return self.visit(ctx.exp)
    
    def visitVarExpr(self, ctx):
        return self.visit(ctx.atom)
    
    # -------------Variables-------------- #
    def visitSingleVar(self, ctx):
        name = ctx.name.text
        value = self.visit(ctx.exp)
        if ctx.getText().startswith('public'):
            global_memory[name] = value
        else:
            memory.add_value(name, value, self.filename)
        return value
    
    def visitMultiVar(self, ctx):
        names = self.visit(ctx.name)
        vals = self.visit(ctx.vals)
        for i in range(0, len(names)):
            memory.add_value(names[i], vals[i], self.filename)

    def visitListSet(self, ctx):
        name = ctx.name.text
        val = self.visit(ctx.exp)
        index = int(ctx.index.text)
        memory.memory[self.filename][name][index] = val
    
    def visitListVar(self, ctx):
        values = self.visit(ctx.vals)
        memory.add_value(ctx.name.text, values, self.filename)
    
    def visitVarName(self, ctx):
        value = memory.get_value(ctx.name.text, self.function_file)
        return value
    
    def visitInvertVar(self, ctx):
        return not memory.get_value(ctx.name.text, self.filename)
    
    def visitListGet(self, ctx):
        index = int(ctx.index.text)
        return memory.get_value(ctx.name.text, self.filename)[index]
        
    def visitVar_list(self, ctx):
        vars = []
        for i in ctx.getChildren():
            v = self.visit(i)
            if not v == None: vars.append(v)
        return vars
    
    def visitCommaVarname(self, ctx):
        lhs = self.visit(ctx.lhs)
        rhs = self.visit(ctx.rhs)
        return lhs + rhs
    
    def visitAtomVarname(self, ctx):
        return [ctx.atom.text]

    def visitNullVarname(self, ctx):
        return []

    def visitCommaVarlist(self, ctx):
        lhs = self.visit(ctx.lhs)
        rhs = self.visit(ctx.rhs)
        return lhs + rhs
    
    def visitAtomVarlist(self, ctx):
        return [self.visit(ctx.atom)]
    
    def visitNullVarlist(self, ctx):
        return []

    # -------------Conditionals-------------- #
    def visitConditional_statement(self, ctx):
        label = ctx.label.text
        if label == 'if':
            if self.visit(ctx.t):
                return self.visit(ctx.stmts)
            elif not ctx.elseif == None:
                return self.visit(ctx.elseif)
        else:
            while self.visit(ctx.t):
                self.visit(ctx.stmts) 
            return None
        
    def visitElseIf(self, ctx):
        temp = self.visit(ctx.lhs)
        if self.was_true:
            self.was_true = False
            return temp
        return self.visit(ctx.rhs)
    
    def visitAtomElif(self, ctx):
        if self.visit(ctx.t):
            self.was_true = True
            return self.visit(ctx.stmts)
    
    def visitElse(self, ctx):
        return self.visit(ctx.stmts)

    def visitParenTruth(self, ctx):
        return self.visit(ctx.t)
    
    def visitLogicTruth(self, ctx):
        left = self.visit(ctx.lhs)
        if ctx.logic == '||':
            if left: return True
            return self.visit(ctx.rhs)
        if ctx.logic == '&&':
            if not left: return False
            return self.visit(ctx.rhs)

    def visitDualTruth(self, ctx):
        left = self.visit(ctx.lhs)
        right = self.visit(ctx.rhs)
        opr = ctx.operand.text
        if opr == '==': return left == right
        elif opr == '!=': return left != right
        elif opr == '>': return left > right
        elif opr == '<': return left < right
        elif opr == '>=': return left >= right
        elif opr == '<=': return left <= right

    def visitAtomTruth(self, ctx):
        return self.visit(ctx.atom) == True
    
    def visitFor_loop(self, ctx):
        list = self.visit(ctx.array)
        for i in range(0, len(list)-1):
            memory.add_value(ctx.value.text, list[i], self.filename)
            self.visit(ctx.stmts)
        memory.add_value(ctx.value.text, list[-1], self.filename)
        return self.visit(ctx.stmts)

    # -------------Functions-------------- #
    def visitFunction_call(self, ctx):
        args = self.visit(ctx.args)
        if ctx.name.text == '__python':
            return self.exec_with_return(args[0])
        elif ctx.name.text == '__filename':
            return self.function_file
        elif ctx.name.text == 'free':
            memory.remove_value(args[0], self.filename)
            return None
        else:
            if memory.value_in(ctx.name.text, self.function_file):
                memory.add_temp_memory(ctx.name.text, args, self.function_file)
                temp = self.visit(memory.get_value(ctx.name.text, self.function_file)['stmts'])
                memory.close_temp_memory()
                return temp
            else:
                raise Exception("Function not found")

    def visitFunction_def(self, ctx):
        name = ctx.name.text
        args = self.visit(ctx.args)
        stmts = ctx.stmts
        public = ctx.getText().startswith('public')
        if public:
            global_memory[name] = {'args': args, 'stmts': stmts}
        else:
            memory.add_value(name, {'args': args, 'stmts': stmts}, self.filename)
        return None
    
    def visitSemiBrackets(self, ctx):
        self.visit(ctx.lhs)
        return self.visit(ctx.rhs)
    
    def visitAtomBrackets(self, ctx):
        return self.visit(ctx.atom)
    
    def visitAtomBracketStatement(self, ctx):
        return self.visit(ctx.atom)
