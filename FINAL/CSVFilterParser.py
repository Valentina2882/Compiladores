# Generated from CSVFilter.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("?\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\3\3\3\3\5\3\32")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\7\5*\n\5\f\5\16\5-\13\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\2\2\t\2\4")
        buf.write("\6\b\n\f\16\2\3\3\2\7\b\2<\2\21\3\2\2\2\4\31\3\2\2\2\6")
        buf.write("\33\3\2\2\2\b\37\3\2\2\2\n\60\3\2\2\2\f\65\3\2\2\2\16")
        buf.write(";\3\2\2\2\20\22\5\4\3\2\21\20\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2\2\25\32\5\6\4\2\26")
        buf.write("\32\5\b\5\2\27\32\5\f\7\2\30\32\5\16\b\2\31\25\3\2\2\2")
        buf.write("\31\26\3\2\2\2\31\27\3\2\2\2\31\30\3\2\2\2\32\5\3\2\2")
        buf.write("\2\33\34\7\3\2\2\34\35\7\r\2\2\35\36\7\4\2\2\36\7\3\2")
        buf.write("\2\2\37 \7\5\2\2 !\7\6\2\2!\"\7\r\2\2\"#\7\f\2\2#+\7\16")
        buf.write("\2\2$%\t\2\2\2%&\7\6\2\2&\'\7\r\2\2\'(\7\f\2\2(*\7\16")
        buf.write("\2\2)$\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,.\3\2\2\2")
        buf.write("-+\3\2\2\2./\7\4\2\2/\t\3\2\2\2\60\61\7\6\2\2\61\62\7")
        buf.write("\r\2\2\62\63\7\f\2\2\63\64\7\16\2\2\64\13\3\2\2\2\65\66")
        buf.write("\7\t\2\2\66\67\7\13\2\2\678\7\6\2\289\7\r\2\29:\7\4\2")
        buf.write("\2:\r\3\2\2\2;<\7\n\2\2<=\7\4\2\2=\17\3\2\2\2\5\23\31")
        buf.write("+")
        return buf.getvalue()


class CSVFilterParser ( Parser ):

    grammarFileName = "CSVFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'column'", 
                     "'and'", "'or'", "'aggregate'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "AGG_FUNC", "OPERATOR", "STRING", "NUMBER", 
                      "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_loadStat = 2
    RULE_filterStat = 3
    RULE_condition = 4
    RULE_aggregateStat = 5
    RULE_printStat = 6

    ruleNames =  [ "prog", "stat", "loadStat", "filterStat", "condition", 
                   "aggregateStat", "printStat" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    AGG_FUNC=9
    OPERATOR=10
    STRING=11
    NUMBER=12
    COMMENT=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVFilterParser.StatContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.StatContext,i)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CSVFilterParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.stat()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSVFilterParser.T__0) | (1 << CSVFilterParser.T__2) | (1 << CSVFilterParser.T__6) | (1 << CSVFilterParser.T__7))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStat(self):
            return self.getTypedRuleContext(CSVFilterParser.LoadStatContext,0)


        def filterStat(self):
            return self.getTypedRuleContext(CSVFilterParser.FilterStatContext,0)


        def aggregateStat(self):
            return self.getTypedRuleContext(CSVFilterParser.AggregateStatContext,0)


        def printStat(self):
            return self.getTypedRuleContext(CSVFilterParser.PrintStatContext,0)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = CSVFilterParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSVFilterParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.loadStat()
                pass
            elif token in [CSVFilterParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.filterStat()
                pass
            elif token in [CSVFilterParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.aggregateStat()
                pass
            elif token in [CSVFilterParser.T__7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 22
                self.printStat()
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


    class LoadStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_loadStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStat" ):
                listener.enterLoadStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStat" ):
                listener.exitLoadStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStat" ):
                return visitor.visitLoadStat(self)
            else:
                return visitor.visitChildren(self)




    def loadStat(self):

        localctx = CSVFilterParser.LoadStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(CSVFilterParser.T__0)
            self.state = 26
            self.match(CSVFilterParser.STRING)
            self.state = 27
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(CSVFilterParser.STRING)
            else:
                return self.getToken(CSVFilterParser.STRING, i)

        def OPERATOR(self, i:int=None):
            if i is None:
                return self.getTokens(CSVFilterParser.OPERATOR)
            else:
                return self.getToken(CSVFilterParser.OPERATOR, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(CSVFilterParser.NUMBER)
            else:
                return self.getToken(CSVFilterParser.NUMBER, i)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_filterStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStat" ):
                listener.enterFilterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStat" ):
                listener.exitFilterStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterStat" ):
                return visitor.visitFilterStat(self)
            else:
                return visitor.visitChildren(self)




    def filterStat(self):

        localctx = CSVFilterParser.FilterStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(CSVFilterParser.T__2)
            self.state = 30
            self.match(CSVFilterParser.T__3)
            self.state = 31
            self.match(CSVFilterParser.STRING)
            self.state = 32
            self.match(CSVFilterParser.OPERATOR)
            self.state = 33
            self.match(CSVFilterParser.NUMBER)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSVFilterParser.T__4 or _la==CSVFilterParser.T__5:
                self.state = 34
                _la = self._input.LA(1)
                if not(_la==CSVFilterParser.T__4 or _la==CSVFilterParser.T__5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 35
                self.match(CSVFilterParser.T__3)
                self.state = 36
                self.match(CSVFilterParser.STRING)
                self.state = 37
                self.match(CSVFilterParser.OPERATOR)
                self.state = 38
                self.match(CSVFilterParser.NUMBER)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def OPERATOR(self):
            return self.getToken(CSVFilterParser.OPERATOR, 0)

        def NUMBER(self):
            return self.getToken(CSVFilterParser.NUMBER, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = CSVFilterParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(CSVFilterParser.T__3)
            self.state = 47
            self.match(CSVFilterParser.STRING)
            self.state = 48
            self.match(CSVFilterParser.OPERATOR)
            self.state = 49
            self.match(CSVFilterParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGG_FUNC(self):
            return self.getToken(CSVFilterParser.AGG_FUNC, 0)

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_aggregateStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateStat" ):
                listener.enterAggregateStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateStat" ):
                listener.exitAggregateStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateStat" ):
                return visitor.visitAggregateStat(self)
            else:
                return visitor.visitChildren(self)




    def aggregateStat(self):

        localctx = CSVFilterParser.AggregateStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_aggregateStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(CSVFilterParser.T__6)
            self.state = 52
            self.match(CSVFilterParser.AGG_FUNC)
            self.state = 53
            self.match(CSVFilterParser.T__3)
            self.state = 54
            self.match(CSVFilterParser.STRING)
            self.state = 55
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVFilterParser.RULE_printStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)




    def printStat(self):

        localctx = CSVFilterParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(CSVFilterParser.T__7)
            self.state = 58
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





