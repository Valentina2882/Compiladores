import csv
from CSVFilterVisitor import CSVFilterVisitor

class MyCSVVisitor(CSVFilterVisitor):
    def __init__(self):
        self.data = []
        self.filters = []
        self.aggregates = []
        self.filename = ""

    def visitLoadStat(self, ctx):
        self.filename = ctx.STRING().getText().replace('"', '')
        with open(self.filename, newline='') as f:
            self.data = list(csv.DictReader(f))
        return None

    def visitFilterStat(self, ctx):
        column = ctx.STRING().getText().replace('"', '')
        op = ctx.OPERATOR().getText()
        value = float(ctx.NUMBER().getText())

        def filtro(row):
            try:
                return eval(f"{float(row[column])} {op} {value}")
            except:
                return False

        self.filters.append(filtro)
        return None

    def visitAggregateStat(self, ctx):
        func = ctx.AGG_FUNC().getText()
        column = ctx.STRING().getText().replace('"', '')
        self.aggregates.append((func, column))
        return None

    def visitPrintStat(self, ctx):
        # Aplicar filtros acumulados
        filtered_data = self.data
        for filtro in self.filters:
            filtered_data = list(filter(filtro, filtered_data))

        # Ejecutar agregaciones
        for func, column in self.aggregates:
            try:
                values = [float(row[column]) for row in filtered_data if row[column]]
            except ValueError:
                print(f"Error: columna {column} no es numérica.")
                continue

            if func == "count":
                print(f"Count of {column}: {len(values)}")
            elif func == "sum":
                print(f"Sum of {column}: {sum(values)}")
            elif func == "average":
                print(f"Average of {column}: {sum(values)/len(values) if values else 0}")

        # También puedes imprimir los datos si quieres
        # for row in filtered_data:
        #     print(row)

        # Limpiar para siguientes scripts
        self.filters = []
        self.aggregates = []
        return None

