# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#prog.
    def visitProg(self, ctx:GrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#normalStatement.
    def visitNormalStatement(self, ctx:GrammarParser.NormalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#fileStatement.
    def visitFileStatement(self, ctx:GrammarParser.FileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#bracket_statement.
    def visitBracket_statement(self, ctx:GrammarParser.Bracket_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#imp.
    def visitImp(self, ctx:GrammarParser.ImpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#singleVar.
    def visitSingleVar(self, ctx:GrammarParser.SingleVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#multiVar.
    def visitMultiVar(self, ctx:GrammarParser.MultiVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#listVar.
    def visitListVar(self, ctx:GrammarParser.ListVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#listSet.
    def visitListSet(self, ctx:GrammarParser.ListSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#invertVar.
    def visitInvertVar(self, ctx:GrammarParser.InvertVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#varName.
    def visitVarName(self, ctx:GrammarParser.VarNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#listGet.
    def visitListGet(self, ctx:GrammarParser.ListGetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_loop.
    def visitFor_loop(self, ctx:GrammarParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#conditional_statement.
    def visitConditional_statement(self, ctx:GrammarParser.Conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#elseIf.
    def visitElseIf(self, ctx:GrammarParser.ElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#elseElif.
    def visitElseElif(self, ctx:GrammarParser.ElseElifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#atomElif.
    def visitAtomElif(self, ctx:GrammarParser.AtomElifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#else.
    def visitElse(self, ctx:GrammarParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parenTruth.
    def visitParenTruth(self, ctx:GrammarParser.ParenTruthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#atomTruth.
    def visitAtomTruth(self, ctx:GrammarParser.AtomTruthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#logicTruth.
    def visitLogicTruth(self, ctx:GrammarParser.LogicTruthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#dualTruth.
    def visitDualTruth(self, ctx:GrammarParser.DualTruthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_def.
    def visitFunction_def(self, ctx:GrammarParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#nullVarname.
    def visitNullVarname(self, ctx:GrammarParser.NullVarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#atomVarname.
    def visitAtomVarname(self, ctx:GrammarParser.AtomVarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#commaVarname.
    def visitCommaVarname(self, ctx:GrammarParser.CommaVarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#nullVarlist.
    def visitNullVarlist(self, ctx:GrammarParser.NullVarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#atomVarlist.
    def visitAtomVarlist(self, ctx:GrammarParser.AtomVarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#commaVarlist.
    def visitCommaVarlist(self, ctx:GrammarParser.CommaVarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#atomBracketStatement.
    def visitAtomBracketStatement(self, ctx:GrammarParser.AtomBracketStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#semiBrackets.
    def visitSemiBrackets(self, ctx:GrammarParser.SemiBracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#atomBrackets.
    def visitAtomBrackets(self, ctx:GrammarParser.AtomBracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#strExpr.
    def visitStrExpr(self, ctx:GrammarParser.StrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#floatExpr.
    def visitFloatExpr(self, ctx:GrammarParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#varExpr.
    def visitVarExpr(self, ctx:GrammarParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#intExpr.
    def visitIntExpr(self, ctx:GrammarParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#opExpr.
    def visitOpExpr(self, ctx:GrammarParser.OpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#nullExpr.
    def visitNullExpr(self, ctx:GrammarParser.NullExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_call.
    def visitFunction_call(self, ctx:GrammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#negExpr.
    def visitNegExpr(self, ctx:GrammarParser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parensExpr.
    def visitParensExpr(self, ctx:GrammarParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#boolExpr.
    def visitBoolExpr(self, ctx:GrammarParser.BoolExprContext):
        return self.visitChildren(ctx)



del GrammarParser