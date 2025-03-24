# Generated from MiGramatica.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiGramaticaParser import MiGramaticaParser
else:
    from MiGramaticaParser import MiGramaticaParser

# This class defines a complete generic visitor for a parse tree produced by MiGramaticaParser.

class MiGramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiGramaticaParser#programa.
    def visitPrograma(self, ctx:MiGramaticaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#ForLoop.
    def visitForLoop(self, ctx:MiGramaticaParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#ForInitAssign.
    def visitForInitAssign(self, ctx:MiGramaticaParser.ForInitAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#ForInitEmpty.
    def visitForInitEmpty(self, ctx:MiGramaticaParser.ForInitEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#CondicionExpresion.
    def visitCondicionExpresion(self, ctx:MiGramaticaParser.CondicionExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#ForUpdateExpresion.
    def visitForUpdateExpresion(self, ctx:MiGramaticaParser.ForUpdateExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#ForUpdateEmpty.
    def visitForUpdateEmpty(self, ctx:MiGramaticaParser.ForUpdateEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#Assign.
    def visitAssign(self, ctx:MiGramaticaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#Comparacion.
    def visitComparacion(self, ctx:MiGramaticaParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#Variable.
    def visitVariable(self, ctx:MiGramaticaParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#MulDiv.
    def visitMulDiv(self, ctx:MiGramaticaParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#AddSub.
    def visitAddSub(self, ctx:MiGramaticaParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#Parens.
    def visitParens(self, ctx:MiGramaticaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#Decremento.
    def visitDecremento(self, ctx:MiGramaticaParser.DecrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#Incremento.
    def visitIncremento(self, ctx:MiGramaticaParser.IncrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#Int.
    def visitInt(self, ctx:MiGramaticaParser.IntContext):
        return self.visitChildren(ctx)



del MiGramaticaParser