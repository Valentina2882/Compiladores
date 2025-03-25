from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    #se ejecuta al salir de un bucle FOR
    def exitForLoop(self, ctx):
        print("🔄 Se detectó un bucle FOR")
    
    #se ejecuta al salir de la inicialización de una variable en un FOR
    def exitInicializacion(self, ctx):
        print(f"⚙️ Inicialización detectada: {ctx.ID().getText()} = {ctx.expresion().getText()}")
    
    #se ejecuta al salir de la condición del FOR
    def exitCondicion(self, ctx):
        print(f"🔍 Condición detectada: {ctx.ID().getText()} {ctx.op.text} {ctx.INT().getText()}")
    
    #se ejecuta al salir de la actualización de la variable en el FOR
    def exitActualizacion(self, ctx):
        print(f"🔄 Actualización detectada: {ctx.ID().getText()} = {ctx.expresion().getText()}")
    
    #se ejecuta al salir de una asignación
    def exitAssign(self, ctx):
        print(f"✍️ Asignación detectada: {ctx.getText()}")