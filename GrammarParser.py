# Generated from Grammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,196,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,5,
        0,29,8,0,10,0,12,0,32,9,0,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,3,2,
        42,8,2,1,3,1,3,3,3,46,8,3,1,3,1,3,1,3,1,3,1,3,3,3,53,8,3,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,61,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,71,
        8,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,79,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,3,4,88,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,105,8,6,1,6,1,6,1,6,5,6,110,8,6,10,6,12,6,113,9,6,1,
        7,1,7,3,7,117,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,3,8,131,8,8,1,8,1,8,1,8,5,8,136,8,8,10,8,12,8,139,9,8,1,9,1,9,
        1,9,3,9,144,8,9,1,9,1,9,1,9,5,9,149,8,9,10,9,12,9,152,9,9,1,10,1,
        10,1,10,1,10,1,10,1,10,5,10,160,8,10,10,10,12,10,163,9,10,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,3,11,183,8,11,1,11,1,11,1,11,1,11,1,11,1,11,5,
        11,191,8,11,10,11,12,11,194,9,11,1,11,0,5,12,16,18,20,22,12,0,2,
        4,6,8,10,12,14,16,18,20,22,0,5,1,0,6,7,1,0,12,13,1,0,10,11,1,0,31,
        32,2,0,29,30,33,33,216,0,30,1,0,0,0,2,37,1,0,0,0,4,41,1,0,0,0,6,
        78,1,0,0,0,8,87,1,0,0,0,10,89,1,0,0,0,12,104,1,0,0,0,14,116,1,0,
        0,0,16,130,1,0,0,0,18,143,1,0,0,0,20,153,1,0,0,0,22,182,1,0,0,0,
        24,25,3,2,1,0,25,26,5,18,0,0,26,29,1,0,0,0,27,29,3,4,2,0,28,24,1,
        0,0,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,
        1,1,0,0,0,32,30,1,0,0,0,33,38,3,22,11,0,34,38,3,6,3,0,35,38,3,8,
        4,0,36,38,3,10,5,0,37,33,1,0,0,0,37,34,1,0,0,0,37,35,1,0,0,0,37,
        36,1,0,0,0,38,3,1,0,0,0,39,42,3,10,5,0,40,42,3,14,7,0,41,39,1,0,
        0,0,41,40,1,0,0,0,42,5,1,0,0,0,43,46,5,1,0,0,44,46,1,0,0,0,45,43,
        1,0,0,0,45,44,1,0,0,0,46,47,1,0,0,0,47,48,5,28,0,0,48,49,5,2,0,0,
        49,79,3,2,1,0,50,53,5,1,0,0,51,53,1,0,0,0,52,50,1,0,0,0,52,51,1,
        0,0,0,53,54,1,0,0,0,54,55,3,16,8,0,55,56,5,2,0,0,56,57,3,16,8,0,
        57,79,1,0,0,0,58,61,5,1,0,0,59,61,1,0,0,0,60,58,1,0,0,0,60,59,1,
        0,0,0,61,62,1,0,0,0,62,63,5,28,0,0,63,64,5,2,0,0,64,65,5,3,0,0,65,
        66,3,18,9,0,66,67,5,4,0,0,67,79,1,0,0,0,68,71,5,1,0,0,69,71,1,0,
        0,0,70,68,1,0,0,0,70,69,1,0,0,0,71,72,1,0,0,0,72,73,5,28,0,0,73,
        74,5,3,0,0,74,75,5,20,0,0,75,76,5,4,0,0,76,77,5,2,0,0,77,79,3,2,
        1,0,78,45,1,0,0,0,78,52,1,0,0,0,78,60,1,0,0,0,78,70,1,0,0,0,79,7,
        1,0,0,0,80,81,5,5,0,0,81,88,5,28,0,0,82,88,5,28,0,0,83,84,5,28,0,
        0,84,85,5,3,0,0,85,86,5,20,0,0,86,88,5,4,0,0,87,80,1,0,0,0,87,82,
        1,0,0,0,87,83,1,0,0,0,88,9,1,0,0,0,89,90,7,0,0,0,90,91,5,8,0,0,91,
        92,3,12,6,0,92,93,5,9,0,0,93,94,3,20,10,0,94,11,1,0,0,0,95,96,6,
        6,-1,0,96,97,5,8,0,0,97,98,3,12,6,0,98,99,5,9,0,0,99,105,1,0,0,0,
        100,101,3,2,1,0,101,102,7,1,0,0,102,103,3,2,1,0,103,105,1,0,0,0,
        104,95,1,0,0,0,104,100,1,0,0,0,105,111,1,0,0,0,106,107,10,2,0,0,
        107,108,7,2,0,0,108,110,3,12,6,3,109,106,1,0,0,0,110,113,1,0,0,0,
        111,109,1,0,0,0,111,112,1,0,0,0,112,13,1,0,0,0,113,111,1,0,0,0,114,
        117,5,1,0,0,115,117,1,0,0,0,116,114,1,0,0,0,116,115,1,0,0,0,117,
        118,1,0,0,0,118,119,5,14,0,0,119,120,5,28,0,0,120,121,5,8,0,0,121,
        122,3,16,8,0,122,123,5,9,0,0,123,124,5,15,0,0,124,125,3,20,10,0,
        125,126,5,16,0,0,126,15,1,0,0,0,127,128,6,8,-1,0,128,131,5,28,0,
        0,129,131,1,0,0,0,130,127,1,0,0,0,130,129,1,0,0,0,131,137,1,0,0,
        0,132,133,10,3,0,0,133,134,5,17,0,0,134,136,3,16,8,4,135,132,1,0,
        0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,17,1,0,0,
        0,139,137,1,0,0,0,140,141,6,9,-1,0,141,144,3,2,1,0,142,144,1,0,0,
        0,143,140,1,0,0,0,143,142,1,0,0,0,144,150,1,0,0,0,145,146,10,3,0,
        0,146,147,5,17,0,0,147,149,3,18,9,4,148,145,1,0,0,0,149,152,1,0,
        0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,19,1,0,0,0,152,150,1,0,0,
        0,153,154,6,10,-1,0,154,155,3,2,1,0,155,156,5,18,0,0,156,161,1,0,
        0,0,157,158,10,2,0,0,158,160,3,20,10,3,159,157,1,0,0,0,160,163,1,
        0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,21,1,0,0,0,163,161,1,0,
        0,0,164,165,6,11,-1,0,165,166,5,8,0,0,166,167,3,22,11,0,167,168,
        5,9,0,0,168,183,1,0,0,0,169,170,5,30,0,0,170,183,3,22,11,10,171,
        183,5,20,0,0,172,183,5,22,0,0,173,183,5,23,0,0,174,183,5,25,0,0,
        175,183,5,21,0,0,176,183,3,8,4,0,177,178,5,28,0,0,178,179,5,8,0,
        0,179,180,3,18,9,0,180,181,5,9,0,0,181,183,1,0,0,0,182,164,1,0,0,
        0,182,169,1,0,0,0,182,171,1,0,0,0,182,172,1,0,0,0,182,173,1,0,0,
        0,182,174,1,0,0,0,182,175,1,0,0,0,182,176,1,0,0,0,182,177,1,0,0,
        0,183,192,1,0,0,0,184,185,10,9,0,0,185,186,7,3,0,0,186,191,3,22,
        11,10,187,188,10,8,0,0,188,189,7,4,0,0,189,191,3,22,11,9,190,184,
        1,0,0,0,190,187,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,
        1,0,0,0,193,23,1,0,0,0,194,192,1,0,0,0,21,28,30,37,41,45,52,60,70,
        78,87,104,111,116,130,137,143,150,161,182,190,192
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'public'", "'='", "'['", "']'", "'!'", 
                     "'if'", "'while'", "'('", "')'", "'&&'", "'||'", "'=='", 
                     "'!='", "'def'", "'{'", "'}'", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'null'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SEMI", "NL", "NUM", "FLOAT", 
                      "BOOL", "StringLiteral", "UnterminatedStringLiteral", 
                      "NULL", "BlockComment", "Comment", "VARNAME", "ADD", 
                      "SUB", "MUL", "DIV", "MOD" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_bracket_statement = 2
    RULE_var_declaration = 3
    RULE_var = 4
    RULE_conditional_statement = 5
    RULE_truth = 6
    RULE_function_def = 7
    RULE_varname_list = 8
    RULE_var_list = 9
    RULE_brackets = 10
    RULE_expr = 11

    ruleNames =  [ "prog", "statement", "bracket_statement", "var_declaration", 
                   "var", "conditional_statement", "truth", "function_def", 
                   "varname_list", "var_list", "brackets", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    SEMI=18
    NL=19
    NUM=20
    FLOAT=21
    BOOL=22
    StringLiteral=23
    UnterminatedStringLiteral=24
    NULL=25
    BlockComment=26
    Comment=27
    VARNAME=28
    ADD=29
    SUB=30
    MUL=31
    DIV=32
    MOD=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMI)
            else:
                return self.getToken(GrammarParser.SEMI, i)

        def bracket_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Bracket_statementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Bracket_statementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = GrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 28
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 24
                        self.statement()
                        self.state = 25
                        self.match(GrammarParser.SEMI)
                        pass

                    elif la_ == 2:
                        self.state = 27
                        self.bracket_statement()
                        pass

             
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def var_declaration(self):
            return self.getTypedRuleContext(GrammarParser.Var_declarationContext,0)


        def var(self):
            return self.getTypedRuleContext(GrammarParser.VarContext,0)


        def conditional_statement(self):
            return self.getTypedRuleContext(GrammarParser.Conditional_statementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 33
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 34
                self.var_declaration()
                pass

            elif la_ == 3:
                self.state = 35
                self.var()
                pass

            elif la_ == 4:
                self.state = 36
                self.conditional_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bracket_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional_statement(self):
            return self.getTypedRuleContext(GrammarParser.Conditional_statementContext,0)


        def function_def(self):
            return self.getTypedRuleContext(GrammarParser.Function_defContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_bracket_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracket_statement" ):
                return visitor.visitBracket_statement(self)
            else:
                return visitor.visitChildren(self)




    def bracket_statement(self):

        localctx = GrammarParser.Bracket_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bracket_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7]:
                self.state = 39
                self.conditional_statement()
                pass
            elif token in [1, 14]:
                self.state = 40
                self.function_def()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_var_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ListVarContext(Var_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Var_declarationContext
            super().__init__(parser)
            self.name = None # Token
            self.vals = None # Var_listContext
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)
        def var_list(self):
            return self.getTypedRuleContext(GrammarParser.Var_listContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListVar" ):
                return visitor.visitListVar(self)
            else:
                return visitor.visitChildren(self)


    class SingleVarContext(Var_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Var_declarationContext
            super().__init__(parser)
            self.name = None # Token
            self.exp = None # StatementContext
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)
        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleVar" ):
                return visitor.visitSingleVar(self)
            else:
                return visitor.visitChildren(self)


    class MultiVarContext(Var_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Var_declarationContext
            super().__init__(parser)
            self.name = None # Varname_listContext
            self.vals = None # Varname_listContext
            self.copyFrom(ctx)

        def varname_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Varname_listContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Varname_listContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiVar" ):
                return visitor.visitMultiVar(self)
            else:
                return visitor.visitChildren(self)


    class ListSetContext(Var_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Var_declarationContext
            super().__init__(parser)
            self.name = None # Token
            self.index = None # Token
            self.exp = None # StatementContext
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)
        def NUM(self):
            return self.getToken(GrammarParser.NUM, 0)
        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListSet" ):
                return visitor.visitListSet(self)
            else:
                return visitor.visitChildren(self)



    def var_declaration(self):

        localctx = GrammarParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_declaration)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.SingleVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 43
                    self.match(GrammarParser.T__0)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 47
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 48
                self.match(GrammarParser.T__1)
                self.state = 49
                localctx.exp = self.statement()
                pass

            elif la_ == 2:
                localctx = GrammarParser.MultiVarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 50
                    self.match(GrammarParser.T__0)
                    pass

                elif la_ == 2:
                    pass


                self.state = 54
                localctx.name = self.varname_list(0)
                self.state = 55
                self.match(GrammarParser.T__1)
                self.state = 56
                localctx.vals = self.varname_list(0)
                pass

            elif la_ == 3:
                localctx = GrammarParser.ListVarContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 58
                    self.match(GrammarParser.T__0)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 62
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 63
                self.match(GrammarParser.T__1)
                self.state = 64
                self.match(GrammarParser.T__2)
                self.state = 65
                localctx.vals = self.var_list(0)
                self.state = 66
                self.match(GrammarParser.T__3)
                pass

            elif la_ == 4:
                localctx = GrammarParser.ListSetContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 68
                    self.match(GrammarParser.T__0)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 72
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 73
                self.match(GrammarParser.T__2)
                self.state = 74
                localctx.index = self.match(GrammarParser.NUM)
                self.state = 75
                self.match(GrammarParser.T__3)
                self.state = 76
                self.match(GrammarParser.T__1)
                self.state = 77
                localctx.exp = self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_var

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ListGetContext(VarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.VarContext
            super().__init__(parser)
            self.name = None # Token
            self.index = None # Token
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)
        def NUM(self):
            return self.getToken(GrammarParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListGet" ):
                return visitor.visitListGet(self)
            else:
                return visitor.visitChildren(self)


    class VarNameContext(VarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.VarContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarName" ):
                return visitor.visitVarName(self)
            else:
                return visitor.visitChildren(self)


    class InvertVarContext(VarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.VarContext
            super().__init__(parser)
            self.inv = None # Token
            self.name = None # Token
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvertVar" ):
                return visitor.visitInvertVar(self)
            else:
                return visitor.visitChildren(self)



    def var(self):

        localctx = GrammarParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.InvertVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                localctx.inv = self.match(GrammarParser.T__4)
                self.state = 81
                localctx.name = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 2:
                localctx = GrammarParser.VarNameContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                localctx.name = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 3:
                localctx = GrammarParser.ListGetContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 84
                self.match(GrammarParser.T__2)
                self.state = 85
                localctx.index = self.match(GrammarParser.NUM)
                self.state = 86
                self.match(GrammarParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.label = None # Token
            self.t = None # TruthContext
            self.stmts = None # BracketsContext

        def truth(self):
            return self.getTypedRuleContext(GrammarParser.TruthContext,0)


        def brackets(self):
            return self.getTypedRuleContext(GrammarParser.BracketsContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_conditional_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_statement" ):
                return visitor.visitConditional_statement(self)
            else:
                return visitor.visitChildren(self)




    def conditional_statement(self):

        localctx = GrammarParser.Conditional_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditional_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            localctx.label = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                localctx.label = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 90
            self.match(GrammarParser.T__7)
            self.state = 91
            localctx.t = self.truth(0)
            self.state = 92
            self.match(GrammarParser.T__8)
            self.state = 93
            localctx.stmts = self.brackets(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TruthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_truth

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenTruthContext(TruthContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.TruthContext
            super().__init__(parser)
            self.t = None # TruthContext
            self.copyFrom(ctx)

        def truth(self):
            return self.getTypedRuleContext(GrammarParser.TruthContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenTruth" ):
                return visitor.visitParenTruth(self)
            else:
                return visitor.visitChildren(self)


    class AtomTruthContext(TruthContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.TruthContext
            super().__init__(parser)
            self.lhs = None # StatementContext
            self.operand = None # Token
            self.rhs = None # StatementContext
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomTruth" ):
                return visitor.visitAtomTruth(self)
            else:
                return visitor.visitChildren(self)


    class LogicTruthContext(TruthContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.TruthContext
            super().__init__(parser)
            self.lhs = None # TruthContext
            self.logic = None # Token
            self.rhs = None # TruthContext
            self.copyFrom(ctx)

        def truth(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.TruthContext)
            else:
                return self.getTypedRuleContext(GrammarParser.TruthContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicTruth" ):
                return visitor.visitLogicTruth(self)
            else:
                return visitor.visitChildren(self)



    def truth(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.TruthContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_truth, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.ParenTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 96
                self.match(GrammarParser.T__7)
                self.state = 97
                localctx.t = self.truth(0)
                self.state = 98
                self.match(GrammarParser.T__8)
                pass

            elif la_ == 2:
                localctx = GrammarParser.AtomTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 100
                localctx.lhs = self.statement()
                self.state = 101
                localctx.operand = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    localctx.operand = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 102
                localctx.rhs = self.statement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.LogicTruthContext(self, GrammarParser.TruthContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_truth)
                    self.state = 106
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 107
                    localctx.logic = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        localctx.logic = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 108
                    localctx.rhs = self.truth(3) 
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Function_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.args = None # Varname_listContext
            self.stmts = None # BracketsContext

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)

        def varname_list(self):
            return self.getTypedRuleContext(GrammarParser.Varname_listContext,0)


        def brackets(self):
            return self.getTypedRuleContext(GrammarParser.BracketsContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_function_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = GrammarParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 114
                self.match(GrammarParser.T__0)
                pass
            elif token in [14]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 118
            self.match(GrammarParser.T__13)
            self.state = 119
            localctx.name = self.match(GrammarParser.VARNAME)
            self.state = 120
            self.match(GrammarParser.T__7)
            self.state = 121
            localctx.args = self.varname_list(0)
            self.state = 122
            self.match(GrammarParser.T__8)
            self.state = 123
            self.match(GrammarParser.T__14)
            self.state = 124
            localctx.stmts = self.brackets(0)
            self.state = 125
            self.match(GrammarParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varname_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_varname_list

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NullVarnameContext(Varname_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Varname_listContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullVarname" ):
                return visitor.visitNullVarname(self)
            else:
                return visitor.visitChildren(self)


    class AtomVarnameContext(Varname_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Varname_listContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomVarname" ):
                return visitor.visitAtomVarname(self)
            else:
                return visitor.visitChildren(self)


    class CommaVarnameContext(Varname_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Varname_listContext
            super().__init__(parser)
            self.lhs = None # Varname_listContext
            self.rhs = None # Varname_listContext
            self.copyFrom(ctx)

        def varname_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Varname_listContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Varname_listContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommaVarname" ):
                return visitor.visitCommaVarname(self)
            else:
                return visitor.visitChildren(self)



    def varname_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.Varname_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_varname_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomVarnameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 128
                localctx.atom = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NullVarnameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CommaVarnameContext(self, GrammarParser.Varname_listContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_varname_list)
                    self.state = 132
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 133
                    self.match(GrammarParser.T__16)
                    self.state = 134
                    localctx.rhs = self.varname_list(4) 
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Var_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_var_list

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NullVarlistContext(Var_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Var_listContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullVarlist" ):
                return visitor.visitNullVarlist(self)
            else:
                return visitor.visitChildren(self)


    class AtomVarlistContext(Var_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Var_listContext
            super().__init__(parser)
            self.atom = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomVarlist" ):
                return visitor.visitAtomVarlist(self)
            else:
                return visitor.visitChildren(self)


    class CommaVarlistContext(Var_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Var_listContext
            super().__init__(parser)
            self.lhs = None # Var_listContext
            self.rhs = None # Var_listContext
            self.copyFrom(ctx)

        def var_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Var_listContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Var_listContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommaVarlist" ):
                return visitor.visitCommaVarlist(self)
            else:
                return visitor.visitChildren(self)



    def var_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.Var_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_var_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomVarlistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 141
                localctx.atom = self.statement()
                pass

            elif la_ == 2:
                localctx = GrammarParser.NullVarlistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CommaVarlistContext(self, GrammarParser.Var_listContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_var_list)
                    self.state = 145
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 146
                    self.match(GrammarParser.T__16)
                    self.state = 147
                    localctx.rhs = self.var_list(4) 
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BracketsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_brackets

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SemiBracketsContext(BracketsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.BracketsContext
            super().__init__(parser)
            self.lhs = None # BracketsContext
            self.rhs = None # BracketsContext
            self.copyFrom(ctx)

        def brackets(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.BracketsContext)
            else:
                return self.getTypedRuleContext(GrammarParser.BracketsContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSemiBrackets" ):
                return visitor.visitSemiBrackets(self)
            else:
                return visitor.visitChildren(self)


    class AtomBracketsContext(BracketsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.BracketsContext
            super().__init__(parser)
            self.atom = None # StatementContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(GrammarParser.SEMI, 0)
        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomBrackets" ):
                return visitor.visitAtomBrackets(self)
            else:
                return visitor.visitChildren(self)



    def brackets(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.BracketsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_brackets, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = GrammarParser.AtomBracketsContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 154
            localctx.atom = self.statement()
            self.state = 155
            self.match(GrammarParser.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.SemiBracketsContext(self, GrammarParser.BracketsContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_brackets)
                    self.state = 157
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 158
                    localctx.rhs = self.brackets(3) 
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def StringLiteral(self):
            return self.getToken(GrammarParser.StringLiteral, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrExpr" ):
                return visitor.visitStrExpr(self)
            else:
                return visitor.visitChildren(self)


    class FloatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # VarContext
            self.copyFrom(ctx)

        def var(self):
            return self.getTypedRuleContext(GrammarParser.VarContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(GrammarParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class OpExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.op = None # Token
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def MUL(self):
            return self.getToken(GrammarParser.MUL, 0)
        def DIV(self):
            return self.getToken(GrammarParser.DIV, 0)
        def ADD(self):
            return self.getToken(GrammarParser.ADD, 0)
        def SUB(self):
            return self.getToken(GrammarParser.SUB, 0)
        def MOD(self):
            return self.getToken(GrammarParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpExpr" ):
                return visitor.visitOpExpr(self)
            else:
                return visitor.visitChildren(self)


    class NullExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(GrammarParser.NULL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullExpr" ):
                return visitor.visitNullExpr(self)
            else:
                return visitor.visitChildren(self)


    class Function_callContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.name = None # Token
            self.args = None # Var_listContext
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)
        def var_list(self):
            return self.getTypedRuleContext(GrammarParser.Var_listContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)


    class NegExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.exp = None # ExprContext
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(GrammarParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegExpr" ):
                return visitor.visitNegExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.exp = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class BoolExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(GrammarParser.BOOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 165
                self.match(GrammarParser.T__7)
                self.state = 166
                localctx.exp = self.expr(0)
                self.state = 167
                self.match(GrammarParser.T__8)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 169
                self.match(GrammarParser.SUB)
                self.state = 170
                localctx.exp = self.expr(10)
                pass

            elif la_ == 3:
                localctx = GrammarParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 171
                localctx.atom = self.match(GrammarParser.NUM)
                pass

            elif la_ == 4:
                localctx = GrammarParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 172
                localctx.atom = self.match(GrammarParser.BOOL)
                pass

            elif la_ == 5:
                localctx = GrammarParser.StrExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                localctx.atom = self.match(GrammarParser.StringLiteral)
                pass

            elif la_ == 6:
                localctx = GrammarParser.NullExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 174
                localctx.atom = self.match(GrammarParser.NULL)
                pass

            elif la_ == 7:
                localctx = GrammarParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                localctx.atom = self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 8:
                localctx = GrammarParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 176
                localctx.atom = self.var()
                pass

            elif la_ == 9:
                localctx = GrammarParser.Function_callContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 177
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 178
                self.match(GrammarParser.T__7)
                self.state = 179
                localctx.args = self.var_list(0)
                self.state = 180
                self.match(GrammarParser.T__8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 190
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.OpExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 184
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 185
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==31 or _la==32):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 186
                        localctx.rhs = self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.OpExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 187
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 188
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 10200547328) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 189
                        localctx.rhs = self.expr(9)
                        pass

             
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.truth_sempred
        self._predicates[8] = self.varname_list_sempred
        self._predicates[9] = self.var_list_sempred
        self._predicates[10] = self.brackets_sempred
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def truth_sempred(self, localctx:TruthContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def varname_list_sempred(self, localctx:Varname_listContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def var_list_sempred(self, localctx:Var_listContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

    def brackets_sempred(self, localctx:BracketsContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         




