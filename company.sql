USE company;
### CRETE TABLE EMPLOYEE
-- CREATE TABLE Employees (
--     ID INT AUTO_INCREMENT PRIMARY KEY,
--     Name VARCHAR(255),
--     Department VARCHAR(255) NOT NULL,
--     Salary INT NOT NULL,
--     Hire_Date DATE
-- );

### SET VALUE IN TABLES employee
-- INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES ('Alice', 'Sales', 50000, '2021-01-15');
-- INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES ('Bob', 'Engineering', 70000, '2020-06-10');
-- INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES ('Charlie', 'Marketing', 60000, '2022-03-2');
-- INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES ('Thomas', 'Developer', 55000, '2021-08-15');

### CRETE TABLE  Departments
-- CREATE TABLE Departments (ID INT AUTO_INCREMENT PRIMARY KEY,
--     Name VARCHAR(255), Manager VARCHAR(255) NOT NULL)
### SET VALUE IN TABLES Departments
-- INSERT INTO Departments (Name, Manager ) VALUES ('Alice', 'Sales');
-- INSERT INTO Departments (Name, Manager ) VALUES ('Bob', 'Engineering');
-- INSERT INTO Departments (Name, Manager ) VALUES ('Charlie', 'Marketing');
-- INSERT INTO Departments (Name, Manager ) VALUES ('Thomas', 'Developer');
-- drop table Departments

-- SELECT * FROM Departments Where ID=3
-- SELECT * FROM Departments
-- SELECT * FROM employees
SELECT Name,Department FROM Employees WHERE Hire_Date >2020-06-10