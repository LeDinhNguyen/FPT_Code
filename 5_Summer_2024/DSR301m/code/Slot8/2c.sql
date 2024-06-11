--Query A1: Enter a function that calculates the total cost of all animal rescues in the PETRESCUE table.
select SUM(COST) from PETRESCUE;
--Query A2: Enter a function that displays the total cost of all animal rescues in the PETRESCUE table in a column called SUM_OF_COST.
select SUM(COST) AS SUM_OF_COST from PETRESCUE;
--Query A3: Enter a function that displays the maximum quantity of animals rescued.
select MAX(QUANTITY) from PETRESCUE;
--Query A4: Enter a function that displays the average cost of animals rescued.
select AVG(COST) from PETRESCUE;
--Query A5: Enter a function that displays the average cost of rescuing a dog.
select AVG(COST/QUANTITY) from PETRESCUE where ANIMAL = 'Dog';

--Query B1: Enter a function that displays the rounded cost of each rescue.
select ROUND(COST) from PETRESCUE;
--Query B2: Enter a function that displays the length of each animal name.
select LENGTH(ANIMAL) from PETRESCUE;
--Query B3: Enter a function that displays the animal name in each rescue in uppercase.
select UCASE(ANIMAL) from PETRESCUE;
--Query B4: Enter a function that displays the animal name in each rescue in uppercase without duplications.
select DISTINCT(UCASE(ANIMAL)) from PETRESCUE;
--Query B5: Enter a query that displays all the columns from the PETRESCUE table, where the animal(s) rescued are cats. Use cat in lower case in the query.
select * from PETRESCUE where LCASE(ANIMAL) = 'cat';

--Query C1: Enter a function that displays the day of the month when cats have been rescued.
select DAY(RESCUEDATE) from PETRESCUE where ANIMAL = 'Cat';
--Query C2: Enter a function that displays the number of rescues on the 5th month.
select SUM(QUANTITY) from PETRESCUE where MONTH(RESCUEDATE)='05';
--Query C3: Enter a function that displays the number of rescues on the 14th day of the month.
select SUM(QUANTITY) from PETRESCUE where DAY(RESCUEDATE)='14';
--Query C4: Animals rescued should see the vet within three days of arrivals. Enter a function that displays the third day from each rescue.
select (RESCUEDATE + 3 DAYS) from PETRESCUE;
--Query C5: Enter a function that displays the length of time the animals have been rescued; the difference between today’s date and the recue date.
select (CURRENT DATE - RESCUEDATE) from PETRESCUE;

--1
select * 
from employees 
where salary < AVG(salary);
--2 
select EMP_ID, F_NAME, L_NAME, SALARY 
from employees 
where SALARY < (select AVG(SALARY) 
                from employees);
-- 3 
select EMP_ID, SALARY, MAX(SALARY) AS MAX_SALARY 
from employees;	
--4
select EMP_ID, SALARY, ( select MAX(SALARY) from employees ) AS MAX_SALARY 
from employees;
--5
select * from ( select EMP_ID, F_NAME, L_NAME, DEP_ID from employees) AS EMP4ALL;

--Ex1
--1
select * from employees where JOB_ID IN (select JOB_IDENT from jobs);
--2 
select * from employees where JOB_ID IN (select JOB_IDENT from jobs where JOB_TITLE= 'Jr. Designer');
--3
select JOB_TITLE, MIN_SALARY,MAX_SALARY,JOB_IDENT from jobs where JOB_IDENT IN (select JOB_ID from employees where SALARY > 70000 );
--4
select JOB_TITLE, MIN_SALARY,MAX_SALARY,JOB_IDENT from jobs where JOB_IDENT IN (select JOB_ID from employees where YEAR(B_DATE)>1976 );
--5 
select JOB_TITLE, MIN_SALARY,MAX_SALARY,JOB_IDENT from jobs where JOB_IDENT IN (select JOB_ID from employees where YEAR(B_DATE)>1976 and SEX='F' );

--Ex2
--1 
select * from employees, jobs;
--2 
select * from employees, jobs where employees.JOB_ID = jobs.JOB_IDENT;
--3 
select * from employees E, jobs J where E.JOB_ID = J.JOB_IDENT;
--4 
select EMP_ID,F_NAME,L_NAME, JOB_TITLE from employees E, jobs J where E.JOB_ID = J.JOB_IDENT;
--5 
select E.EMP_ID,E.F_NAME,E.L_NAME, J.JOB_TITLE from employees E, jobs J where E.JOB_ID = J.JOB_IDENT;

