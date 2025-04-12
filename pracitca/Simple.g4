grammar Simple;

prog: classDef+ ;

classDef
    : 'class' ID '{' member+ '}' 
    ;

member
    : 'int' ID ';'
    | 'int' ID '(' ID ')' '{' stat+ '}' 
    ;

stat
    : expr ';'
    | ID '=' expr ';'
    ;

expr
    : expr op=('*'|'/') expr      # MulDivExpr
    | expr op=('+'|'-') expr      # AddSubExpr
    | ID '(' expr ')'             # FuncCallExpr
    | INT                         # IntExpr
    | ID                          # IdExpr
    | '(' expr ')'                # ParenExpr
    ;

INT : [0-9]+ ;
ID  : [a-zA-Z]+ ;
WS  : [ \t\r\n]+ -> skip ;
