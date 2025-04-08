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
        4,1,34,216,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,1,1,1,5,1,38,8,1,10,1,12,1,
        41,9,1,1,1,1,1,1,1,1,1,1,1,3,1,48,8,1,1,2,1,2,3,2,52,8,2,1,3,1,3,
        1,3,5,3,57,8,3,10,3,12,3,60,9,3,1,3,1,3,1,4,1,4,3,4,66,8,4,1,4,1,
        4,1,4,1,4,1,4,3,4,73,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,81,8,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,91,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,
        4,99,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,108,8,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,125,8,7,1,7,1,7,
        1,7,5,7,130,8,7,10,7,12,7,133,9,7,1,8,1,8,3,8,137,8,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,151,8,9,1,9,1,9,1,9,5,
        9,156,8,9,10,9,12,9,159,9,9,1,10,1,10,1,10,3,10,164,8,10,1,10,1,
        10,1,10,5,10,169,8,10,10,10,12,10,172,9,10,1,11,1,11,1,11,1,11,1,
        11,1,11,5,11,180,8,11,10,11,12,11,183,9,11,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,3,12,203,8,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,211,8,12,10,
        12,12,12,214,9,12,1,12,0,5,14,18,20,22,24,13,0,2,4,6,8,10,12,14,
        16,18,20,22,24,0,5,1,0,7,8,1,0,13,14,1,0,11,12,1,0,32,33,2,0,30,
        31,34,34,238,0,32,1,0,0,0,2,39,1,0,0,0,4,51,1,0,0,0,6,53,1,0,0,0,
        8,98,1,0,0,0,10,107,1,0,0,0,12,109,1,0,0,0,14,124,1,0,0,0,16,136,
        1,0,0,0,18,150,1,0,0,0,20,163,1,0,0,0,22,173,1,0,0,0,24,202,1,0,
        0,0,26,27,3,2,1,0,27,28,5,19,0,0,28,31,1,0,0,0,29,31,3,4,2,0,30,
        26,1,0,0,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,
        0,33,1,1,0,0,0,34,32,1,0,0,0,35,36,5,29,0,0,36,38,9,0,0,0,37,35,
        1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,47,1,0,0,0,
        41,39,1,0,0,0,42,48,3,24,12,0,43,48,3,8,4,0,44,48,3,10,5,0,45,48,
        3,12,6,0,46,48,3,6,3,0,47,42,1,0,0,0,47,43,1,0,0,0,47,44,1,0,0,0,
        47,45,1,0,0,0,47,46,1,0,0,0,48,3,1,0,0,0,49,52,3,12,6,0,50,52,3,
        16,8,0,51,49,1,0,0,0,51,50,1,0,0,0,52,5,1,0,0,0,53,58,5,1,0,0,54,
        55,5,29,0,0,55,57,9,0,0,0,56,54,1,0,0,0,57,60,1,0,0,0,58,56,1,0,
        0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,62,5,29,0,0,62,
        7,1,0,0,0,63,66,5,2,0,0,64,66,1,0,0,0,65,63,1,0,0,0,65,64,1,0,0,
        0,66,67,1,0,0,0,67,68,5,29,0,0,68,69,5,3,0,0,69,99,3,2,1,0,70,73,
        5,2,0,0,71,73,1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,0,73,74,1,0,0,0,
        74,75,3,18,9,0,75,76,5,3,0,0,76,77,3,18,9,0,77,99,1,0,0,0,78,81,
        5,2,0,0,79,81,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,82,1,0,0,0,
        82,83,5,29,0,0,83,84,5,3,0,0,84,85,5,4,0,0,85,86,3,20,10,0,86,87,
        5,5,0,0,87,99,1,0,0,0,88,91,5,2,0,0,89,91,1,0,0,0,90,88,1,0,0,0,
        90,89,1,0,0,0,91,92,1,0,0,0,92,93,5,29,0,0,93,94,5,4,0,0,94,95,5,
        21,0,0,95,96,5,5,0,0,96,97,5,3,0,0,97,99,3,2,1,0,98,65,1,0,0,0,98,
        72,1,0,0,0,98,80,1,0,0,0,98,90,1,0,0,0,99,9,1,0,0,0,100,101,5,6,
        0,0,101,108,5,29,0,0,102,108,5,29,0,0,103,104,5,29,0,0,104,105,5,
        4,0,0,105,106,5,21,0,0,106,108,5,5,0,0,107,100,1,0,0,0,107,102,1,
        0,0,0,107,103,1,0,0,0,108,11,1,0,0,0,109,110,7,0,0,0,110,111,5,9,
        0,0,111,112,3,14,7,0,112,113,5,10,0,0,113,114,3,22,11,0,114,13,1,
        0,0,0,115,116,6,7,-1,0,116,117,5,9,0,0,117,118,3,14,7,0,118,119,
        5,10,0,0,119,125,1,0,0,0,120,121,3,2,1,0,121,122,7,1,0,0,122,123,
        3,2,1,0,123,125,1,0,0,0,124,115,1,0,0,0,124,120,1,0,0,0,125,131,
        1,0,0,0,126,127,10,2,0,0,127,128,7,2,0,0,128,130,3,14,7,3,129,126,
        1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,15,1,
        0,0,0,133,131,1,0,0,0,134,137,5,2,0,0,135,137,1,0,0,0,136,134,1,
        0,0,0,136,135,1,0,0,0,137,138,1,0,0,0,138,139,5,15,0,0,139,140,5,
        29,0,0,140,141,5,9,0,0,141,142,3,18,9,0,142,143,5,10,0,0,143,144,
        5,16,0,0,144,145,3,22,11,0,145,146,5,17,0,0,146,17,1,0,0,0,147,148,
        6,9,-1,0,148,151,5,29,0,0,149,151,1,0,0,0,150,147,1,0,0,0,150,149,
        1,0,0,0,151,157,1,0,0,0,152,153,10,3,0,0,153,154,5,18,0,0,154,156,
        3,18,9,4,155,152,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,
        1,0,0,0,158,19,1,0,0,0,159,157,1,0,0,0,160,161,6,10,-1,0,161,164,
        3,2,1,0,162,164,1,0,0,0,163,160,1,0,0,0,163,162,1,0,0,0,164,170,
        1,0,0,0,165,166,10,3,0,0,166,167,5,18,0,0,167,169,3,20,10,4,168,
        165,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,
        21,1,0,0,0,172,170,1,0,0,0,173,174,6,11,-1,0,174,175,3,2,1,0,175,
        176,5,19,0,0,176,181,1,0,0,0,177,178,10,2,0,0,178,180,3,22,11,3,
        179,177,1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,
        182,23,1,0,0,0,183,181,1,0,0,0,184,185,6,12,-1,0,185,186,5,9,0,0,
        186,187,3,24,12,0,187,188,5,10,0,0,188,203,1,0,0,0,189,190,5,31,
        0,0,190,203,3,24,12,10,191,203,5,21,0,0,192,203,5,23,0,0,193,203,
        5,24,0,0,194,203,5,26,0,0,195,203,5,22,0,0,196,203,3,10,5,0,197,
        198,5,29,0,0,198,199,5,9,0,0,199,200,3,20,10,0,200,201,5,10,0,0,
        201,203,1,0,0,0,202,184,1,0,0,0,202,189,1,0,0,0,202,191,1,0,0,0,
        202,192,1,0,0,0,202,193,1,0,0,0,202,194,1,0,0,0,202,195,1,0,0,0,
        202,196,1,0,0,0,202,197,1,0,0,0,203,212,1,0,0,0,204,205,10,9,0,0,
        205,206,7,3,0,0,206,211,3,24,12,10,207,208,10,8,0,0,208,209,7,4,
        0,0,209,211,3,24,12,9,210,204,1,0,0,0,210,207,1,0,0,0,211,214,1,
        0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,25,1,0,0,0,214,212,1,0,
        0,0,23,30,32,39,47,51,58,65,72,80,90,98,107,124,131,136,150,157,
        163,170,181,202,210,212
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "'public'", "'='", "'['", 
                     "']'", "'!'", "'if'", "'while'", "'('", "')'", "'&&'", 
                     "'||'", "'=='", "'!='", "'def'", "'{'", "'}'", "','", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'null'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SEMI", "NL", 
                      "NUM", "FLOAT", "BOOL", "StringLiteral", "UnterminatedStringLiteral", 
                      "NULL", "BlockComment", "Comment", "VARNAME", "ADD", 
                      "SUB", "MUL", "DIV", "MOD" ]

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
    SEMI=19
    NL=20
    NUM=21
    FLOAT=22
    BOOL=23
    StringLiteral=24
    UnterminatedStringLiteral=25
    NULL=26
    BlockComment=27
    Comment=28
    VARNAME=29
    ADD=30
    SUB=31
    MUL=32
    DIV=33
    MOD=34

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




    def prog(self):

        localctx = GrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 30
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 26
                        self.statement()
                        self.state = 27
                        self.match(GrammarParser.SEMI)
                        pass

                    elif la_ == 2:
                        self.state = 29
                        self.bracket_statement()
                        pass

             
                self.state = 34
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


        def imp(self):
            return self.getTypedRuleContext(GrammarParser.ImpContext,0)


        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.VARNAME)
            else:
                return self.getToken(GrammarParser.VARNAME, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_statement




    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 35
                    self.match(GrammarParser.VARNAME)
                    self.state = 36
                    self.matchWildcard() 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 47
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

            elif la_ == 4:
                self.state = 45
                self.conditional_statement()
                pass

            elif la_ == 5:
                self.state = 46
                self.imp()
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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8]:
                self.state = 49
                self.conditional_statement()
                pass
            elif token in [2, 15]:
                self.state = 50
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
            self.state = 53
            self.match(GrammarParser.T__0)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 54
                    self.match(GrammarParser.VARNAME)
                    self.state = 55
                    self.matchWildcard() 
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 61
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
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.SingleVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 63
                    self.match(GrammarParser.T__1)
                    pass
                elif token in [29]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 67
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 68
                self.match(GrammarParser.T__2)
                self.state = 69
                localctx.exp = self.statement()
                pass

            elif la_ == 2:
                localctx = GrammarParser.MultiVarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 70
                    self.match(GrammarParser.T__1)
                    pass

                elif la_ == 2:
                    pass


                self.state = 74
                localctx.name = self.varname_list(0)
                self.state = 75
                self.match(GrammarParser.T__2)
                self.state = 76
                localctx.vals = self.varname_list(0)
                pass

            elif la_ == 3:
                localctx = GrammarParser.ListVarContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 78
                    self.match(GrammarParser.T__1)
                    pass
                elif token in [29]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 82
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 83
                self.match(GrammarParser.T__2)
                self.state = 84
                self.match(GrammarParser.T__3)
                self.state = 85
                localctx.vals = self.var_list(0)
                self.state = 86
                self.match(GrammarParser.T__4)
                pass

            elif la_ == 4:
                localctx = GrammarParser.ListSetContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 88
                    self.match(GrammarParser.T__1)
                    pass
                elif token in [29]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 92
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 93
                self.match(GrammarParser.T__3)
                self.state = 94
                localctx.index = self.match(GrammarParser.NUM)
                self.state = 95
                self.match(GrammarParser.T__4)
                self.state = 96
                self.match(GrammarParser.T__2)
                self.state = 97
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
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.InvertVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                localctx.inv = self.match(GrammarParser.T__5)
                self.state = 101
                localctx.name = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 2:
                localctx = GrammarParser.VarNameContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                localctx.name = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 3:
                localctx = GrammarParser.ListGetContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 104
                self.match(GrammarParser.T__3)
                self.state = 105
                localctx.index = self.match(GrammarParser.NUM)
                self.state = 106
                self.match(GrammarParser.T__4)
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
            self.state = 109
            localctx.label = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                localctx.label = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 110
            self.match(GrammarParser.T__8)
            self.state = 111
            localctx.t = self.truth(0)
            self.state = 112
            self.match(GrammarParser.T__9)
            self.state = 113
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
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.ParenTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 116
                self.match(GrammarParser.T__8)
                self.state = 117
                localctx.t = self.truth(0)
                self.state = 118
                self.match(GrammarParser.T__9)
                pass

            elif la_ == 2:
                localctx = GrammarParser.AtomTruthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                localctx.lhs = self.statement()
                self.state = 121
                localctx.operand = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    localctx.operand = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 122
                localctx.rhs = self.statement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.LogicTruthContext(self, GrammarParser.TruthContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_truth)
                    self.state = 126
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 127
                    localctx.logic = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==11 or _la==12):
                        localctx.logic = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 128
                    localctx.rhs = self.truth(3) 
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 134
                self.match(GrammarParser.T__1)
                pass
            elif token in [15]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 138
            self.match(GrammarParser.T__14)
            self.state = 139
            localctx.name = self.match(GrammarParser.VARNAME)
            self.state = 140
            self.match(GrammarParser.T__8)
            self.state = 141
            localctx.args = self.varname_list(0)
            self.state = 142
            self.match(GrammarParser.T__9)
            self.state = 143
            self.match(GrammarParser.T__15)
            self.state = 144
            localctx.stmts = self.brackets(0)
            self.state = 145
            self.match(GrammarParser.T__16)
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
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomVarnameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 148
                localctx.atom = self.match(GrammarParser.VARNAME)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NullVarnameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CommaVarnameContext(self, GrammarParser.Varname_listContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_varname_list)
                    self.state = 152
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 153
                    self.match(GrammarParser.T__17)
                    self.state = 154
                    localctx.rhs = self.varname_list(4) 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.AtomVarlistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 161
                localctx.atom = self.statement()
                pass

            elif la_ == 2:
                localctx = GrammarParser.NullVarlistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.CommaVarlistContext(self, GrammarParser.Var_listContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_var_list)
                    self.state = 165
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 166
                    self.match(GrammarParser.T__17)
                    self.state = 167
                    localctx.rhs = self.var_list(4) 
                self.state = 172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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

            self.state = 174
            localctx.atom = self.statement()
            self.state = 175
            self.match(GrammarParser.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.SemiBracketsContext(self, GrammarParser.BracketsContext(self, _parentctx, _parentState))
                    localctx.lhs = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_brackets)
                    self.state = 177
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 178
                    localctx.rhs = self.brackets(3) 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 185
                self.match(GrammarParser.T__8)
                self.state = 186
                localctx.exp = self.expr(0)
                self.state = 187
                self.match(GrammarParser.T__9)
                pass

            elif la_ == 2:
                localctx = GrammarParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 189
                self.match(GrammarParser.SUB)
                self.state = 190
                localctx.exp = self.expr(10)
                pass

            elif la_ == 3:
                localctx = GrammarParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 191
                localctx.atom = self.match(GrammarParser.NUM)
                pass

            elif la_ == 4:
                localctx = GrammarParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 192
                localctx.atom = self.match(GrammarParser.BOOL)
                pass

            elif la_ == 5:
                localctx = GrammarParser.StrExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 193
                localctx.atom = self.match(GrammarParser.StringLiteral)
                pass

            elif la_ == 6:
                localctx = GrammarParser.NullExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 194
                localctx.atom = self.match(GrammarParser.NULL)
                pass

            elif la_ == 7:
                localctx = GrammarParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 195
                localctx.atom = self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 8:
                localctx = GrammarParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 196
                localctx.atom = self.var()
                pass

            elif la_ == 9:
                localctx = GrammarParser.Function_callContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 197
                localctx.name = self.match(GrammarParser.VARNAME)
                self.state = 198
                self.match(GrammarParser.T__8)
                self.state = 199
                localctx.args = self.var_list(0)
                self.state = 200
                self.match(GrammarParser.T__9)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 210
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.OpExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 204
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 205
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 206
                        localctx.rhs = self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.OpExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 207
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 208
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 20401094656) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 209
                        localctx.rhs = self.expr(9)
                        pass

             
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
         




