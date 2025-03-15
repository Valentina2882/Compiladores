# Compiladores

1,2,3. Gramatica que se ultilizó

grammar MiGramatica;

// Regla principal: permite múltiples sentencias terminadas en ';'
programa: (sentencia ';')+ EOF ;

// Sentencias permitidas
sentencia
    : forStmt    
    | asignacion  
    ;

// Regla para for
forStmt
    : 'for' '(' inicializacion ';' condicion ';' actualizacion ')' '{' (sentencia ';')* '}' # ForLoop
    ;

// Inicialización del for (Ej: i = 0)
inicializacion
    : ID '=' expresion 
    ;

// Condiciones dentro del for (Ej: i < 10)
condicion
    : ID op=('>' | '<' | '==' | '!=') INT  
    ;

// Actualización del for (Ej: i = i + 1)
actualizacion
    : ID '=' expresion 
    ;

// Asignaciones con ;
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
WS  : [ \t\r\n]+ -> skip ;       // Ignorar espacios en blanco

Expresion regular:
for (i = 0; i < 10; i = i + 1) {
    x = x + i;
}

java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica programa -tokens -tree < prueba.txt
Nota: utilizamos este comando para que nos compile, ya que del otro modo se nos bugueo, usted miró 

Resultado:
[@0,0:2='for',<'for'>,1:0]
[@1,4:4='(',<'('>,1:4]
[@2,5:5='i',<ID>,1:5]
[@3,7:7='=',<'='>,1:7]
[@4,9:9='0',<INT>,1:9]
[@5,10:10=';',<';'>,1:10]
[@6,12:12='i',<ID>,1:12]
[@7,14:14='<',<'<'>,1:14]
[@8,16:17='10',<INT>,1:16]
[@9,18:18=';',<';'>,1:18]
[@10,20:20='i',<ID>,1:20]
[@11,22:22='=',<'='>,1:22]
[@12,24:24='i',<ID>,1:24]
[@13,26:26='+',<'+'>,1:26]
[@14,28:28='1',<INT>,1:28]
[@15,29:29=')',<')'>,1:29]
[@16,31:31='{',<'{'>,1:31]
[@17,37:37='x',<ID>,2:4]
[@18,39:39='=',<'='>,2:6]
[@19,41:41='x',<ID>,2:8]
[@20,43:43='+',<'+'>,2:10]
[@21,45:45='i',<ID>,2:12]
[@22,46:46=';',<';'>,2:13]
[@23,48:48='}',<'}'>,3:0]
[@24,49:49=';',<';'>,3:1]
[@25,50:49='<EOF>',<EOF>,3:2]

(programa (sentencia (forStmt for ( (inicializacion i = (expresion 0)) ; (condicion i < 10) ; (actualizacion i = (expresion (expresion i) + (expresion 1))) ) { (sentencia (asignacion x = (expresion (expresion x) + (expresion i)))) ; })) ; <EOF>)

Preguntas:

1. La opcion (a) es la correcta porque representa con precisión los tokens generados por ANTLR para el for.

2. La opcion (a) es la correcta porque el nodo raiz es forStmt, y sus componentes principales (inicialización, condición, actualización y cuerpo) son sus nodos secundarios.

3. Si se omiten los ;, el analizador sintáctico no podrá identificar correctamente la estructura del for, lo que generará un error de sintaxis en la fase de parsing.