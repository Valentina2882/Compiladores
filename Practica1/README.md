# Compiladores

1,2,3. Gramatica que se ultilizó
grammar MiGramatica;

// Regla principal: una secuencia de expresiones separadas por punto y coma.
programa: (expresion ';')+ ;

// Reglas de expresiones con prioridades para operaciones aritméticas.
expresion
    : ID '=' expresion                   # Assign   // Asignación de variables
    | expresion op=('*'|'/') expresion   # MulDiv    // Multiplicación y división
    | expresion op=('+'|'-') expresion   # AddSub    // Suma y resta
    | '(' expresion ')'                  # Parens   // Expresión entre paréntesis
    | ID                                  # Variable // Uso de variables
    | INT                                 # Int      // Entero
    ;

// Reglas léxicas:
// Identificador: inicia con letra o guión bajo, seguido de letras, dígitos o guiones bajos.
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;

// Número entero: secuencia de dígitos.
INT : [0-9]+ ;

// Espacios en blanco: se omiten (skip).
WS  : [ \t\r\n]+ -> skip ;

Expresion regular:
a = 10;
b = 5 + a * 2;
c = (b - 3) / 2;

echo "a=10; b = 5 + a * 2; c = (b - 3) / 2;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica programa -tokens

Resultado:
[@0,0:0='a',<ID>,1:0]
[@1,1:1='=',<'='>,1:1]
[@2,2:3='10',<INT>,1:2]
[@3,4:4=';',<';'>,1:4]
[@4,6:6='b',<ID>,1:6]
[@5,8:8='=',<'='>,1:8]
[@6,10:10='5',<INT>,1:10]
[@7,12:12='+',<'+'>,1:12]
[@8,14:14='a',<ID>,1:14]
[@9,16:16='*',<'*'>,1:16]
[@10,18:18='2',<INT>,1:18]
[@11,19:19=';',<';'>,1:19]
[@12,21:21='c',<ID>,1:21]
[@13,23:23='=',<'='>,1:23]
[@14,25:25='(',<'('>,1:25]
[@15,26:26='b',<ID>,1:26]
[@16,28:28='-',<'-'>,1:28]
[@17,30:30='3',<INT>,1:30]
[@18,31:31=')',<')'>,1:31]
[@19,33:33='/',<'/'>,1:33]
[@20,35:35='2',<INT>,1:35]
[@21,36:36=';',<';'>,1:36]
[@22,38:37='<EOF>',<EOF>,2:0]

4. echo "a=10; b = 5 + a * 2; c = (b - 3) / 2;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica programa -tree

(programa (expresion a = (expresion 10)) ; (expresion (expresion b = (expresion 5)) + (expresion (expresion a) * (expresion 2))) ; (expresion (expresion c = (expresion ( (expresion (expresion b) - (expresion 3)) ))) / (expresion 2)) ;)

Preguntas del Cuestionario:

1. b) Como operadores aritméticos específicos
Porque en ANTLR, los operadores +, -, * y / se definen explicitamente en la gramatica como tokens unicos y son reconocidos como tales en la salida de -tokens.

2. El arbol se construye respetando la jerarquía de operadores, evaluando primero * antes que +, lo que confirma que la opción d) es la correcta.

3. Dado que visualizar los tokens y el arbol ayuda tanto a entender la traducción del codigo, optimizarlo y verificar la gramatica, la opción d) Todas las anteriores es la correcta. 

