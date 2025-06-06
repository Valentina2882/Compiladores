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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7")
        buf.write("\5(\n\5\f\5\16\5+\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2\66\2\17\3\2\2")
        buf.write("\2\4\27\3\2\2\2\6\31\3\2\2\2\b\35\3\2\2\2\n.\3\2\2\2\f")
        buf.write("\64\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20\21\3\2\2\2")
        buf.write("\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\30\5\6\4")
        buf.write("\2\24\30\5\b\5\2\25\30\5\n\6\2\26\30\5\f\7\2\27\23\3\2")
        buf.write("\2\2\27\24\3\2\2\2\27\25\3\2\2\2\27\26\3\2\2\2\30\5\3")
        buf.write("\2\2\2\31\32\7\3\2\2\32\33\7\13\2\2\33\34\7\17\2\2\34")
        buf.write("\7\3\2\2\2\35\36\7\4\2\2\36\37\7\7\2\2\37 \7\13\2\2 !")
        buf.write("\7\n\2\2!)\7\f\2\2\"#\7\t\2\2#$\7\7\2\2$%\7\13\2\2%&\7")
        buf.write("\n\2\2&(\7\f\2\2\'\"\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3")
        buf.write("\2\2\2*,\3\2\2\2+)\3\2\2\2,-\7\17\2\2-\t\3\2\2\2./\7\5")
        buf.write("\2\2/\60\7\b\2\2\60\61\7\7\2\2\61\62\7\13\2\2\62\63\7")
        buf.write("\17\2\2\63\13\3\2\2\2\64\65\7\6\2\2\65\66\7\17\2\2\66")
        buf.write("\r\3\2\2\2\5\21\27)")
        return buf.getvalue()


class CSVFilterParser ( Parser ):

    grammarFileName = "CSVFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "'filter'", "'aggregate'", "'print'", 
                     "'column'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "LOAD", "FILTER", "AGGREGATE", "PRINT", 
                      "COLUMN", "AGG_FUNC", "LOGIC_OP", "OPERATOR", "STRING", 
                      "NUMBER", "COMMENT", "WS", "SEMI" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_loadStat = 2
    RULE_filterStat = 3
    RULE_aggregateStat = 4
    RULE_printStat = 5

    ruleNames =  [ "prog", "stat", "loadStat", "filterStat", "aggregateStat", 
                   "printStat" ]

    EOF = Token.EOF
    LOAD=1
    FILTER=2
    AGGREGATE=3
    PRINT=4
    COLUMN=5
    AGG_FUNC=6
    LOGIC_OP=7
    OPERATOR=8
    STRING=9
    NUMBER=10
    COMMENT=11
    WS=12
    SEMI=13

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
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stat()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSVFilterParser.LOAD) | (1 << CSVFilterParser.FILTER) | (1 << CSVFilterParser.AGGREGATE) | (1 << CSVFilterParser.PRINT))) != 0)):
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
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSVFilterParser.LOAD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.loadStat()
                pass
            elif token in [CSVFilterParser.FILTER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.filterStat()
                pass
            elif token in [CSVFilterParser.AGGREGATE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.aggregateStat()
                pass
            elif token in [CSVFilterParser.PRINT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 20
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

        def LOAD(self):
            return self.getToken(CSVFilterParser.LOAD, 0)

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def SEMI(self):
            return self.getToken(CSVFilterParser.SEMI, 0)

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
            self.state = 23
            self.match(CSVFilterParser.LOAD)
            self.state = 24
            self.match(CSVFilterParser.STRING)
            self.state = 25
            self.match(CSVFilterParser.SEMI)
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

        def FILTER(self):
            return self.getToken(CSVFilterParser.FILTER, 0)

        def COLUMN(self, i:int=None):
            if i is None:
                return self.getTokens(CSVFilterParser.COLUMN)
            else:
                return self.getToken(CSVFilterParser.COLUMN, i)

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

        def SEMI(self):
            return self.getToken(CSVFilterParser.SEMI, 0)

        def LOGIC_OP(self, i:int=None):
            if i is None:
                return self.getTokens(CSVFilterParser.LOGIC_OP)
            else:
                return self.getToken(CSVFilterParser.LOGIC_OP, i)

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
            self.state = 27
            self.match(CSVFilterParser.FILTER)
            self.state = 28
            self.match(CSVFilterParser.COLUMN)
            self.state = 29
            self.match(CSVFilterParser.STRING)
            self.state = 30
            self.match(CSVFilterParser.OPERATOR)
            self.state = 31
            self.match(CSVFilterParser.NUMBER)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSVFilterParser.LOGIC_OP:
                self.state = 32
                self.match(CSVFilterParser.LOGIC_OP)
                self.state = 33
                self.match(CSVFilterParser.COLUMN)
                self.state = 34
                self.match(CSVFilterParser.STRING)
                self.state = 35
                self.match(CSVFilterParser.OPERATOR)
                self.state = 36
                self.match(CSVFilterParser.NUMBER)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(CSVFilterParser.SEMI)
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

        def AGGREGATE(self):
            return self.getToken(CSVFilterParser.AGGREGATE, 0)

        def AGG_FUNC(self):
            return self.getToken(CSVFilterParser.AGG_FUNC, 0)

        def COLUMN(self):
            return self.getToken(CSVFilterParser.COLUMN, 0)

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def SEMI(self):
            return self.getToken(CSVFilterParser.SEMI, 0)

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
        self.enterRule(localctx, 8, self.RULE_aggregateStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(CSVFilterParser.AGGREGATE)
            self.state = 45
            self.match(CSVFilterParser.AGG_FUNC)
            self.state = 46
            self.match(CSVFilterParser.COLUMN)
            self.state = 47
            self.match(CSVFilterParser.STRING)
            self.state = 48
            self.match(CSVFilterParser.SEMI)
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

        def PRINT(self):
            return self.getToken(CSVFilterParser.PRINT, 0)

        def SEMI(self):
            return self.getToken(CSVFilterParser.SEMI, 0)

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
        self.enterRule(localctx, 10, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(CSVFilterParser.PRINT)
            self.state = 51
            self.match(CSVFilterParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





