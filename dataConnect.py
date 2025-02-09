import mysql.connector
import re
try:
    new_database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="demon",
            database="company" 
        )
    if new_database.is_connected():
            print("successfully connected")
    else:
            print("failed to connect")
except:
    print(f"Error")   

cursor=new_database.cursor()
# cursor.execute("SELECT * from employees")
# new_data=cursor.fetchall()
# for x in new_data:
#     print(x)


# “Show me all employees in the [department] department.”
def employees(Employee):
    cursor=new_database.cursor()
    cursor.execute("SELECT Name, Department, Salary, Hire_Date FROM Employees WHERE Department = %s",(Employee,))
    return cursor.fetchall()

# “Who is the manager of the [department] department?”
def manager(Department):
   cursor=new_database.cursor()
   cursor.execute("SELECT Name FROM Departments WHERE Manager = %s", (Department,))
   return cursor.fetchall()

# “List all employees hired after [date].”
def employees_hired_after(date):
    cursor=new_database.cursor()
    cursor.execute("SELECT * FROM Employees WHERE Hire_Date >%s", (date,))
    return cursor.fetchall()

# “What is the total salary expense for the [department] department?”
def total_salary_expense(amount):
    cursor=new_database.cursor()    
    cursor.execute("SELECT SUM(Salary) FROM Employees WHERE Department = %s", (amount,))
    return cursor.fetchall()[0]

