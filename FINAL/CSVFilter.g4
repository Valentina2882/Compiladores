grammar CSVFilter;

prog: stat+ ;

stat
    : loadStat
    | filterStat
    | aggregateStat
    | printStat
    ;

loadStat:   'load' STRING ';' ;
filterStat: 'filter' 'column' STRING OPERATOR NUMBER ';' ;
aggregateStat: 'aggregate' AGG_FUNC 'column' STRING ';' ;
printStat:  'print' ';' ;

AGG_FUNC: 'count' | 'sum' | 'average' ;
OPERATOR: '>' | '<' | '>=' | '<=' | '==' | '!=' ;
STRING: '"' (~["\r\n])* '"' ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;

WS: [ \t\r\n]+ -> skip ;
