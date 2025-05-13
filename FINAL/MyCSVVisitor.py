from CSVFilterParser import CSVFilterParser
from CSVFilterVisitor import CSVFilterVisitor
import pandas as pd

class MyCSVVisitor(CSVFilterVisitor):
    def __init__(self):
        self.df = None

    def visitProg(self, ctx: CSVFilterParser.ProgContext):
        print("🌳 Árbol sintáctico:")
        print(ctx.toStringTree(recog=ctx.parser))
        for stat in ctx.stat():
            self.visit(stat)
        return None

    def visitLoadStat(self, ctx: CSVFilterParser.LoadStatContext):
        archivo = ctx.STRING().getText().replace('"', '')
        try:
            self.df = pd.read_csv(archivo)
            print(f"\n📥 Cargando archivo: {archivo}")
        except Exception as e:
            print(f"❌ Error al cargar el archivo: {e}")
        return None

    def visitFilterStat(self, ctx):
        if self.df is None:
            print("⚠️ No hay archivo cargado.")
            return None

        # Extraer todas las condiciones
        condiciones = []
        for i in range(0, len(ctx.STRING())):
            columna = ctx.STRING(i).getText().replace('"', '')
            operador = ctx.OPERATOR(i).getText()
            valor = float(ctx.NUMBER(i).getText())

            if operador == '>':
                condicion = self.df[columna] > valor
            elif operador == '<':
                condicion = self.df[columna] < valor
            elif operador == '>=':
                condicion = self.df[columna] >= valor
            elif operador == '<=':
                condicion = self.df[columna] <= valor
            elif operador == '==':
                condicion = self.df[columna] == valor
            elif operador == '!=':
                condicion = self.df[columna] != valor
            else:
                print(f"❌ Operador no soportado: {operador}")
                return None

            condiciones.append(condicion)

        # Aplicar los operadores lógicos correctamente
        filtro_final = condiciones[0]
        logical_ops = [t.getText() for t in ctx.children if t.getText() in ('and', 'or')]

        for i, op in enumerate(logical_ops):
            if op == 'and':
                filtro_final = filtro_final & condiciones[i + 1]
            elif op == 'or':
                filtro_final = filtro_final | condiciones[i + 1]
            else:
                print(f"❌ Operador lógico desconocido: {op}")
                return None

        self.df = self.df[filtro_final]
        print(f"\n🧪 Filtro aplicado → {len(self.df)} filas")
        print("📄 Filas filtradas (máx. 10):")
        print(self.df.head(10).to_string(index=False))
        return None

    def visitAggregateStat(self, ctx: CSVFilterParser.AggregateStatContext):
        if self.df is None:
            print("⚠️ No hay archivo cargado.")
            return None

        operacion = ctx.getChild(1).getText()  # sum, count, average
        columna = ctx.STRING().getText().replace('"', '')

        if operacion == 'sum':
            resultado = self.df[columna].sum()
            print(f"🧮 Suma de '{columna}': {resultado}")
        elif operacion == 'count':
            resultado = self.df[columna].count()
            print(f"🔢 Conteo de '{columna}': {resultado}")
        elif operacion == 'average':
            resultado = self.df[columna].mean()
            print(f"📊 Promedio de '{columna}': {resultado}")
        else:
            print(f"❌ Operación no soportada: {operacion}")
            return None

        return None