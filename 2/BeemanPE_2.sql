/*  
	ABeeman, 25-Jul-2018
	Solution for Euler Problem #2
	https://projecteuler.net/problem=2
	Language: T-SQL
*/

-- Run the DROP statement if running this code more than once to check other max values or modulos
--DROP table #evenValues

create table #evenValues(myNum int)

declare @Fib1 int = 1
declare @Fib2 int = 2
declare @current int = @Fib1 + @Fib2

if (@Fib1 % 2 = 0)
begin
	insert into #evenValues
	select @Fib1
end

if (@Fib2 % 2 = 0)
begin
	insert into #evenValues
	select @Fib2
end

while @current < 4000001
begin
	if (@current % 2 = 0)
	begin
		insert into #evenValues
		select @current
	end

	set @Fib1 = @Fib2
	set @Fib2 = @current
	set @current = @Fib1 + @Fib2
end

select sum(myNum) from #evenValues