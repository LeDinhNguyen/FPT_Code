--Query 1--
select f_name, l_name from EMPLOYEES
where address like '%Elgin,IL%'
--Query2--
select f_name,l_name from employees
where b_date like '197%''
-- Query 3--
select * from employees 
where (salary between 60000 and 70000) and dep_id=7
--Query 4--
select f_name, l_name, dep_id from employees
order by dep_id
-- Query 5--
select f_name, l_name , dep_id from employees
order by dep_id desc, l_name desc
--Query 6--
select d.dep_name, e.f_name, e.l_name 
from employees as e, departments as d 
order by d.dep_name, e.l_name desc
--Query 7--
select dep_id, count(*)
from employees 
group by dep_id 
--Query 8--
select dep_id, count(*), AVG(salary)
from employees 
group by dep_id
--Query 9--
select dep_id, count(*) as "num_employees", AVG(salary) as "AVG_SALARY"
from employees 
group by dep_id ;
--Query 10--
select dep_id, count(*) as "num_employees", avg(salary) as "avg_salary"
from employees 
group by dep_id 
order by avg_salary
--Query 11--
select dep_id, count(*) as "num_employees",avg(salary) as "avg_salary"
from employees 
group by dep_id 
having count(*) < 4
order by avg(salary)
