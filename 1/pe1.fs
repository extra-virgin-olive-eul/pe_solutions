: mod3 ( -- ) 3 mod 0= IF true ELSE false ENDIF ;
: mod5 ( -- ) 5 mod 0= IF true ELSE false ENDIF ;
: mod3or5 ( -- ) dup mod3 true = IF true ELSE dup mod5 ENDIF ;
: main ( -- ) 1000 1 ?DO i mod3or5 true = IF + ELSE drop ENDIF LOOP ;

0
main
.
