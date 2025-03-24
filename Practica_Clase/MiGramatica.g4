grammar MiGramatica;

programa: (forStmt ';')+ EOF ;

forStmt
    : 'for' '(' inicializacion ';' condicion ';' actualizacion ')' '{' (asignacion ';')* '}' # ForLoop
    ;

inicializacion
    : asignacion  # ForInitAssign
    |             # ForInitEmpty
    ;

condicion
    : expresion # CondicionExpresion
    ;

actualizacion
    : expresion # ForUpdateExpresion
    |           # ForUpdateEmpty
    ;

asignacion
    : ID '=' expresion # Assign
    ;

expresion
    : expresion op=('*'|'/') expresion     # MulDiv
    | expresion op=('+'|'-') expresion     # AddSub
    | expresion op=('<'|'>'|'=='|'!=') expresion # Comparacion
    | INT                                  # Int
    | ID                                   # Variable
    | ID '++'                              # Incremento
    | ID '--'                              # Decremento
    | '(' expresion ')'                    # Parens
    ;

ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT : [0-9]+ ;                   // Números enteros
WS  : [ \t\r\n]+ -> skip ;       // Ignorar espacios en blanco