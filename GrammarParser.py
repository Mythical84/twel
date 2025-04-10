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
        4,1,41,260,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,3,0,33,8,0,1,0,1,0,1,0,5,0,38,8,0,10,0,12,0,41,
        9,0,1,1,1,1,1,1,3,1,46,8,1,1,1,1,1,5,1,50,8,1,10,1,12,1,53,9,1,1,
        1,1,1,1,1,3,1,58,8,1,3,1,60,8,1,1,2,1,2,3,2,64,8,2,1,3,1,3,1,3,5,
        3,69,8,3,10,3,12,3,72,9,3,1,3,1,3,1,4,1,4,3,4,78,8,4,1,4,1,4,1,4,
        1,4,1,4,3,4,85,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,93,8,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,103,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,111,
        8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,120,8,5,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,3,6,130,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        3,7,142,8,7,1,7,1,7,5,7,146,8,7,10,7,12,7,149,9,7,1,8,1,8,1,8,1,
        8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,166,8,9,1,9,1,
        9,1,9,5,9,171,8,9,10,9,12,9,174,9,9,1,10,1,10,3,10,178,8,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,3,11,192,
        8,11,1,11,1,11,1,11,5,11,197,8,11,10,11,12,11,200,9,11,1,12,1,12,
        1,12,3,12,205,8,12,1,12,1,12,1,12,5,12,210,8,12,10,12,12,12,213,
        9,12,1,13,1,13,1,13,1,13,1,13,3,13,220,8,13,1,13,1,13,5,13,224,8,
        13,10,13,12,13,227,9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,247,8,14,
        1,14,1,14,1,14,1,14,1,14,1,14,5,14,255,8,14,10,14,12,14,258,9,14,
        1,14,0,6,14,18,22,24,26,28,15,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,0,5,1,0,8,9,1,0,18,23,1,0,16,17,1,0,39,40,2,0,37,38,41,41,
        287,0,39,1,0,0,0,2,59,1,0,0,0,4,63,1,0,0,0,6,65,1,0,0,0,8,110,1,
        0,0,0,10,119,1,0,0,0,12,121,1,0,0,0,14,141,1,0,0,0,16,150,1,0,0,
        0,18,165,1,0,0,0,20,177,1,0,0,0,22,191,1,0,0,0,24,204,1,0,0,0,26,
        219,1,0,0,0,28,246,1,0,0,0,30,33,3,2,1,0,31,33,3,6,3,0,32,30,1,0,
        0,0,32,31,1,0,0,0,33,34,1,0,0,0,34,35,5,26,0,0,35,38,1,0,0,0,36,
        38,3,4,2,0,37,32,1,0,0,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,
        0,39,40,1,0,0,0,40,1,1,0,0,0,41,39,1,0,0,0,42,46,3,28,14,0,43,46,
        3,8,4,0,44,46,3,10,5,0,45,42,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,
        46,60,1,0,0,0,47,48,5,36,0,0,48,50,5,1,0,0,49,47,1,0,0,0,50,53,1,
        0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,57,1,0,0,0,53,51,1,0,0,0,54,
        58,3,28,14,0,55,58,3,8,4,0,56,58,3,10,5,0,57,54,1,0,0,0,57,55,1,
        0,0,0,57,56,1,0,0,0,58,60,1,0,0,0,59,45,1,0,0,0,59,51,1,0,0,0,60,
        3,1,0,0,0,61,64,3,12,6,0,62,64,3,20,10,0,63,61,1,0,0,0,63,62,1,0,
        0,0,64,5,1,0,0,0,65,70,5,2,0,0,66,67,5,36,0,0,67,69,9,0,0,0,68,66,
        1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,
        72,70,1,0,0,0,73,74,5,36,0,0,74,7,1,0,0,0,75,78,5,3,0,0,76,78,1,
        0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,79,1,0,0,0,79,80,5,36,0,0,80,
        81,5,4,0,0,81,111,3,2,1,0,82,85,5,3,0,0,83,85,1,0,0,0,84,82,1,0,
        0,0,84,83,1,0,0,0,85,86,1,0,0,0,86,87,3,22,11,0,87,88,5,4,0,0,88,
        89,3,22,11,0,89,111,1,0,0,0,90,93,5,3,0,0,91,93,1,0,0,0,92,90,1,
        0,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,95,5,36,0,0,95,96,5,4,0,0,96,
        97,5,5,0,0,97,98,3,24,12,0,98,99,5,6,0,0,99,111,1,0,0,0,100,103,
        5,3,0,0,101,103,1,0,0,0,102,100,1,0,0,0,102,101,1,0,0,0,103,104,
        1,0,0,0,104,105,5,36,0,0,105,106,5,5,0,0,106,107,5,28,0,0,107,108,
        5,6,0,0,108,109,5,4,0,0,109,111,3,2,1,0,110,77,1,0,0,0,110,84,1,
        0,0,0,110,92,1,0,0,0,110,102,1,0,0,0,111,9,1,0,0,0,112,113,5,7,0,
        0,113,120,5,36,0,0,114,120,5,36,0,0,115,116,5,36,0,0,116,117,5,5,
        0,0,117,118,5,28,0,0,118,120,5,6,0,0,119,112,1,0,0,0,119,114,1,0,
        0,0,119,115,1,0,0,0,120,11,1,0,0,0,121,122,7,0,0,0,122,123,5,10,
        0,0,123,124,3,18,9,0,124,125,5,11,0,0,125,126,5,12,0,0,126,127,3,
        26,13,0,127,129,5,13,0,0,128,130,3,14,7,0,129,128,1,0,0,0,129,130,
        1,0,0,0,130,13,1,0,0,0,131,132,6,7,-1,0,132,133,5,14,0,0,133,134,
        5,10,0,0,134,135,3,18,9,0,135,136,5,11,0,0,136,137,5,12,0,0,137,
        138,3,26,13,0,138,139,5,13,0,0,139,142,1,0,0,0,140,142,3,16,8,0,
        141,131,1,0,0,0,141,140,1,0,0,0,142,147,1,0,0,0,143,144,10,3,0,0,
        144,146,3,14,7,4,145,143,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,
        147,148,1,0,0,0,148,15,1,0,0,0,149,147,1,0,0,0,150,151,5,15,0,0,
        151,152,5,12,0,0,152,153,3,26,13,0,153,154,5,13,0,0,154,17,1,0,0,
        0,155,156,6,9,-1,0,156,157,5,10,0,0,157,158,3,18,9,0,158,159,5,11,
        0,0,159,166,1,0,0,0,160,161,3,2,1,0,161,162,7,1,0,0,162,163,3,2,
        1,0,163,166,1,0,0,0,164,166,3,2,1,0,165,155,1,0,0,0,165,160,1,0,
        0,0,165,164,1,0,0,0,166,172,1,0,0,0,167,168,10,3,0,0,168,169,7,2,
        0,0,169,171,3,18,9,4,170,167,1,0,0,0,171,174,1,0,0,0,172,170,1,0,
        0,0,172,173,1,0,0,0,173,19,1,0,0,0,174,172,1,0,0,0,175,178,5,3,0,
        0,176,178,1,0,0,0,177,175,1,0,0,0,177,176,1,0,0,0,178,179,1,0,0,
        0,179,180,5,24,0,0,180,181,5,36,0,0,181,182,5,10,0,0,182,183,3,22,
        11,0,183,184,5,11,0,0,184,185,5,12,0,0,185,186,3,26,13,0,186,187,
        5,13,0,0,187,21,1,0,0,0,188,189,6,11,-1,0,189,192,5,36,0,0,190,192,
        1,0,0,0,191,188,1,0,0,0,191,190,1,0,0,0,192,198,1,0,0,0,193,194,
        10,3,0,0,194,195,5,25,0,0,195,197,3,22,11,4,196,193,1,0,0,0,197,
        200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,23,1,0,0,0,200,198,
        1,0,0,0,201,202,6,12,-1,0,202,205,3,2,1,0,203,205,1,0,0,0,204,201,
        1,0,0,0,204,203,1,0,0,0,205,211,1,0,0,0,206,207,10,3,0,0,207,208,
        5,25,0,0,208,210,3,24,12,4,209,206,1,0,0,0,210,213,1,0,0,0,211,209,
        1,0,0,0,211,212,1,0,0,0,212,25,1,0,0,0,213,211,1,0,0,0,214,215,6,
        13,-1,0,215,216,3,2,1,0,216,217,5,26,0,0,217,220,1,0,0,0,218,220,
        3,4,2,0,219,214,1,0,0,0,219,218,1,0,0,0,220,225,1,0,0,0,221,222,
        10,3,0,0,222,224,3,26,13,4,223,221,1,0,0,0,224,227,1,0,0,0,225,223,
        1,0,0,0,225,226,1,0,0,0,226,27,1,0,0,0,227,225,1,0,0,0,228,229,6,
        14,-1,0,229,230,5,10,0,0,230,231,3,28,14,0,231,232,5,11,0,0,232,
        247,1,0,0,0,233,234,5,38,0,0,234,247,3,28,14,10,235,247,5,28,0,0,
        236,247,5,30,0,0,237,247,5,31,0,0,238,247,5,33,0,0,239,247,5,29,
        0,0,240,247,3,10,5,0,241,242,5,36,0,0,242,243,5,10,0,0,243,244,3,
        24,12,0,244,245,5,11,0,0,245,247,1,0,0,0,246,228,1,0,0,0,246,233,
        1,0,0,0,246,235,1,0,0,0,246,236,1,0,0,0,246,237,1,0,0,0,246,238,
        1,0,0,0,246,239,1,0,0,0,246,240,1,0,0,0,246,241,1,0,0,0,247,256,
        1,0,0,0,248,249,10,9,0,0,249,250,7,3,0,0,250,255,3,28,14,10,251,
        252,10,8,0,0,252,253,7,4,0,0,253,255,3,28,14,9,254,248,1,0,0,0,254,
        251,1,0,0,0,255,258,1,0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,
        29,1,0,0,0,258,256,1,0,0,0,30,32,37,39,45,51,57,59,63,70,77,84,92,
        102,110,119,129,141,147,165,172,177,191,198,204,211,219,225,246,
        254,256
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'import'", "'public'", "'='", 
                     "'['", "']'", "'!'", "'if'", "'while'", "'('", "')'", 
                     "'{'", "'}'", "'elif'", "'else'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'def'", "','", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'null'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_imp = 3
    RULE_var_declaration = 4
    RULE_var = 5
    RULE_conditional_statement = 6
    RULE_elif = 7
    RULE_else = 8
    RULE_truth = 9
    RULE_function_def = 10
    RULE_varname_list = 11
    RULE_var_list = 12
    RULE_brackets = 13
    RULE_expr = 14

    ruleNames =  [ "prog", "statement", "bracket_statement", "imp", "var_declaration", 
                   "var", "conditional_statement", "elif", "else", "truth", 
                   "function_def", "varname_list", "var_list", "brackets", 
                   "expr" ]

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
    SEMI=26
    NL=27
    NUM=28
    FLOAT=29
    BOOL=30
    StringLiteral=31
    UnterminatedStringLiteral=32
    NULL=33
    BlockComment=34
    Comment=35
    VARNAME=36
    ADD=37
    SUB=38
    MUL=39
    DIV=40
    MOD=41

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
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        self.state = 32
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                        if la_ == 1:
                            self.state = 30
                            self.statement()
                            pass

                        elif la_ == 2:
                            self.state = 31
                            self.imp()
                            pass


                        self.state = 34
                        self.match(GrammarParser.SEMI)
                        pass

                    elif la_ == 2:
                        self.state = 36
                        self.bracket_statement()
                        pass

             
                self.state = 41
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
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.NormalStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 42
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 43
                    self.var_declaration()
                    pass

                elif la_ == 3:
                    self.state = 44
                    self.var()
                    pass


                pass

            elif la_ == 2:
                localctx = GrammarParser.FileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 47
                        self.match(GrammarParser.VARNAME)
                        self.state = 48
                        self.match(GrammarParser.T__0) 
                    self.state = 53
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 57
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 54
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 55
                    self.var_declaration()
                    pass

                elif la_ == 3:
                    self.state = 56
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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9]:
                self.state = 61
                self.conditional_statement()
                pass
            elif token in [3, 24]:
                self.state = 62
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
            self.state = 65
            self.match(GrammarParser.T__1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    self.match(GrammarParser.VARNAME)
                    self.state = 67
                    self.matchWildcard() 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 73
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
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.SingleVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 75
                    self.match(GrammarParser.T__2)
                    pass
                elif token in [36]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 79
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 80
                self.match(GrammarParser.T__3)
                self.state = 81
                localctx.exp = self.statement()
                pass

            elif la_ == 2:
                localctx = GrammarParser.MultiVarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 82
                    self.match(GrammarParser.T__2)
                    pass

                elif la_ == 2:
                    pass


                self.state = 86
                localctx.name = self.varname_list(0)
                self.state = 87
                self.match(GrammarParser.T__3)
                self.state = 88
                localctx.vals = self.varname_list(0)
                pass

            elif la_ == 3:
                localctx = GrammarParser.ListVarContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 90
                    self.match(GrammarParser.T__2)
                    pass
                elif token in [36]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 94
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 95
                self.match(GrammarParser.T__3)
                self.state = 96
                self.match(GrammarParser.T__4)
                self.state = 97
                localctx.vals = self.var_list(0)
                self.state = 98
                self.match(GrammarParser.T__5)
                pass

            elif la_ == 4:
                localctx = GrammarParser.ListSetContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 100
                    self.match(GrammarParser.T__2)
                    pass
                elif token in [36]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 104
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 105
                self.match(GrammarParser.T__4)
                self.state = 106
                localctx.index = self.match(GrammarParser.NUM)
                self.state = 107
                self.match(GrammarParser.T__5)
                self.state = 108
                self.match(GrammarParser.T__3)
                self.state = 109
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
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.InvertVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                localctx.inv = self.match(GrammarParser.T__6)
                self.state = 113
                localctx.name = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 2:
                localctx = GrammarParser.VarNameContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                localctx.name = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 3:
                localctx = GrammarParser.ListGetContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 116
                self.match(GrammarParser.T__4)
                self.state = 117
                localctx.index = self.match(GrammarParser.NUM)
                self.state = 118
                self.match(GrammarParser.T__5)
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
        self.enterRule(localctx, 12, self.RULE_conditional_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            localctx.label = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                localctx.label = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 122
            self.match(GrammarParser.T__9)
            self.state = 123
            localctx.t = self.truth(0)
            self.state = 124
            self.match(GrammarParser.T__10)
            self.state = 125
            self.match(GrammarParser.T__11)
            self.state = 126
            localctx.stmts = self.brackets(0)
            self.state = 127
            self.match(GrammarParser.T__12)
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 128
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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_elif, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = GrammarParser.AtomElifContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 132
                self.match(GrammarParser.T__13)
                self.state = 133
                self.match(GrammarParser.T__9)
                self.state = 134
                localctx.t = self.truth(0)
                self.state = 135
                self.match(GrammarParser.T__10)
                self.state = 136
                self.match(GrammarParser.T__11)
                self.state = 137
                localctx.stmts = self.brackets(0)
                self.state = 138
                self.match(GrammarParser.T__12)
                pass
            elif token in [15]:
                localctx = GrammarParser.ElseElifContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.else_()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 147
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
                    self.state = 143
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 144
                    localctx.rhs = self.elif_(4) 
                self.state = 149
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
        self.enterRule(localctx, 16, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(GrammarParser.T__14)
            self.state = 151
            self.match(GrammarParser.T__11)
            self.state = 152
            localctx.stmts = self.brackets(0)
            self.state = 153
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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_truth, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.ParenTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 156
                self.match(GrammarParser.T__9)
                self.state = 157
                localctx.t = self.truth(0)
                self.state = 158
                self.match(GrammarParser.T__10)
                pass

            elif la_ == 2:
                localctx = GrammarParser.DualTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 160
                localctx.lhs = self.statement()
                self.state = 161
                localctx.operand = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                    localctx.operand = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 162
                localctx.rhs = self.statement()
                pass

            elif la_ == 3:
                localctx = GrammarParser.AtomTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 164
                localctx.atom = self.statement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 172
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
                    self.state = 167
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 168
                    localctx.logic = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==17):
                        localctx.logic = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 169
                    localctx.rhs = self.truth(4) 
                self.state = 174
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
        self.enterRule(localctx, 20, self.RULE_function_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 175
                self.match(GrammarParser.T__2)
                pass
            elif token in [24]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 179
            self.match(GrammarParser.T__23)
            self.state = 180
            localctx.name = self.match(GrammarParser.VARNAME)
            self.state = 181
            self.match(GrammarParser.T__9)
            self.state = 182
            localctx.args = self.varname_list(0)
            self.state = 183
            self.match(GrammarParser.T__10)
            self.state = 184
            self.match(GrammarParser.T__11)
            self.state = 185
            localctx.stmts = self.brackets(0)
            self.state = 186
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_varname_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomVarnameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 189
                localctx.atom = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NullVarnameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 198
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
                    self.state = 193
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 194
                    self.match(GrammarParser.T__24)
                    self.state = 195
                    localctx.rhs = self.varname_list(4) 
                self.state = 200
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_var_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomVarlistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 202
                localctx.atom = self.statement()
                pass

            elif la_ == 2:
                localctx = GrammarParser.NullVarlistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 211
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
                    self.state = 206
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 207
                    self.match(GrammarParser.T__24)
                    self.state = 208
                    localctx.rhs = self.var_list(4) 
                self.state = 213
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_brackets, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomBracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 215
                localctx.atom = self.statement()
                self.state = 216
                self.match(GrammarParser.SEMI)
                pass

            elif la_ == 2:
                localctx = GrammarParser.AtomBracketStatementContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 218
                localctx.atom = self.bracket_statement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 225
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
                    self.state = 221
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 222
                    localctx.rhs = self.brackets(4) 
                self.state = 227
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 229
                self.match(GrammarParser.T__9)
                self.state = 230
                localctx.exp = self.expr(0)
                self.state = 231
                self.match(GrammarParser.T__10)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 233
                self.match(GrammarParser.SUB)
                self.state = 234
                localctx.exp = self.expr(10)
                pass

            elif la_ == 3:
                localctx = GrammarParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 235
                localctx.atom = self.match(GrammarParser.NUM)
                pass

            elif la_ == 4:
                localctx = GrammarParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 236
                localctx.atom = self.match(GrammarParser.BOOL)
                pass

            elif la_ == 5:
                localctx = GrammarParser.StrExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 237
                localctx.atom = self.match(GrammarParser.StringLiteral)
                pass

            elif la_ == 6:
                localctx = GrammarParser.NullExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 238
                localctx.atom = self.match(GrammarParser.NULL)
                pass

            elif la_ == 7:
                localctx = GrammarParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 239
                localctx.atom = self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 8:
                localctx = GrammarParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 240
                localctx.atom = self.var()
                pass

            elif la_ == 9:
                localctx = GrammarParser.Function_callContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 241
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 242
                self.match(GrammarParser.T__9)
                self.state = 243
                localctx.args = self.var_list(0)
                self.state = 244
                self.match(GrammarParser.T__10)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 254
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.OpExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 248
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 249
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==39 or _la==40):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 250
                        localctx.rhs = self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.OpExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 251
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 252
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2611340115968) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 253
                        localctx.rhs = self.expr(9)
                        pass

             
                self.state = 258
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
        self._predicates[7] = self.elif_sempred
        self._predicates[9] = self.truth_sempred
        self._predicates[11] = self.varname_list_sempred
        self._predicates[12] = self.var_list_sempred
        self._predicates[13] = self.brackets_sempred
        self._predicates[14] = self.expr_sempred
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
         




