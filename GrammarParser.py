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
        4,1,43,273,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,3,0,35,8,0,1,0,1,0,1,0,5,0,40,8,0,10,
        0,12,0,43,9,0,1,1,1,1,1,1,3,1,48,8,1,1,1,1,1,5,1,52,8,1,10,1,12,
        1,55,9,1,1,1,1,1,1,1,3,1,60,8,1,3,1,62,8,1,1,2,1,2,1,2,3,2,67,8,
        2,1,3,1,3,1,3,5,3,72,8,3,10,3,12,3,75,9,3,1,3,1,3,1,4,1,4,3,4,81,
        8,4,1,4,1,4,1,4,1,4,1,4,3,4,88,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,96,
        8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,106,8,4,1,4,1,4,1,4,1,4,
        1,4,1,4,3,4,114,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,123,8,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,3,7,143,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,155,
        8,8,1,8,1,8,5,8,159,8,8,10,8,12,8,162,9,8,1,9,1,9,1,9,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,179,8,10,1,
        10,1,10,1,10,5,10,184,8,10,10,10,12,10,187,9,10,1,11,1,11,3,11,191,
        8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,
        3,12,205,8,12,1,12,1,12,1,12,5,12,210,8,12,10,12,12,12,213,9,12,
        1,13,1,13,1,13,3,13,218,8,13,1,13,1,13,1,13,5,13,223,8,13,10,13,
        12,13,226,9,13,1,14,1,14,1,14,1,14,1,14,3,14,233,8,14,1,14,1,14,
        5,14,237,8,14,10,14,12,14,240,9,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,
        260,8,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,268,8,15,10,15,12,15,
        271,9,15,1,15,0,6,16,20,24,26,28,30,16,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,0,5,1,0,14,15,1,0,20,25,1,0,18,19,1,0,41,42,2,
        0,39,40,43,43,300,0,41,1,0,0,0,2,61,1,0,0,0,4,66,1,0,0,0,6,68,1,
        0,0,0,8,113,1,0,0,0,10,122,1,0,0,0,12,124,1,0,0,0,14,134,1,0,0,0,
        16,154,1,0,0,0,18,163,1,0,0,0,20,178,1,0,0,0,22,190,1,0,0,0,24,204,
        1,0,0,0,26,217,1,0,0,0,28,232,1,0,0,0,30,259,1,0,0,0,32,35,3,2,1,
        0,33,35,3,6,3,0,34,32,1,0,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,37,
        5,28,0,0,37,40,1,0,0,0,38,40,3,4,2,0,39,34,1,0,0,0,39,38,1,0,0,0,
        40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,1,1,0,0,0,43,41,1,0,
        0,0,44,48,3,30,15,0,45,48,3,8,4,0,46,48,3,10,5,0,47,44,1,0,0,0,47,
        45,1,0,0,0,47,46,1,0,0,0,48,62,1,0,0,0,49,50,5,38,0,0,50,52,5,1,
        0,0,51,49,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,59,
        1,0,0,0,55,53,1,0,0,0,56,60,3,30,15,0,57,60,3,8,4,0,58,60,3,10,5,
        0,59,56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,62,1,0,0,0,61,47,
        1,0,0,0,61,53,1,0,0,0,62,3,1,0,0,0,63,67,3,14,7,0,64,67,3,22,11,
        0,65,67,3,12,6,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,5,
        1,0,0,0,68,73,5,2,0,0,69,70,5,38,0,0,70,72,9,0,0,0,71,69,1,0,0,0,
        72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,1,
        0,0,0,76,77,5,38,0,0,77,7,1,0,0,0,78,81,5,3,0,0,79,81,1,0,0,0,80,
        78,1,0,0,0,80,79,1,0,0,0,81,82,1,0,0,0,82,83,5,38,0,0,83,84,5,4,
        0,0,84,114,3,2,1,0,85,88,5,3,0,0,86,88,1,0,0,0,87,85,1,0,0,0,87,
        86,1,0,0,0,88,89,1,0,0,0,89,90,3,24,12,0,90,91,5,4,0,0,91,92,3,24,
        12,0,92,114,1,0,0,0,93,96,5,3,0,0,94,96,1,0,0,0,95,93,1,0,0,0,95,
        94,1,0,0,0,96,97,1,0,0,0,97,98,5,38,0,0,98,99,5,4,0,0,99,100,5,5,
        0,0,100,101,3,26,13,0,101,102,5,6,0,0,102,114,1,0,0,0,103,106,5,
        3,0,0,104,106,1,0,0,0,105,103,1,0,0,0,105,104,1,0,0,0,106,107,1,
        0,0,0,107,108,5,38,0,0,108,109,5,5,0,0,109,110,5,30,0,0,110,111,
        5,6,0,0,111,112,5,4,0,0,112,114,3,2,1,0,113,80,1,0,0,0,113,87,1,
        0,0,0,113,95,1,0,0,0,113,105,1,0,0,0,114,9,1,0,0,0,115,116,5,7,0,
        0,116,123,5,38,0,0,117,123,5,38,0,0,118,119,5,38,0,0,119,120,5,5,
        0,0,120,121,5,30,0,0,121,123,5,6,0,0,122,115,1,0,0,0,122,117,1,0,
        0,0,122,118,1,0,0,0,123,11,1,0,0,0,124,125,5,8,0,0,125,126,5,9,0,
        0,126,127,5,38,0,0,127,128,5,10,0,0,128,129,3,2,1,0,129,130,5,11,
        0,0,130,131,5,12,0,0,131,132,3,28,14,0,132,133,5,13,0,0,133,13,1,
        0,0,0,134,135,7,0,0,0,135,136,5,9,0,0,136,137,3,20,10,0,137,138,
        5,11,0,0,138,139,5,12,0,0,139,140,3,28,14,0,140,142,5,13,0,0,141,
        143,3,16,8,0,142,141,1,0,0,0,142,143,1,0,0,0,143,15,1,0,0,0,144,
        145,6,8,-1,0,145,146,5,16,0,0,146,147,5,9,0,0,147,148,3,20,10,0,
        148,149,5,11,0,0,149,150,5,12,0,0,150,151,3,28,14,0,151,152,5,13,
        0,0,152,155,1,0,0,0,153,155,3,18,9,0,154,144,1,0,0,0,154,153,1,0,
        0,0,155,160,1,0,0,0,156,157,10,3,0,0,157,159,3,16,8,4,158,156,1,
        0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,17,1,0,
        0,0,162,160,1,0,0,0,163,164,5,17,0,0,164,165,5,12,0,0,165,166,3,
        28,14,0,166,167,5,13,0,0,167,19,1,0,0,0,168,169,6,10,-1,0,169,170,
        5,9,0,0,170,171,3,20,10,0,171,172,5,11,0,0,172,179,1,0,0,0,173,174,
        3,2,1,0,174,175,7,1,0,0,175,176,3,2,1,0,176,179,1,0,0,0,177,179,
        3,2,1,0,178,168,1,0,0,0,178,173,1,0,0,0,178,177,1,0,0,0,179,185,
        1,0,0,0,180,181,10,3,0,0,181,182,7,2,0,0,182,184,3,20,10,4,183,180,
        1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,21,1,
        0,0,0,187,185,1,0,0,0,188,191,5,3,0,0,189,191,1,0,0,0,190,188,1,
        0,0,0,190,189,1,0,0,0,191,192,1,0,0,0,192,193,5,26,0,0,193,194,5,
        38,0,0,194,195,5,9,0,0,195,196,3,24,12,0,196,197,5,11,0,0,197,198,
        5,12,0,0,198,199,3,28,14,0,199,200,5,13,0,0,200,23,1,0,0,0,201,202,
        6,12,-1,0,202,205,5,38,0,0,203,205,1,0,0,0,204,201,1,0,0,0,204,203,
        1,0,0,0,205,211,1,0,0,0,206,207,10,3,0,0,207,208,5,27,0,0,208,210,
        3,24,12,4,209,206,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,
        1,0,0,0,212,25,1,0,0,0,213,211,1,0,0,0,214,215,6,13,-1,0,215,218,
        3,2,1,0,216,218,1,0,0,0,217,214,1,0,0,0,217,216,1,0,0,0,218,224,
        1,0,0,0,219,220,10,3,0,0,220,221,5,27,0,0,221,223,3,26,13,4,222,
        219,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,
        27,1,0,0,0,226,224,1,0,0,0,227,228,6,14,-1,0,228,229,3,2,1,0,229,
        230,5,28,0,0,230,233,1,0,0,0,231,233,3,4,2,0,232,227,1,0,0,0,232,
        231,1,0,0,0,233,238,1,0,0,0,234,235,10,3,0,0,235,237,3,28,14,4,236,
        234,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,
        29,1,0,0,0,240,238,1,0,0,0,241,242,6,15,-1,0,242,243,5,9,0,0,243,
        244,3,30,15,0,244,245,5,11,0,0,245,260,1,0,0,0,246,247,5,40,0,0,
        247,260,3,30,15,10,248,260,5,30,0,0,249,260,5,32,0,0,250,260,5,33,
        0,0,251,260,5,35,0,0,252,260,5,31,0,0,253,260,3,10,5,0,254,255,5,
        38,0,0,255,256,5,9,0,0,256,257,3,26,13,0,257,258,5,11,0,0,258,260,
        1,0,0,0,259,241,1,0,0,0,259,246,1,0,0,0,259,248,1,0,0,0,259,249,
        1,0,0,0,259,250,1,0,0,0,259,251,1,0,0,0,259,252,1,0,0,0,259,253,
        1,0,0,0,259,254,1,0,0,0,260,269,1,0,0,0,261,262,10,9,0,0,262,263,
        7,3,0,0,263,268,3,30,15,10,264,265,10,8,0,0,265,266,7,4,0,0,266,
        268,3,30,15,9,267,261,1,0,0,0,267,264,1,0,0,0,268,271,1,0,0,0,269,
        267,1,0,0,0,269,270,1,0,0,0,270,31,1,0,0,0,271,269,1,0,0,0,30,34,
        39,41,47,53,59,61,66,73,80,87,95,105,113,122,142,154,160,178,185,
        190,204,211,217,224,232,238,259,267,269
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'import'", "'public'", "'='", 
                     "'['", "']'", "'!'", "'for'", "'('", "'in'", "')'", 
                     "'{'", "'}'", "'if'", "'while'", "'elif'", "'else'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'def'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'null'", "<INVALID>", "<INVALID>", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SEMI", "NL", "NUM", "FLOAT", "BOOL", "StringLiteral", 
                      "UnterminatedStringLiteral", "NULL", "BlockComment", 
                      "Comment", "VARNAME", "ADD", "SUB", "MUL", "DIV", 
                      "MOD" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_bracket_statement = 2
    RULE_imp = 3
    RULE_var_declaration = 4
    RULE_var = 5
    RULE_for_loop = 6
    RULE_conditional_statement = 7
    RULE_elif = 8
    RULE_else = 9
    RULE_truth = 10
    RULE_function_def = 11
    RULE_varname_list = 12
    RULE_var_list = 13
    RULE_brackets = 14
    RULE_expr = 15

    ruleNames =  [ "prog", "statement", "bracket_statement", "imp", "var_declaration", 
                   "var", "for_loop", "conditional_statement", "elif", "else", 
                   "truth", "function_def", "varname_list", "var_list", 
                   "brackets", "expr" ]

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
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    SEMI=28
    NL=29
    NUM=30
    FLOAT=31
    BOOL=32
    StringLiteral=33
    UnterminatedStringLiteral=34
    NULL=35
    BlockComment=36
    Comment=37
    VARNAME=38
    ADD=39
    SUB=40
    MUL=41
    DIV=42
    MOD=43

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


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def imp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ImpContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ImpContext,i)


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
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        self.state = 34
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                        if la_ == 1:
                            self.state = 32
                            self.statement()
                            pass

                        elif la_ == 2:
                            self.state = 33
                            self.imp()
                            pass


                        self.state = 36
                        self.match(GrammarParser.SEMI)
                        pass

                    elif la_ == 2:
                        self.state = 38
                        self.bracket_statement()
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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


        def getRuleIndex(self):
            return GrammarParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NormalStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)

        def var_declaration(self):
            return self.getTypedRuleContext(GrammarParser.Var_declarationContext,0)

        def var(self):
            return self.getTypedRuleContext(GrammarParser.VarContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalStatement" ):
                return visitor.visitNormalStatement(self)
            else:
                return visitor.visitChildren(self)


    class FileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)

        def var_declaration(self):
            return self.getTypedRuleContext(GrammarParser.Var_declarationContext,0)

        def var(self):
            return self.getTypedRuleContext(GrammarParser.VarContext,0)

        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.VARNAME)
            else:
                return self.getToken(GrammarParser.VARNAME, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileStatement" ):
                return visitor.visitFileStatement(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.NormalStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 44
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 45
                    self.var_declaration()
                    pass

                elif la_ == 3:
                    self.state = 46
                    self.var()
                    pass


                pass

            elif la_ == 2:
                localctx = GrammarParser.FileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 49
                        self.match(GrammarParser.VARNAME)
                        self.state = 50
                        self.match(GrammarParser.T__0) 
                    self.state = 55
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 59
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 57
                    self.var_declaration()
                    pass

                elif la_ == 3:
                    self.state = 58
                    self.var()
                    pass


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


        def for_loop(self):
            return self.getTypedRuleContext(GrammarParser.For_loopContext,0)


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
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15]:
                self.state = 63
                self.conditional_statement()
                pass
            elif token in [3, 26]:
                self.state = 64
                self.function_def()
                pass
            elif token in [8]:
                self.state = 65
                self.for_loop()
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


    class ImpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.VARNAME)
            else:
                return self.getToken(GrammarParser.VARNAME, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_imp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImp" ):
                return visitor.visitImp(self)
            else:
                return visitor.visitChildren(self)




    def imp(self):

        localctx = GrammarParser.ImpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_imp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(GrammarParser.T__1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 69
                    self.match(GrammarParser.VARNAME)
                    self.state = 70
                    self.matchWildcard() 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 76
            self.match(GrammarParser.VARNAME)
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
        self.enterRule(localctx, 8, self.RULE_var_declaration)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.SingleVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 78
                    self.match(GrammarParser.T__2)
                    pass
                elif token in [38]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 82
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 83
                self.match(GrammarParser.T__3)
                self.state = 84
                localctx.exp = self.statement()
                pass

            elif la_ == 2:
                localctx = GrammarParser.MultiVarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 85
                    self.match(GrammarParser.T__2)
                    pass

                elif la_ == 2:
                    pass


                self.state = 89
                localctx.name = self.varname_list(0)
                self.state = 90
                self.match(GrammarParser.T__3)
                self.state = 91
                localctx.vals = self.varname_list(0)
                pass

            elif la_ == 3:
                localctx = GrammarParser.ListVarContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 93
                    self.match(GrammarParser.T__2)
                    pass
                elif token in [38]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 97
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 98
                self.match(GrammarParser.T__3)
                self.state = 99
                self.match(GrammarParser.T__4)
                self.state = 100
                localctx.vals = self.var_list(0)
                self.state = 101
                self.match(GrammarParser.T__5)
                pass

            elif la_ == 4:
                localctx = GrammarParser.ListSetContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 103
                    self.match(GrammarParser.T__2)
                    pass
                elif token in [38]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 107
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 108
                self.match(GrammarParser.T__4)
                self.state = 109
                localctx.index = self.match(GrammarParser.NUM)
                self.state = 110
                self.match(GrammarParser.T__5)
                self.state = 111
                self.match(GrammarParser.T__3)
                self.state = 112
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
        self.enterRule(localctx, 10, self.RULE_var)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.InvertVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                localctx.inv = self.match(GrammarParser.T__6)
                self.state = 116
                localctx.name = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 2:
                localctx = GrammarParser.VarNameContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                localctx.name = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 3:
                localctx = GrammarParser.ListGetContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 119
                self.match(GrammarParser.T__4)
                self.state = 120
                localctx.index = self.match(GrammarParser.NUM)
                self.state = 121
                self.match(GrammarParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # Token
            self.array = None # StatementContext
            self.stmts = None # BracketsContext

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)

        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def brackets(self):
            return self.getTypedRuleContext(GrammarParser.BracketsContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_for_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = GrammarParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(GrammarParser.T__7)
            self.state = 125
            self.match(GrammarParser.T__8)
            self.state = 126
            localctx.value = self.match(GrammarParser.VARNAME)
            self.state = 127
            self.match(GrammarParser.T__9)
            self.state = 128
            localctx.array = self.statement()
            self.state = 129
            self.match(GrammarParser.T__10)
            self.state = 130
            self.match(GrammarParser.T__11)
            self.state = 131
            localctx.stmts = self.brackets(0)
            self.state = 132
            self.match(GrammarParser.T__12)
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
            self.elseif = None # ElifContext

        def truth(self):
            return self.getTypedRuleContext(GrammarParser.TruthContext,0)


        def brackets(self):
            return self.getTypedRuleContext(GrammarParser.BracketsContext,0)


        def elif_(self):
            return self.getTypedRuleContext(GrammarParser.ElifContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_conditional_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_statement" ):
                return visitor.visitConditional_statement(self)
            else:
                return visitor.visitChildren(self)




    def conditional_statement(self):

        localctx = GrammarParser.Conditional_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditional_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            localctx.label = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                localctx.label = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 135
            self.match(GrammarParser.T__8)
            self.state = 136
            localctx.t = self.truth(0)
            self.state = 137
            self.match(GrammarParser.T__10)
            self.state = 138
            self.match(GrammarParser.T__11)
            self.state = 139
            localctx.stmts = self.brackets(0)
            self.state = 140
            self.match(GrammarParser.T__12)
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 141
                localctx.elseif = self.elif_(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_elif

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ElseIfContext(ElifContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ElifContext
            super().__init__(parser)
            self.lhs = None # ElifContext
            self.rhs = None # ElifContext
            self.copyFrom(ctx)

        def elif_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ElifContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ElifContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIf" ):
                return visitor.visitElseIf(self)
            else:
                return visitor.visitChildren(self)


    class ElseElifContext(ElifContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ElifContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def else_(self):
            return self.getTypedRuleContext(GrammarParser.ElseContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseElif" ):
                return visitor.visitElseElif(self)
            else:
                return visitor.visitChildren(self)


    class AtomElifContext(ElifContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ElifContext
            super().__init__(parser)
            self.t = None # TruthContext
            self.stmts = None # BracketsContext
            self.copyFrom(ctx)

        def truth(self):
            return self.getTypedRuleContext(GrammarParser.TruthContext,0)

        def brackets(self):
            return self.getTypedRuleContext(GrammarParser.BracketsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomElif" ):
                return visitor.visitAtomElif(self)
            else:
                return visitor.visitChildren(self)



    def elif_(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ElifContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_elif, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = GrammarParser.AtomElifContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 145
                self.match(GrammarParser.T__15)
                self.state = 146
                self.match(GrammarParser.T__8)
                self.state = 147
                localctx.t = self.truth(0)
                self.state = 148
                self.match(GrammarParser.T__10)
                self.state = 149
                self.match(GrammarParser.T__11)
                self.state = 150
                localctx.stmts = self.brackets(0)
                self.state = 151
                self.match(GrammarParser.T__12)
                pass
            elif token in [17]:
                localctx = GrammarParser.ElseElifContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.else_()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ElseIfContext(self, GrammarParser.ElifContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_elif)
                    self.state = 156
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 157
                    localctx.rhs = self.elif_(4) 
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.stmts = None # BracketsContext

        def brackets(self):
            return self.getTypedRuleContext(GrammarParser.BracketsContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse" ):
                return visitor.visitElse(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = GrammarParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(GrammarParser.T__16)
            self.state = 164
            self.match(GrammarParser.T__11)
            self.state = 165
            localctx.stmts = self.brackets(0)
            self.state = 166
            self.match(GrammarParser.T__12)
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
            self.atom = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


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


    class DualTruthContext(TruthContext):

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
            if hasattr( visitor, "visitDualTruth" ):
                return visitor.visitDualTruth(self)
            else:
                return visitor.visitChildren(self)



    def truth(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.TruthContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_truth, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.ParenTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 169
                self.match(GrammarParser.T__8)
                self.state = 170
                localctx.t = self.truth(0)
                self.state = 171
                self.match(GrammarParser.T__10)
                pass

            elif la_ == 2:
                localctx = GrammarParser.DualTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                localctx.lhs = self.statement()
                self.state = 174
                localctx.operand = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                    localctx.operand = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 175
                localctx.rhs = self.statement()
                pass

            elif la_ == 3:
                localctx = GrammarParser.AtomTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 177
                localctx.atom = self.statement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.LogicTruthContext(self, GrammarParser.TruthContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_truth)
                    self.state = 180
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 181
                    localctx.logic = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==18 or _la==19):
                        localctx.logic = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 182
                    localctx.rhs = self.truth(4) 
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_function_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 188
                self.match(GrammarParser.T__2)
                pass
            elif token in [26]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 192
            self.match(GrammarParser.T__25)
            self.state = 193
            localctx.name = self.match(GrammarParser.VARNAME)
            self.state = 194
            self.match(GrammarParser.T__8)
            self.state = 195
            localctx.args = self.varname_list(0)
            self.state = 196
            self.match(GrammarParser.T__10)
            self.state = 197
            self.match(GrammarParser.T__11)
            self.state = 198
            localctx.stmts = self.brackets(0)
            self.state = 199
            self.match(GrammarParser.T__12)
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_varname_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomVarnameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 202
                localctx.atom = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NullVarnameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CommaVarnameContext(self, GrammarParser.Varname_listContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_varname_list)
                    self.state = 206
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 207
                    self.match(GrammarParser.T__26)
                    self.state = 208
                    localctx.rhs = self.varname_list(4) 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_var_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomVarlistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 215
                localctx.atom = self.statement()
                pass

            elif la_ == 2:
                localctx = GrammarParser.NullVarlistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CommaVarlistContext(self, GrammarParser.Var_listContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_var_list)
                    self.state = 219
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 220
                    self.match(GrammarParser.T__26)
                    self.state = 221
                    localctx.rhs = self.var_list(4) 
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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


    class AtomBracketStatementContext(BracketsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.BracketsContext
            super().__init__(parser)
            self.atom = None # Bracket_statementContext
            self.copyFrom(ctx)

        def bracket_statement(self):
            return self.getTypedRuleContext(GrammarParser.Bracket_statementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomBracketStatement" ):
                return visitor.visitAtomBracketStatement(self)
            else:
                return visitor.visitChildren(self)


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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_brackets, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomBracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 228
                localctx.atom = self.statement()
                self.state = 229
                self.match(GrammarParser.SEMI)
                pass

            elif la_ == 2:
                localctx = GrammarParser.AtomBracketStatementContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 231
                localctx.atom = self.bracket_statement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.SemiBracketsContext(self, GrammarParser.BracketsContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_brackets)
                    self.state = 234
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 235
                    localctx.rhs = self.brackets(4) 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 242
                self.match(GrammarParser.T__8)
                self.state = 243
                localctx.exp = self.expr(0)
                self.state = 244
                self.match(GrammarParser.T__10)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 246
                self.match(GrammarParser.SUB)
                self.state = 247
                localctx.exp = self.expr(10)
                pass

            elif la_ == 3:
                localctx = GrammarParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 248
                localctx.atom = self.match(GrammarParser.NUM)
                pass

            elif la_ == 4:
                localctx = GrammarParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 249
                localctx.atom = self.match(GrammarParser.BOOL)
                pass

            elif la_ == 5:
                localctx = GrammarParser.StrExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 250
                localctx.atom = self.match(GrammarParser.StringLiteral)
                pass

            elif la_ == 6:
                localctx = GrammarParser.NullExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 251
                localctx.atom = self.match(GrammarParser.NULL)
                pass

            elif la_ == 7:
                localctx = GrammarParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 252
                localctx.atom = self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 8:
                localctx = GrammarParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 253
                localctx.atom = self.var()
                pass

            elif la_ == 9:
                localctx = GrammarParser.Function_callContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 254
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 255
                self.match(GrammarParser.T__8)
                self.state = 256
                localctx.args = self.var_list(0)
                self.state = 257
                self.match(GrammarParser.T__10)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 267
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.OpExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 261
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 262
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==41 or _la==42):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 263
                        localctx.rhs = self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.OpExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 264
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 265
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 10445360463872) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 266
                        localctx.rhs = self.expr(9)
                        pass

             
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self._predicates[8] = self.elif_sempred
        self._predicates[10] = self.truth_sempred
        self._predicates[12] = self.varname_list_sempred
        self._predicates[13] = self.var_list_sempred
        self._predicates[14] = self.brackets_sempred
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def elif_sempred(self, localctx:ElifContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def truth_sempred(self, localctx:TruthContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def varname_list_sempred(self, localctx:Varname_listContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

    def var_list_sempred(self, localctx:Var_listContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

    def brackets_sempred(self, localctx:BracketsContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         




