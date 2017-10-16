: sumofsquares ( -- ) 0 101 1 ?DO i i * + LOOP ;
: squareofsums ( -- ) 100 dup 1+ * 2 / dup * ;

sumofsquares squareofsums
swap - .
