import os
from antlr4 import *
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor

def obtener_scripts_en_orden(carpeta):
    archivos = [f for f in os.listdir(carpeta) if f.endswith(".dsl")]
    # Ordenar extraído el número del nombre
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
    stream = CommonTokenStream(lexer)
    parser = CSVFilterParser(stream)
    tree = parser.prog()
    visitor = MyCSVVisitor()
    visitor.visit(tree)

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
