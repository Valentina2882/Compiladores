import os
from antlr4 import *
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor
from PIL import Image  # Para abrir la imagen automáticamente

class VisualizadorArbol:
    def __init__(self):
        from graphviz import Digraph
        self.dot = Digraph(comment="Árbol Sintáctico")
        self.nodo_id = 0

    def agregar_nodo(self, label):
        self.nodo_id += 1
        self.dot.node(str(self.nodo_id), label)
        return self.nodo_id

    def agregar_arista(self, desde, hacia):
        self.dot.edge(str(desde), str(hacia))

    def recorrer(self, tree, parent=None):
        label = type(tree).__name__
        if hasattr(tree, 'getText'):
            text = tree.getText()
            if text:
                label += f"\n{text}"
        nodo_actual = self.agregar_nodo(label)
        if parent is not None:
            self.agregar_arista(parent, nodo_actual)
        for i in range(tree.getChildCount()):
            self.recorrer(tree.getChild(i), nodo_actual)

    def exportar(self, nombre_archivo):
        self.dot.render(nombre_archivo, format='png', cleanup=True)

def obtener_scripts_en_orden(carpeta):
    archivos = [f for f in os.listdir(carpeta) if f.endswith(".dsl")]
    archivos.sort(key=lambda f: int(f.replace("script_", "").replace(".dsl", "")))
    return archivos

def mostrar_menu(scripts):
    print("\n📜 Scripts disponibles:")
    for idx, script in enumerate(scripts, 1):
        print(f"{idx}. {script}")
    print("0. Salir\n")

def ejecutar_script(path_completo):
    input_stream = FileStream(path_completo, encoding='utf-8')

    lexer = CSVFilterLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print(f"\n🔍 Tokens del script: {os.path.basename(path_completo)}\n")
    print("Tokens simbólicos disponibles:")
    print(CSVFilterLexer.symbolicNames)

    tokens = token_stream.tokens
    for token in tokens:
        if 0 < token.type < len(CSVFilterLexer.symbolicNames):
            nombre_token = CSVFilterLexer.symbolicNames[token.type]
            print(f"{token.text}\t→\t{nombre_token} (Línea {token.line}, Columna {token.column})")
        else:
            print(f"{token.text}\t→\tTipo desconocido ({token.type}) (Línea {token.line}, Columna {token.column})")

    token_stream.reset()

    parser = CSVFilterParser(token_stream)
    tree = parser.prog()

    visitor = MyCSVVisitor()
    visitor.visit(tree)

    # Visualizar el árbol
    visualizador = VisualizadorArbol()
    visualizador.recorrer(tree)
    nombre_base = os.path.splitext(os.path.basename(path_completo))[0]
    visualizador.exportar(f"arbol_{nombre_base}")

    # Abrir imagen automáticamente
    ruta_imagen = f"arbol_{nombre_base}.png"
    if os.path.exists(ruta_imagen):
        print(f"\n🌳 Árbol sintáctico generado: {ruta_imagen}")
        img = Image.open(ruta_imagen)
        img.show()
    else:
        print("❌ No se pudo encontrar la imagen del árbol sintáctico.")

def main():
    carpeta_scripts = "Scripts"
    while True:
        scripts = obtener_scripts_en_orden(carpeta_scripts)
        mostrar_menu(scripts)

        try:
            opcion = int(input("Selecciona el número del script a ejecutar: "))
        except ValueError:
            print("❌ Opción no válida.")
            continue

        if opcion == 0:
            print("👋 Saliendo...")
            break
        elif 1 <= opcion <= len(scripts):
            script_elegido = scripts[opcion - 1]
            ruta = os.path.join(carpeta_scripts, script_elegido)
            print(f"\n📄 Ejecutando: {ruta}\n")
            ejecutar_script(ruta)
            input("\n⏭️ Presiona Enter para continuar...")
        else:
            print("❌ Opción fuera de rango.")

if __name__ == "__main__":
    main()
