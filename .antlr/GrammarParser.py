# Generated from c:/Users/tartinger2025/Documents/Mythic Script/Grammar.g4 by ANTLR 4.13.1
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
        4,1,35,226,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        3,0,29,8,0,1,0,1,0,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,1,1,1,1,1,1,
        1,3,1,43,8,1,1,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,1,1,1,1,1,1,1,
        3,1,56,8,1,3,1,58,8,1,1,2,1,2,3,2,62,8,2,1,3,1,3,1,3,5,3,67,8,3,
        10,3,12,3,70,9,3,1,3,1,3,1,4,1,4,3,4,76,8,4,1,4,1,4,1,4,1,4,1,4,
        3,4,83,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,91,8,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,3,4,101,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,109,8,4,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,118,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,135,8,7,1,7,1,7,1,7,5,7,140,
        8,7,10,7,12,7,143,9,7,1,8,1,8,3,8,147,8,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,161,8,9,1,9,1,9,1,9,5,9,166,8,9,10,
        9,12,9,169,9,9,1,10,1,10,1,10,3,10,174,8,10,1,10,1,10,1,10,5,10,
        179,8,10,10,10,12,10,182,9,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,
        190,8,11,10,11,12,11,193,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,213,
        8,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,221,8,12,10,12,12,12,224,
        9,12,1,12,0,5,14,18,20,22,24,13,0,2,4,6,8,10,12,14,16,18,20,22,24,
        0,5,1,0,8,9,1,0,14,15,1,0,12,13,1,0,33,34,2,0,31,32,35,35,252,0,
        35,1,0,0,0,2,57,1,0,0,0,4,61,1,0,0,0,6,63,1,0,0,0,8,108,1,0,0,0,
        10,117,1,0,0,0,12,119,1,0,0,0,14,134,1,0,0,0,16,146,1,0,0,0,18,160,
        1,0,0,0,20,173,1,0,0,0,22,183,1,0,0,0,24,212,1,0,0,0,26,29,3,2,1,
        0,27,29,3,6,3,0,28,26,1,0,0,0,28,27,1,0,0,0,29,30,1,0,0,0,30,31,
        5,20,0,0,31,34,1,0,0,0,32,34,3,4,2,0,33,28,1,0,0,0,33,32,1,0,0,0,
        34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,1,1,0,0,0,37,35,1,0,
        0,0,38,43,3,24,12,0,39,43,3,8,4,0,40,43,3,10,5,0,41,43,3,12,6,0,
        42,38,1,0,0,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,58,1,
        0,0,0,44,45,5,30,0,0,45,47,5,1,0,0,46,44,1,0,0,0,47,50,1,0,0,0,48,
        46,1,0,0,0,48,49,1,0,0,0,49,55,1,0,0,0,50,48,1,0,0,0,51,56,3,24,
        12,0,52,56,3,8,4,0,53,56,3,10,5,0,54,56,3,12,6,0,55,51,1,0,0,0,55,
        52,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,58,1,0,0,0,57,42,1,0,0,
        0,57,48,1,0,0,0,58,3,1,0,0,0,59,62,3,12,6,0,60,62,3,16,8,0,61,59,
        1,0,0,0,61,60,1,0,0,0,62,5,1,0,0,0,63,68,5,2,0,0,64,65,5,30,0,0,
        65,67,9,0,0,0,66,64,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,
        0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,72,5,30,0,0,72,7,1,0,0,0,73,
        76,5,3,0,0,74,76,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,77,1,0,0,
        0,77,78,5,30,0,0,78,79,5,4,0,0,79,109,3,2,1,0,80,83,5,3,0,0,81,83,
        1,0,0,0,82,80,1,0,0,0,82,81,1,0,0,0,83,84,1,0,0,0,84,85,3,18,9,0,
        85,86,5,4,0,0,86,87,3,18,9,0,87,109,1,0,0,0,88,91,5,3,0,0,89,91,
        1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,92,1,0,0,0,92,93,5,30,0,0,
        93,94,5,4,0,0,94,95,5,5,0,0,95,96,3,20,10,0,96,97,5,6,0,0,97,109,
        1,0,0,0,98,101,5,3,0,0,99,101,1,0,0,0,100,98,1,0,0,0,100,99,1,0,
        0,0,101,102,1,0,0,0,102,103,5,30,0,0,103,104,5,5,0,0,104,105,5,22,
        0,0,105,106,5,6,0,0,106,107,5,4,0,0,107,109,3,2,1,0,108,75,1,0,0,
        0,108,82,1,0,0,0,108,90,1,0,0,0,108,100,1,0,0,0,109,9,1,0,0,0,110,
        111,5,7,0,0,111,118,5,30,0,0,112,118,5,30,0,0,113,114,5,30,0,0,114,
        115,5,5,0,0,115,116,5,22,0,0,116,118,5,6,0,0,117,110,1,0,0,0,117,
        112,1,0,0,0,117,113,1,0,0,0,118,11,1,0,0,0,119,120,7,0,0,0,120,121,
        5,10,0,0,121,122,3,14,7,0,122,123,5,11,0,0,123,124,3,22,11,0,124,
        13,1,0,0,0,125,126,6,7,-1,0,126,127,5,10,0,0,127,128,3,14,7,0,128,
        129,5,11,0,0,129,135,1,0,0,0,130,131,3,2,1,0,131,132,7,1,0,0,132,
        133,3,2,1,0,133,135,1,0,0,0,134,125,1,0,0,0,134,130,1,0,0,0,135,
        141,1,0,0,0,136,137,10,2,0,0,137,138,7,2,0,0,138,140,3,14,7,3,139,
        136,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,
        15,1,0,0,0,143,141,1,0,0,0,144,147,5,3,0,0,145,147,1,0,0,0,146,144,
        1,0,0,0,146,145,1,0,0,0,147,148,1,0,0,0,148,149,5,16,0,0,149,150,
        5,30,0,0,150,151,5,10,0,0,151,152,3,18,9,0,152,153,5,11,0,0,153,
        154,5,17,0,0,154,155,3,22,11,0,155,156,5,18,0,0,156,17,1,0,0,0,157,
        158,6,9,-1,0,158,161,5,30,0,0,159,161,1,0,0,0,160,157,1,0,0,0,160,
        159,1,0,0,0,161,167,1,0,0,0,162,163,10,3,0,0,163,164,5,19,0,0,164,
        166,3,18,9,4,165,162,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,
        168,1,0,0,0,168,19,1,0,0,0,169,167,1,0,0,0,170,171,6,10,-1,0,171,
        174,3,2,1,0,172,174,1,0,0,0,173,170,1,0,0,0,173,172,1,0,0,0,174,
        180,1,0,0,0,175,176,10,3,0,0,176,177,5,19,0,0,177,179,3,20,10,4,
        178,175,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,
        181,21,1,0,0,0,182,180,1,0,0,0,183,184,6,11,-1,0,184,185,3,2,1,0,
        185,186,5,20,0,0,186,191,1,0,0,0,187,188,10,2,0,0,188,190,3,22,11,
        3,189,187,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,
        0,192,23,1,0,0,0,193,191,1,0,0,0,194,195,6,12,-1,0,195,196,5,10,
        0,0,196,197,3,24,12,0,197,198,5,11,0,0,198,213,1,0,0,0,199,200,5,
        32,0,0,200,213,3,24,12,10,201,213,5,22,0,0,202,213,5,24,0,0,203,
        213,5,25,0,0,204,213,5,27,0,0,205,213,5,23,0,0,206,213,3,10,5,0,
        207,208,5,30,0,0,208,209,5,10,0,0,209,210,3,20,10,0,210,211,5,11,
        0,0,211,213,1,0,0,0,212,194,1,0,0,0,212,199,1,0,0,0,212,201,1,0,
        0,0,212,202,1,0,0,0,212,203,1,0,0,0,212,204,1,0,0,0,212,205,1,0,
        0,0,212,206,1,0,0,0,212,207,1,0,0,0,213,222,1,0,0,0,214,215,10,9,
        0,0,215,216,7,3,0,0,216,221,3,24,12,10,217,218,10,8,0,0,218,219,
        7,4,0,0,219,221,3,24,12,9,220,214,1,0,0,0,220,217,1,0,0,0,221,224,
        1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,25,1,0,0,0,224,222,1,
        0,0,0,26,28,33,35,42,48,55,57,61,68,75,82,90,100,108,117,134,141,
        146,160,167,173,180,191,212,220,222
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'import'", "'public'", "'='", 
                     "'['", "']'", "'!'", "'if'", "'while'", "'('", "')'", 
                     "'&&'", "'||'", "'=='", "'!='", "'def'", "'{'", "'}'", 
                     "','", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'null'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_conditional_statement = 6
    RULE_truth = 7
    RULE_function_def = 8
    RULE_varname_list = 9
    RULE_var_list = 10
    RULE_brackets = 11
    RULE_expr = 12

    ruleNames =  [ "prog", "statement", "bracket_statement", "imp", "var_declaration", 
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
    T__17=18
    T__18=19
    SEMI=20
    NL=21
    NUM=22
    FLOAT=23
    BOOL=24
    StringLiteral=25
    UnterminatedStringLiteral=26
    NULL=27
    BlockComment=28
    Comment=29
    VARNAME=30
    ADD=31
    SUB=32
    MUL=33
    DIV=34
    MOD=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
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




    def prog(self):

        localctx = GrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        self.state = 28
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                        if la_ == 1:
                            self.state = 26
                            self.statement()
                            pass

                        elif la_ == 2:
                            self.state = 27
                            self.imp()
                            pass


                        self.state = 30
                        self.match(GrammarParser.SEMI)
                        pass

                    elif la_ == 2:
                        self.state = 32
                        self.bracket_statement()
                        pass

             
                self.state = 37
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

        def conditional_statement(self):
            return self.getTypedRuleContext(GrammarParser.Conditional_statementContext,0)



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

        def conditional_statement(self):
            return self.getTypedRuleContext(GrammarParser.Conditional_statementContext,0)

        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.VARNAME)
            else:
                return self.getToken(GrammarParser.VARNAME, i)



    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.NormalStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 38
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 39
                    self.var_declaration()
                    pass

                elif la_ == 3:
                    self.state = 40
                    self.var()
                    pass

                elif la_ == 4:
                    self.state = 41
                    self.conditional_statement()
                    pass


                pass

            elif la_ == 2:
                localctx = GrammarParser.FileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 44
                        self.match(GrammarParser.VARNAME)
                        self.state = 45
                        self.match(GrammarParser.T__0) 
                    self.state = 50
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 55
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 51
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 52
                    self.var_declaration()
                    pass

                elif la_ == 3:
                    self.state = 53
                    self.var()
                    pass

                elif la_ == 4:
                    self.state = 54
                    self.conditional_statement()
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




    def bracket_statement(self):

        localctx = GrammarParser.Bracket_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bracket_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9]:
                self.state = 59
                self.conditional_statement()
                pass
            elif token in [3, 16]:
                self.state = 60
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




    def imp(self):

        localctx = GrammarParser.ImpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_imp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(GrammarParser.T__1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 64
                    self.match(GrammarParser.VARNAME)
                    self.state = 65
                    self.matchWildcard() 
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 71
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




    def var_declaration(self):

        localctx = GrammarParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_declaration)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.SingleVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 73
                    self.match(GrammarParser.T__2)
                    pass
                elif token in [30]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 77
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 78
                self.match(GrammarParser.T__3)
                self.state = 79
                localctx.exp = self.statement()
                pass

            elif la_ == 2:
                localctx = GrammarParser.MultiVarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 80
                    self.match(GrammarParser.T__2)
                    pass

                elif la_ == 2:
                    pass


                self.state = 84
                localctx.name = self.varname_list(0)
                self.state = 85
                self.match(GrammarParser.T__3)
                self.state = 86
                localctx.vals = self.varname_list(0)
                pass

            elif la_ == 3:
                localctx = GrammarParser.ListVarContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 88
                    self.match(GrammarParser.T__2)
                    pass
                elif token in [30]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 92
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 93
                self.match(GrammarParser.T__3)
                self.state = 94
                self.match(GrammarParser.T__4)
                self.state = 95
                localctx.vals = self.var_list(0)
                self.state = 96
                self.match(GrammarParser.T__5)
                pass

            elif la_ == 4:
                localctx = GrammarParser.ListSetContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 100
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 98
                    self.match(GrammarParser.T__2)
                    pass
                elif token in [30]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 102
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 103
                self.match(GrammarParser.T__4)
                self.state = 104
                localctx.index = self.match(GrammarParser.NUM)
                self.state = 105
                self.match(GrammarParser.T__5)
                self.state = 106
                self.match(GrammarParser.T__3)
                self.state = 107
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


    class VarNameContext(VarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.VarContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)


    class InvertVarContext(VarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.VarContext
            super().__init__(parser)
            self.inv = None # Token
            self.name = None # Token
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)



    def var(self):

        localctx = GrammarParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.InvertVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                localctx.inv = self.match(GrammarParser.T__6)
                self.state = 111
                localctx.name = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 2:
                localctx = GrammarParser.VarNameContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                localctx.name = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 3:
                localctx = GrammarParser.ListGetContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 114
                self.match(GrammarParser.T__4)
                self.state = 115
                localctx.index = self.match(GrammarParser.NUM)
                self.state = 116
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

        def truth(self):
            return self.getTypedRuleContext(GrammarParser.TruthContext,0)


        def brackets(self):
            return self.getTypedRuleContext(GrammarParser.BracketsContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_conditional_statement




    def conditional_statement(self):

        localctx = GrammarParser.Conditional_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_conditional_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            localctx.label = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                localctx.label = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 120
            self.match(GrammarParser.T__9)
            self.state = 121
            localctx.t = self.truth(0)
            self.state = 122
            self.match(GrammarParser.T__10)
            self.state = 123
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




    def truth(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.TruthContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_truth, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.ParenTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 126
                self.match(GrammarParser.T__9)
                self.state = 127
                localctx.t = self.truth(0)
                self.state = 128
                self.match(GrammarParser.T__10)
                pass

            elif la_ == 2:
                localctx = GrammarParser.AtomTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                localctx.lhs = self.statement()
                self.state = 131
                localctx.operand = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    localctx.operand = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 132
                localctx.rhs = self.statement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.LogicTruthContext(self, GrammarParser.TruthContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_truth)
                    self.state = 136
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 137
                    localctx.logic = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==12 or _la==13):
                        localctx.logic = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 138
                    localctx.rhs = self.truth(3) 
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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




    def function_def(self):

        localctx = GrammarParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_function_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 144
                self.match(GrammarParser.T__2)
                pass
            elif token in [16]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 148
            self.match(GrammarParser.T__15)
            self.state = 149
            localctx.name = self.match(GrammarParser.VARNAME)
            self.state = 150
            self.match(GrammarParser.T__9)
            self.state = 151
            localctx.args = self.varname_list(0)
            self.state = 152
            self.match(GrammarParser.T__10)
            self.state = 153
            self.match(GrammarParser.T__16)
            self.state = 154
            localctx.stmts = self.brackets(0)
            self.state = 155
            self.match(GrammarParser.T__17)
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



    class AtomVarnameContext(Varname_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Varname_listContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(GrammarParser.VARNAME, 0)


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




    def varname_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.Varname_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_varname_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomVarnameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 158
                localctx.atom = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NullVarnameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CommaVarnameContext(self, GrammarParser.Varname_listContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_varname_list)
                    self.state = 162
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 163
                    self.match(GrammarParser.T__18)
                    self.state = 164
                    localctx.rhs = self.varname_list(4) 
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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



    class AtomVarlistContext(Var_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.Var_listContext
            super().__init__(parser)
            self.atom = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)



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




    def var_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.Var_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_var_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomVarlistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 171
                localctx.atom = self.statement()
                pass

            elif la_ == 2:
                localctx = GrammarParser.NullVarlistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CommaVarlistContext(self, GrammarParser.Var_listContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_var_list)
                    self.state = 175
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 176
                    self.match(GrammarParser.T__18)
                    self.state = 177
                    localctx.rhs = self.var_list(4) 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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



    class AtomBracketsContext(BracketsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.BracketsContext
            super().__init__(parser)
            self.atom = None # StatementContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(GrammarParser.SEMI, 0)
        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)




    def brackets(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.BracketsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_brackets, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = GrammarParser.AtomBracketsContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 184
            localctx.atom = self.statement()
            self.state = 185
            self.match(GrammarParser.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.SemiBracketsContext(self, GrammarParser.BracketsContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_brackets)
                    self.state = 187
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 188
                    localctx.rhs = self.brackets(3) 
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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


    class FloatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)


    class VarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # VarContext
            self.copyFrom(ctx)

        def var(self):
            return self.getTypedRuleContext(GrammarParser.VarContext,0)



    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(GrammarParser.NUM, 0)


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


    class NullExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(GrammarParser.NULL, 0)


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



    class NegExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.exp = None # ExprContext
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(GrammarParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)



    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.exp = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)



    class BoolExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(GrammarParser.BOOL, 0)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 195
                self.match(GrammarParser.T__9)
                self.state = 196
                localctx.exp = self.expr(0)
                self.state = 197
                self.match(GrammarParser.T__10)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 199
                self.match(GrammarParser.SUB)
                self.state = 200
                localctx.exp = self.expr(10)
                pass

            elif la_ == 3:
                localctx = GrammarParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 201
                localctx.atom = self.match(GrammarParser.NUM)
                pass

            elif la_ == 4:
                localctx = GrammarParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 202
                localctx.atom = self.match(GrammarParser.BOOL)
                pass

            elif la_ == 5:
                localctx = GrammarParser.StrExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 203
                localctx.atom = self.match(GrammarParser.StringLiteral)
                pass

            elif la_ == 6:
                localctx = GrammarParser.NullExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 204
                localctx.atom = self.match(GrammarParser.NULL)
                pass

            elif la_ == 7:
                localctx = GrammarParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 205
                localctx.atom = self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 8:
                localctx = GrammarParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 206
                localctx.atom = self.var()
                pass

            elif la_ == 9:
                localctx = GrammarParser.Function_callContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 207
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 208
                self.match(GrammarParser.T__9)
                self.state = 209
                localctx.args = self.var_list(0)
                self.state = 210
                self.match(GrammarParser.T__10)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 220
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.OpExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 214
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 215
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==33 or _la==34):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 216
                        localctx.rhs = self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.OpExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 217
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 218
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 40802189312) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 219
                        localctx.rhs = self.expr(9)
                        pass

             
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self._predicates[7] = self.truth_sempred
        self._predicates[9] = self.varname_list_sempred
        self._predicates[10] = self.var_list_sempred
        self._predicates[11] = self.brackets_sempred
        self._predicates[12] = self.expr_sempred
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
         




