grammar CSVFilter;

prog: stat+ ;

stat
    : loadStat
    | filterStat
    | aggregateStat
    | printStat
    ;

loadStat: LOAD STRING SEMI ;
filterStat: FILTER COLUMN STRING OPERATOR NUMBER (LOGIC_OP COLUMN STRING OPERATOR NUMBER)* SEMI ;
aggregateStat: AGGREGATE AGG_FUNC COLUMN STRING SEMI ;
printStat: PRINT SEMI ;

// Palabras clave como tokens individuales
LOAD: 'load' ;
FILTER: 'filter' ;
AGGREGATE: 'aggregate' ;
PRINT: 'print' ;
COLUMN: 'column' ;

// Funciones de agregación
AGG_FUNC: 'count' | 'sum' | 'average' ;

// Operadores lógicos
LOGIC_OP: 'and' | 'or' ;

// Operadores de comparación
OPERATOR: '>' | '<' | '>=' | '<=' | '==' | '!=' ;

// Otros tokens
STRING: '"' (~["\r\n])* '"' ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;

// Comentarios línea
COMMENT: '//' ~[\r\n]* -> skip ;

// Espacios en blanco
WS: [ \t\r\n]+ -> skip ;

// Caracteres especiales
SEMI: ';' ;
