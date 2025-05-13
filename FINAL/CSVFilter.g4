grammar CSVFilter;

prog: stat+ ;

stat
    : loadStat
    | filterStat
    | aggregateStat
    | printStat
    ;

loadStat:   'load' STRING ';' ;
filterStat: 'filter' 'column' STRING OPERATOR NUMBER (('and' | 'or') 'column' STRING OPERATOR NUMBER)* ';' ;
condition: 'column' STRING OPERATOR NUMBER ;  // Definir una condición simple para cada columna

aggregateStat: 'aggregate' AGG_FUNC 'column' STRING ';' ;
printStat:  'print' ';' ;

AGG_FUNC: 'count' | 'sum' | 'average' ;
OPERATOR: '>' | '<' | '>=' | '<=' | '==' | '!=' ;
STRING: '"' (~["\r\n])* '"' ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;

// Comentarios tipo línea
COMMENT: '//' ~[\r\n]* -> skip ;

// Espacios en blanco
WS: [ \t\r\n]+ -> skip ;
