# Compiladores

1,2,3. Gramatica que se ultilizó
grammar MiGramatica;

// Regla principal: permite múltiples sentencias terminadas en ';'
programa: (sentencia ';')+ EOF ;

// Sentencias permitidas
sentencia
    : whileStmt   
    | asignacion  
    ;

// Regla para `while`
whileStmt
    : 'while' '(' condicion ')' '{' (sentencia ';')* '}' # WhileLoop
    ;

// Condiciones dentro de `while`
condicion
    : ID op=('>' | '<' | '==' | '!=') expresion  # CondicionSimple
    ;

// Asignaciones con `;`
asignacion
    : ID '=' expresion # Assign
    ;

// Expresiones matemáticas con prioridad de operadores
expresion
    : expresion op=('*'|'/') expresion     # MulDiv
    | expresion op=('+'|'-') expresion     # AddSub
    | INT                                  # Int
    | ID                                   # Variable
    | '(' expresion ')'                    # Parens
    ;

// Reglas léxicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT : [0-9]+ ;                   // Números enteros
WS  : [ \t\r\n]+ -> skip ;       // Ignorar espacios en blanco

Expresion regular:
x = 0;
while (x < 5) {
    x = x + 1;
}

echo "x=0; while (x < 5) { x = x + 1; };" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica programa -tokens

Resultado:
[@0,0:0='x',<ID>,1:0]
[@1,1:1='=',<'='>,1:1]
[@2,2:2='0',<INT>,1:2]
[@3,3:3=';',<';'>,1:3]
[@4,5:9='while',<'while'>,1:5]
[@5,11:11='(',<'('>,1:11]
[@6,12:12='x',<ID>,1:12]
[@7,14:14='<',<'<'>,1:14]
[@8,16:16='5',<INT>,1:16]
[@9,17:17=')',<')'>,1:17]
[@10,19:19='{',<'{'>,1:19]
[@11,21:21='x',<ID>,1:21]
[@12,23:23='=',<'='>,1:23]
[@13,25:25='x',<ID>,1:25]
[@14,27:27='+',<'+'>,1:27]
[@15,29:29='1',<INT>,1:29]
[@16,30:30=';',<';'>,1:30]
[@17,32:32='}',<'}'>,1:32]
[@18,33:33=';',<';'>,1:33]
[@19,35:34='<EOF>',<EOF>,2:0]

4. echo "x=0; while (x < 5) { x = x + 1; };" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica programa -tree

(programa (sentencia (asignacion x = (expresion 0))) ; (sentencia (whileStmt while ( (condicion x < (expresion 5)) ) { (sentencia (asignacion x = (expresion (expresion x) + (expresion 1)))) ; })) ; <EOF>)

Preguntas:

1. La opcion (a) es la correcta porque estamos usando gramatica para una expresion regular para while.

2. La opcion (c) es correcta porque en el arbol de análisis sintactico, while es el nodo principal y tiene dos hijos: la condicion y el cuerpo del bucle.

3. a) Se ejecuta solo la primera línea después de while, esto es porque ANTLR sigue el orden jerárquico del código fuente.

