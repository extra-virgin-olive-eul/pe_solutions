: mod3 ( -- ) 3 mod 0= if true else false endif ;
: mod5 ( -- ) 5 mod 0= if true else false endif ;
: mod3or5 ( -- ) dup mod3 true = if true else dup mod5 endif ;
: main ( -- ) 1000 1 ?DO i mod3or5 true = if + else drop endif LOOP ;

0
main
