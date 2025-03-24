from MiGramaticaVisitor import MiGramaticaVisitor

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}

    def visitPrograma(self, ctx):
        for forStmt in ctx.forStmt():
            self.visit(forStmt)
        return self.variables

    def visitAssign(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.variables[var] = value
        print(f"📝 {var} = {value}")
        return value

    def visitInt(self, ctx):
        return int(ctx.getText())

    def visitVariable(self, ctx):
        var = ctx.getText()
        if var not in self.variables:
            print(f"⚠️ Variable '{var}' no está inicializada. Se asume 0.")
        return self.variables.get(var, 0)

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left / right

    def visitParens(self, ctx):
        return self.visit(ctx.expresion())

    def visitForLoop(self, ctx):
        if ctx.inicializacion():
            self.visit(ctx.inicializacion())
        
        while self.visit(ctx.condicion()):
            for asignacion in ctx.asignacion():
                self.visit(asignacion)
            
            if ctx.actualizacion():
                self.visit(ctx.actualizacion())

    def visitCondicionExpresion(self, ctx):
        return self.visit(ctx.expresion())

    def visitComparacion(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op.text

        if op == '>':
            return left > right
        elif op == '<':
            return left < right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right
        return False

    def visitIncremento(self, ctx):
        var = ctx.ID().getText()
        self.variables[var] = self.variables.get(var, 0) + 1
        return self.variables[var]

    def visitDecremento(self, ctx):
        var = ctx.ID().getText()
        self.variables[var] = self.variables.get(var, 0) - 1
        return self.variables[var]