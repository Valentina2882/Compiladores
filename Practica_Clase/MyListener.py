from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    def exitForLoop(self, ctx):
        print("🔄 Se detectó un bucle FOR")
        inicializacion = ctx.inicializacion().getText() if ctx.inicializacion() else "Sin inicialización"
        condicion = ctx.condicion().getText() if ctx.condicion() else "Sin condición"
        actualizacion = ctx.actualizacion().getText() if ctx.actualizacion() else "Sin actualización"
        
        print(f"   - Inicialización: {inicializacion}")
        print(f"   - Condición: {condicion}")
        print(f"   - Actualización: {actualizacion}")

    def exitAssign(self, ctx):
        print("✍️ Asignación detectada:", ctx.getText())