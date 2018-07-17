/*  
	ABeeman, 17-Jul-2018
	Solution for Euler Problem #1
	https://projecteuler.net/problem=1
	Language: T-SQL
*/

-- Run the DROP statement if running this code more than once to check other max values or modulos
--drop table #MultiplesUnder1000
create table #MultiplesUnder1000(myNum int)

--select * from #MultiplesUnder1000

declare @myInt integer = 1

while @myInt < 1000
begin
	if (@myInt % 3 = 0 or @myInt % 5 = 0)
	begin
		insert into #MultiplesUnder1000
		select @myInt
	end

	set @myInt = @myInt + 1
end

select * from #MultiplesUnder1000

select sum(myNum) from #MultiplesUnder1000