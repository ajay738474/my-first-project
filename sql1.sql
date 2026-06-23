

CREATE TABLE employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Department VARCHAR(20),
    Salary INT
);


INSERT INTO employees VALUES
(1,'Ajay','IT',50000),
(2,'Ravi','HR',40000),
(3,'Kumar','IT',70000),
(4,'Priya','Finance',60000),
(5,'Anu','HR',45000);

SELECT * FROM employees;


SELECT Name FROM employees;


SELECT Name, Salary FROM employees;


SELECT *
FROM employees
WHERE Salary > 50000;


SELECT *
FROM employees
WHERE Salary < 50000;


SELECT *
FROM employees
WHERE Salary = 50000;


SELECT *
FROM employees
ORDER BY Salary;


SELECT *
FROM employees
ORDER BY Salary DESC;


SELECT COUNT(*)
FROM employees;


SELECT AVG(Salary)
FROM employees;


SELECT MAX(Salary)
FROM employees;


SELECT MIN(Salary)
FROM employees;

SELECT SUM(Salary)
FROM employees;

SELECT Department, COUNT(*)
FROM employees
GROUP BY Department;

SELECT Department, AVG(Salary)
FROM employees
GROUP BY Department;


SELECT Department, MAX(Salary)
FROM employees
GROUP BY Department;


SELECT *
FROM employees
WHERE Department = 'IT';

SELECT *
FROM employees
WHERE Department = 'HR'
AND Salary > 40000;