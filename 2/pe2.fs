variable v
0 v !

: nextfib ( -- ) over over + rot drop ;
: lessthan4mil ( -- ) dup 4000000 < IF true ELSE false ENDIF ;
: even ( -- ) dup 2 mod 0= IF true ELSE false ENDIF ;
: add2total ( -- ) dup v @ + v ! ;
: main ( -- ) BEGIN nextfib lessthan4mil WHILE even IF add2total ENDIF REPEAT ;

1 1 
main 
v @ .
