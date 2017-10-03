data numbers;
    do i = 1 to 1000;
        if mod(i, 3) = 0 or mod(i, 5) = 0 then output;
    end;
run;

proc means data=numbers SUM;
run;
