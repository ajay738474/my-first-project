-- Create Table

CREATE TABLE employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Department VARCHAR(20),
    Salary INT
);

-- Insert Data

INSERT INTO employees VALUES
(1,'Ajay','IT',50000),
(2,'Ravi','HR',40000),
(3,'Kumar','IT',70000),
(4,'Priya','Finance',60000),
(5,'Anu','HR',45000);

-- Show All Data

SELECT * FROM employees;

-- Show Specific Column

SELECT Name FROM employees;

-- Multiple Columns

SELECT Name, Salary FROM employees;

-- Filter Rows

SELECT * FROM employees
WHERE Salary > 50000;

-- Sort Ascending

SELECT * FROM employees
ORDER BY Salary;

-- Sort Descending

SELECT * FROM employees
ORDER BY Salary DESC;

-- Count Rows

SELECT COUNT(*) FROM employees;

-- Average Salary

SELECT AVG(Salary) FROM employees;

-- Maximum Salary

SELECT MAX(Salary) FROM employees;

-- Minimum Salary

SELECT MIN(Salary) FROM employees;

-- Sum of Salaries

SELECT SUM(Salary) FROM employees;

-- Group By

SELECT Department, AVG(Salary)
FROM employees
GROUP BY Department;

-- Having

SELECT Department, AVG(Salary)
FROM employees
GROUP BY Department
HAVING AVG(Salary) > 50000;

-- Inner Join

SELECT e.Name, d.DepartmentName
FROM employee_dept e
INNER JOIN departments d
ON e.DeptID = d.DeptID;

-- Left Join

SELECT e.Name, d.DepartmentName
FROM employee_dept e
LEFT JOIN departments d
ON e.DeptID = d.DeptID;

-- Subquery

SELECT *
FROM employees
WHERE Salary >
(
    SELECT AVG(Salary)
    FROM employees
);