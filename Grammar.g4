grammar Grammar;

options {
    language='Python3';
}

prog: ((statement|imp) SEMI | bracket_statement)*;

statement: (expr | var_declaration | var | conditional_statement) # normalStatement
    | (VARNAME'.')* (expr | var_declaration | var | conditional_statement) # fileStatement
    ;
bracket_statement: (conditional_statement | function_def);

imp: 'import' (VARNAME.)* VARNAME;

var_declaration: ('public'|) name=VARNAME '=' exp=statement # singleVar
    | ('public'|) name=varname_list '=' vals=varname_list # multiVar
    | ('public'|) name=VARNAME '=' '[' vals=var_list ']' # listVar
    | ('public'|) name=VARNAME '[' index=NUM ']' '=' exp=statement # listSet 
    ;

var: inv='!' name=VARNAME # invertVar
    | name=VARNAME # varName
    | name=VARNAME '[' index=NUM ']' # listGet
    ;

conditional_statement: label=('if'|'while') '(' t=truth ')' stmts=brackets;
truth: '(' t=truth ')' # parenTruth
    | lhs=truth logic=('&&'|'||') rhs=truth # logicTruth
    | lhs=statement operand=('=='|'!=') rhs=statement # atomTruth
    ;

function_def: ('public'|) 'def' name=VARNAME '(' args=varname_list ')' '{' stmts=brackets '}';

varname_list: lhs=varname_list ',' rhs=varname_list # commaVarname
    | atom=VARNAME # atomVarname
    | # nullVarname
    ;

var_list: lhs=var_list ',' rhs=var_list # commaVarlist
    | atom=statement # atomVarlist
    | # nullVarlist
    ;

brackets: lhs=brackets rhs=brackets # semiBrackets
    | atom=statement SEMI # atomBrackets
    ;

expr: '(' exp=expr ')' # parensExpr
    | SUB exp=expr # negExpr
    | lhs=expr op=(MUL|DIV) rhs=expr # opExpr
    | lhs=expr op=(ADD|SUB|MOD) rhs=expr # opExpr
    | atom=NUM # intExpr
    | atom=BOOL # boolExpr
    | atom=StringLiteral # strExpr
    | atom=NULL # nullExpr
    | atom=FLOAT # floatExpr
    | atom=var # varExpr
    | name=VARNAME '(' args=var_list ')' # function_call
    ;

// fragments
SEMI: [;]+;
NL: [\r\n ]+ -> skip;

NUM: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
BOOL: ('true'|'false');
// i have zero clue why this works, i found it on a random stack overflow post
StringLiteral: UnterminatedStringLiteral ('"');
UnterminatedStringLiteral: ('"') (~["\\\r\n] | '\\' (. | EOF))* ;
NULL: 'null';

BlockComment: '/*' .*? '*/' -> skip;
Comment: '//' .*? -> skip;

VARNAME: ([a-zA-Z_])([a-zA-Z0-9-_]*);

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';