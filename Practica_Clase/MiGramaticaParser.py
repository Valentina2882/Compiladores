# Generated from MiGramatica.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\6\2\24\n\2\r\2\16\2\25\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3&\n\3\f")
        buf.write("\3\16\3)\13\3\3\3\3\3\3\4\3\4\5\4/\n\4\3\5\3\5\3\6\3\6")
        buf.write("\5\6\65\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\bF\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\7\bQ\n\b\f\b\16\bT\13\b\3\b\2\3\16\t\2\4\6")
        buf.write("\b\n\f\16\2\5\3\2\n\13\3\2\f\r\3\2\16\21\2Y\2\23\3\2\2")
        buf.write("\2\4\31\3\2\2\2\6.\3\2\2\2\b\60\3\2\2\2\n\64\3\2\2\2\f")
        buf.write("\66\3\2\2\2\16E\3\2\2\2\20\21\5\4\3\2\21\22\7\3\2\2\22")
        buf.write("\24\3\2\2\2\23\20\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2\2")
        buf.write("\25\26\3\2\2\2\26\27\3\2\2\2\27\30\7\2\2\3\30\3\3\2\2")
        buf.write("\2\31\32\7\4\2\2\32\33\7\5\2\2\33\34\5\6\4\2\34\35\7\3")
        buf.write("\2\2\35\36\5\b\5\2\36\37\7\3\2\2\37 \5\n\6\2 !\7\6\2\2")
        buf.write("!\'\7\7\2\2\"#\5\f\7\2#$\7\3\2\2$&\3\2\2\2%\"\3\2\2\2")
        buf.write("&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)\'\3\2\2\2")
        buf.write("*+\7\b\2\2+\5\3\2\2\2,/\5\f\7\2-/\3\2\2\2.,\3\2\2\2.-")
        buf.write("\3\2\2\2/\7\3\2\2\2\60\61\5\16\b\2\61\t\3\2\2\2\62\65")
        buf.write("\5\16\b\2\63\65\3\2\2\2\64\62\3\2\2\2\64\63\3\2\2\2\65")
        buf.write("\13\3\2\2\2\66\67\7\24\2\2\678\7\t\2\289\5\16\b\29\r\3")
        buf.write("\2\2\2:;\b\b\1\2;F\7\25\2\2<F\7\24\2\2=>\7\24\2\2>F\7")
        buf.write("\22\2\2?@\7\24\2\2@F\7\23\2\2AB\7\5\2\2BC\5\16\b\2CD\7")
        buf.write("\6\2\2DF\3\2\2\2E:\3\2\2\2E<\3\2\2\2E=\3\2\2\2E?\3\2\2")
        buf.write("\2EA\3\2\2\2FR\3\2\2\2GH\f\n\2\2HI\t\2\2\2IQ\5\16\b\13")
        buf.write("JK\f\t\2\2KL\t\3\2\2LQ\5\16\b\nMN\f\b\2\2NO\t\4\2\2OQ")
        buf.write("\5\16\b\tPG\3\2\2\2PJ\3\2\2\2PM\3\2\2\2QT\3\2\2\2RP\3")
        buf.write("\2\2\2RS\3\2\2\2S\17\3\2\2\2TR\3\2\2\2\t\25\'.\64EPR")
        return buf.getvalue()


class MiGramaticaParser ( Parser ):

    grammarFileName = "MiGramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'for'", "'('", "')'", "'{'", "'}'", 
                     "'='", "'*'", "'/'", "'+'", "'-'", "'<'", "'>'", "'=='", 
                     "'!='", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_forStmt = 1
    RULE_inicializacion = 2
    RULE_condicion = 3
    RULE_actualizacion = 4
    RULE_asignacion = 5
    RULE_expresion = 6

    ruleNames =  [ "programa", "forStmt", "inicializacion", "condicion", 
                   "actualizacion", "asignacion", "expresion" ]

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
    ID=18
    INT=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiGramaticaParser.EOF, 0)

        def forStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ForStmtContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ForStmtContext,i)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = MiGramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.forStmt()
                self.state = 15
                self.match(MiGramaticaParser.T__0)
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiGramaticaParser.T__1):
                    break

            self.state = 21
            self.match(MiGramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_forStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForLoopContext(ForStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ForStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def inicializacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.InicializacionContext,0)

        def condicion(self):
            return self.getTypedRuleContext(MiGramaticaParser.CondicionContext,0)

        def actualizacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ActualizacionContext,0)

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.AsignacionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)



    def forStmt(self):

        localctx = MiGramaticaParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            localctx = MiGramaticaParser.ForLoopContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(MiGramaticaParser.T__1)
            self.state = 24
            self.match(MiGramaticaParser.T__2)
            self.state = 25
            self.inicializacion()
            self.state = 26
            self.match(MiGramaticaParser.T__0)
            self.state = 27
            self.condicion()
            self.state = 28
            self.match(MiGramaticaParser.T__0)
            self.state = 29
            self.actualizacion()
            self.state = 30
            self.match(MiGramaticaParser.T__3)
            self.state = 31
            self.match(MiGramaticaParser.T__4)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiGramaticaParser.ID:
                self.state = 32
                self.asignacion()
                self.state = 33
                self.match(MiGramaticaParser.T__0)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(MiGramaticaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_inicializacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForInitEmptyContext(InicializacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.InicializacionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInitEmpty" ):
                listener.enterForInitEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInitEmpty" ):
                listener.exitForInitEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitEmpty" ):
                return visitor.visitForInitEmpty(self)
            else:
                return visitor.visitChildren(self)


    class ForInitAssignContext(InicializacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.InicializacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def asignacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.AsignacionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInitAssign" ):
                listener.enterForInitAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInitAssign" ):
                listener.exitForInitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitAssign" ):
                return visitor.visitForInitAssign(self)
            else:
                return visitor.visitChildren(self)



    def inicializacion(self):

        localctx = MiGramaticaParser.InicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_inicializacion)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiGramaticaParser.ID]:
                localctx = MiGramaticaParser.ForInitAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.asignacion()
                pass
            elif token in [MiGramaticaParser.T__0]:
                localctx = MiGramaticaParser.ForInitEmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)

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


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_condicion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondicionExpresionContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicionExpresion" ):
                listener.enterCondicionExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicionExpresion" ):
                listener.exitCondicionExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicionExpresion" ):
                return visitor.visitCondicionExpresion(self)
            else:
                return visitor.visitChildren(self)



    def condicion(self):

        localctx = MiGramaticaParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condicion)
        try:
            localctx = MiGramaticaParser.CondicionExpresionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActualizacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_actualizacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForUpdateEmptyContext(ActualizacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ActualizacionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdateEmpty" ):
                listener.enterForUpdateEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdateEmpty" ):
                listener.exitForUpdateEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdateEmpty" ):
                return visitor.visitForUpdateEmpty(self)
            else:
                return visitor.visitChildren(self)


    class ForUpdateExpresionContext(ActualizacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ActualizacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdateExpresion" ):
                listener.enterForUpdateExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdateExpresion" ):
                listener.exitForUpdateExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdateExpresion" ):
                return visitor.visitForUpdateExpresion(self)
            else:
                return visitor.visitChildren(self)



    def actualizacion(self):

        localctx = MiGramaticaParser.ActualizacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_actualizacion)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiGramaticaParser.T__2, MiGramaticaParser.ID, MiGramaticaParser.INT]:
                localctx = MiGramaticaParser.ForUpdateExpresionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.expresion(0)
                pass
            elif token in [MiGramaticaParser.T__3]:
                localctx = MiGramaticaParser.ForUpdateEmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)

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


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_asignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)
        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def asignacion(self):

        localctx = MiGramaticaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            localctx = MiGramaticaParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MiGramaticaParser.ID)
            self.state = 53
            self.match(MiGramaticaParser.T__6)
            self.state = 54
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ComparacionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class DecrementoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecremento" ):
                listener.enterDecremento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecremento" ):
                listener.exitDecremento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecremento" ):
                return visitor.visitDecremento(self)
            else:
                return visitor.visitChildren(self)


    class IncrementoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncremento" ):
                listener.enterIncremento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncremento" ):
                listener.exitIncremento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncremento" ):
                return visitor.visitIncremento(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiGramaticaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiGramaticaParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = MiGramaticaParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 57
                self.match(MiGramaticaParser.INT)
                pass

            elif la_ == 2:
                localctx = MiGramaticaParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(MiGramaticaParser.ID)
                pass

            elif la_ == 3:
                localctx = MiGramaticaParser.IncrementoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(MiGramaticaParser.ID)
                self.state = 60
                self.match(MiGramaticaParser.T__15)
                pass

            elif la_ == 4:
                localctx = MiGramaticaParser.DecrementoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(MiGramaticaParser.ID)
                self.state = 62
                self.match(MiGramaticaParser.T__16)
                pass

            elif la_ == 5:
                localctx = MiGramaticaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(MiGramaticaParser.T__2)
                self.state = 64
                self.expresion(0)
                self.state = 65
                self.match(MiGramaticaParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 78
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MiGramaticaParser.MulDivContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 69
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 70
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MiGramaticaParser.T__7 or _la==MiGramaticaParser.T__8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        self.expresion(9)
                        pass

                    elif la_ == 2:
                        localctx = MiGramaticaParser.AddSubContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 72
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 73
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MiGramaticaParser.T__9 or _la==MiGramaticaParser.T__10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        self.expresion(8)
                        pass

                    elif la_ == 3:
                        localctx = MiGramaticaParser.ComparacionContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 75
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 76
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiGramaticaParser.T__11) | (1 << MiGramaticaParser.T__12) | (1 << MiGramaticaParser.T__13) | (1 << MiGramaticaParser.T__14))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        self.expresion(7)
                        pass

             
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self._predicates[6] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




