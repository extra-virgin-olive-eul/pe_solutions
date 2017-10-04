data fibs;
    a = 1;
    b = 1;
    output;
    do until(b > 4000000);
        c = a + b;
        output;
        a = b;
        b = c;
    end;
    rename b = fib;
    drop a c;
run;

/* If this next part is done above, it seg faults */
data evenfibs;
    set fibs;
    if mod(fib, 2) = 0;
run;

proc means data=evenfibs SUM;
run;
