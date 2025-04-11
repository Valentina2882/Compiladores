import sys
import json
from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser
from CSVListener import CSVListener
from collections import Counter
import re

class Loader(CSVListener):
    EMPTY = ""
    def __init__(self):
        self.rows = []
        self.header = []
        self.currentRowFieldValues = []
        self.emptyFieldCount = 0  

    def enterRow(self, ctx:CSVParser.RowContext):
        self.currentRowFieldValues = []

    def exitText(self, ctx:CSVParser.TextContext):
        self.currentRowFieldValues.append(ctx.getText())

    def exitString(self, ctx:CSVParser.StringContext):
        self.currentRowFieldValues.append(ctx.getText())

    def exitEmpty(self, ctx:CSVParser.EmptyContext):
        self.currentRowFieldValues.append(self.EMPTY)
        self.emptyFieldCount += 1  

    def exitHeader(self, ctx:CSVParser.HeaderContext):
        self.header = list(self.currentRowFieldValues)

    def exitRow(self, ctx:CSVParser.RowContext):
        # Evita procesar la fila si es parte del header
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
            return

        m = {}
        for i, val in enumerate(self.currentRowFieldValues):
            key = self.header[i] if i < len(self.header) else f"col_{i}"
            m[key] = val
        self.rows.append(m)

    def print_column_stats(self, column_name="Cantidad"):
        valores = [fila[column_name] for fila in self.rows if column_name in fila]
        print(f"\nEstadísticas para columna '{column_name}':")
        for valor in valores:
            print(f"• {valor}")

    def limpiar_montos(self):
        for fila in self.rows:
            if "Cantidad" in fila:
                fila["Cantidad"] = fila["Cantidad"].replace('"', '').replace('$','').replace(',', '')

    def exportar_a_json(self, filename="output.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.rows, f, indent=2, ensure_ascii=False)



    def contar_meses(self, columna="Mes"):
        meses = [fila[columna] for fila in self.rows if columna in fila]
        conteo = Counter(meses)
        return conteo 

    def detectar_filas_repetidas(self):
        fila_tuplas = [tuple(fila.items()) for fila in self.rows]
        conteo = Counter(fila_tuplas)
        
        repetidas = [dict(tupla) for tupla, cantidad in conteo.items() if cantidad > 1]
        
        if repetidas:
            print("\nFilas repetidas encontradas:")
            for fila in repetidas:
                print(fila)
        else:
            print("\nNo hay filas repetidas.")
    def detectar_campos_invalidos(self, columna="Cantidad"):
        print(f"\nDetectando valores vacíos o mal formateados en la columna '{columna}':")
        formato_valido = re.compile(r'^"?\$?\d+(,\d{3})*(\.\d{2})?"?$')  # acepta "$1,000.00", 1000, "950", etc.

        encontrados = False
        for i, fila in enumerate(self.rows, start=1):
            valor = fila.get(columna, "").strip()
            if valor == "" or not formato_valido.match(valor):
                print(f"Fila {i}: Valor inválido -> '{valor}'")
                encontrados = True

        if not encontrados:
            print("Todos los valores están correctamente formateados.")
    
    def sumar_montos_por_mes(self, columna_monto="Cantidad", columna_mes="Mes"):
        suma_por_mes = {}
        for fila in self.rows:
            mes = fila.get(columna_mes, "").strip()
            monto_raw = fila.get(columna_monto, "").replace('"', '').replace('$','').replace(',', '').strip()

            if mes and monto_raw.replace('.', '', 1).isdigit():
                monto = float(monto_raw)
                suma_por_mes[mes] = suma_por_mes.get(mes, 0) + monto

        print("\nSuma de montos por mes:")
        for mes, total in suma_por_mes.items():
            print(f"{mes}: {total}")
        return suma_por_mes

            



def main(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVParser(stream)
    tree = parser.csvFile()

    loader = Loader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)

    #for row in loader.rows:
     #   print(row)
    #print(f"Total de campos vacíos: {loader.emptyFieldCount}")
    #loader.print_column_stats("Cantidad")
    #loader.limpiar_montos()
    #loader.exportar_a_json("output.json")

    #conteo = loader.contar_meses()
    #print("Meses encontrados:")
    #for mes, cantidad in conteo.items():
    #    print(f"{mes}: {cantidad}")
    #loader.detectar_filas_repetidas()
    #loader.detectar_campos_invalidos("Cantidad")
    #loader.sumar_montos_por_mes()




if __name__ == '__main__':
    main(sys.argv)