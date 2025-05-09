from antlr4 import *
from JSONLexer import JSONLexer
from JSONParser import JSONParser
from JSONParserListener import JSONParserListener

class XMLEmitter(JSONParserListener):
    def __init__(self):
        self.xml_map = {}

    def getXML(self, ctx):
        return self.xml_map.get(ctx, '')

    def setXML(self, ctx, value):
        self.xml_map[ctx] = value

    def exitAtom(self, ctx):
        self.setXML(ctx, ctx.getText())

    def exitString(self, ctx):
        self.setXML(ctx, ctx.getText().strip('"'))

    def exitObjectValue(self, ctx):
        self.setXML(ctx, self.getXML(ctx.jsonObject()))

    def exitPair(self, ctx):
        tag = ctx.STRING().getText().strip('"')
        val = self.getXML(ctx.value())
        self.setXML(ctx, f"<{tag}>{val}</{tag}>\n")

    def exitAnObject(self, ctx):
        self.setXML(ctx, ''.join(self.getXML(p) for p in ctx.pair()))

    def exitEmptyObject(self, ctx):
        self.setXML(ctx, '')

    def exitArrayOfValues(self, ctx):
        body = ''.join(f"<element>{self.getXML(v)}</element>\n" for v in ctx.value())
        self.setXML(ctx, body)

    def exitEmptyArray(self, ctx):
        self.setXML(ctx, '')

    def exitJson(self, ctx):
        self.setXML(ctx, self.getXML(ctx.getChild(0)))