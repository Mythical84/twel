# Generated from c:/Users/tartinger2025/Documents/Mythic Script/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#prog.
    def enterProg(self, ctx:GrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by GrammarParser#prog.
    def exitProg(self, ctx:GrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by GrammarParser#parensOp.
    def enterParensOp(self, ctx:GrammarParser.ParensOpContext):
        pass

    # Exit a parse tree produced by GrammarParser#parensOp.
    def exitParensOp(self, ctx:GrammarParser.ParensOpContext):
        pass


    # Enter a parse tree produced by GrammarParser#mulOp.
    def enterMulOp(self, ctx:GrammarParser.MulOpContext):
        pass

    # Exit a parse tree produced by GrammarParser#mulOp.
    def exitMulOp(self, ctx:GrammarParser.MulOpContext):
        pass


    # Enter a parse tree produced by GrammarParser#addOp.
    def enterAddOp(self, ctx:GrammarParser.AddOpContext):
        pass

    # Exit a parse tree produced by GrammarParser#addOp.
    def exitAddOp(self, ctx:GrammarParser.AddOpContext):
        pass


    # Enter a parse tree produced by GrammarParser#negOp.
    def enterNegOp(self, ctx:GrammarParser.NegOpContext):
        pass

    # Exit a parse tree produced by GrammarParser#negOp.
    def exitNegOp(self, ctx:GrammarParser.NegOpContext):
        pass


    # Enter a parse tree produced by GrammarParser#atomOp.
    def enterAtomOp(self, ctx:GrammarParser.AtomOpContext):
        pass

    # Exit a parse tree produced by GrammarParser#atomOp.
    def exitAtomOp(self, ctx:GrammarParser.AtomOpContext):
        pass



del GrammarParser