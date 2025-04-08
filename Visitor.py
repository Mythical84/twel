from GrammarVisitor import GrammarVisitor
import ast
import copy
from memory import global_memory
from memory import memory

class Visitor(GrammarVisitor):
    def __init__(self, filename):
        self.filename = filename
        memory.register_file(filename)

    # From https://stackoverflow.com/questions/33409207/how-to-return-value-from-exec-in-function
    def convertExpr2Expression(self, Expr):
        Expr.lineno = 0
        Expr.col_offset = 0
        result = ast.Expression(Expr.value, lineno=0, col_offset = 0)

        return result

    def exec_with_return(self, code):
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

    # -------------Data Types-------------- #
    def visitIntExpr(self, ctx):
        return int(ctx.atom.text)
    
    def visitBoolExpr(self, ctx):
        return ctx.atom.text == 'true'
    
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
        return -self.visit(ctx.children)
        
    def visitParensExpr(self, ctx):
        return self.visit(ctx.children)
    
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
        value = memory.get_value(ctx.name.text, self.filename)
        if value == None: raise Exception("Variable name not found") 
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
        else:
            while self.visit(ctx.t):
                self.visit(ctx.stmts) 
            return None

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

    def visitAtomTruth(self, ctx):
        left = self.visit(ctx.lhs)
        right = self.visit(ctx.rhs)
        return left == right if ctx.operand == '==' else not left == right

    # -------------Functions-------------- #
    def visitFunction_call(self, ctx):
        args = self.visit(ctx.args)
        if ctx.name.text == '__python':
            return self.exec_with_return(args[0])
        elif ctx.name.text == '__filename':
            return self.filename
        elif ctx.name.text == 'free':
            memory.remove_value(ctx.args[0], self.filename)
            return None
        else:
            if memory.value_in(ctx.name.text, self.filename):
                memory.add_temp_memory(ctx.name.text, args, self.filename)
                temp = self.visit(memory.get_value(ctx.name.text, self.filename)['stmts'])
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