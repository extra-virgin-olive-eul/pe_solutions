%macro populate_table;  
    /* Craft a table of the first 1000 ints evenly divisible by 3 or 5 */
    %local i;

    proc sql noprint;
        create table first_1000_mod3or5 (NUMBER num(15) NOT NULL);
        %do i=1 %to 1000;
            %if %sysfunc(mod(&i, 3)) = 0 %then %do;
                insert into first_1000_mod3or5 VALUES (&i) ;
            %end;
            %else %do;
                %if %sysfunc(mod(&i, 5)) = 0 %then %do;
                    insert into first_1000_mod3or5 VALUES (&i) ;
                %end;
            %end;
        %end;
    quit;
%mend;

%populate_table;

proc sql;
    select sum(NUMBER) from first_1000_mod3or5;
quit;
