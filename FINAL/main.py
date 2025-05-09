from antlr4 import *
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py archivo.dsl")
        return

    input_file = sys.argv[1]

    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = CSVFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVFilterParser(stream)

    tree = parser.prog()
    visitor = MyCSVVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    main()
