from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    def exitForLoop(self, ctx):
        print("🔄 Se detectó un bucle FOR")
    
    def exitInicializacion(self, ctx):
        print(f"⚙️ Inicialización detectada: {ctx.ID().getText()} = {ctx.expresion().getText()}")
    
    def exitCondicion(self, ctx):
        print(f"🔍 Condición detectada: {ctx.ID().getText()} {ctx.op.text} {ctx.INT().getText()}")
    
    def exitActualizacion(self, ctx):
        print(f"🔄 Actualización detectada: {ctx.ID().getText()} = {ctx.expresion().getText()}")
    
    def exitAssign(self, ctx):
        print(f"✍️ Asignación detectada: {ctx.getText()}")
