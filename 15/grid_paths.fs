: fact ( -- ) 1+ 1 ?DO i * LOOP ;
: perm_w_rep ( -- ) 40 fact 1 20 fact 1 20 fact * / ;

1 perm_w_rep .
