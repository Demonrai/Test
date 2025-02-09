import re
import dataConnect
def select_query(option):
    option=option.lower()

    #find employee of the department
    if "employee " in option and "department" in option:
        employee_department=re.search(r"employee from (.*?) department",option).group(1)
        return dataConnect.employees(employee_department)
    
    elif "manager" in option:
        search_manager = re.search(r"manager (.*?)$", option)
        if search_manager:
            department = search_manager.group(1).strip() 
            return dataConnect.manager(department)
    
    # find the total salary expenses
    elif "salary" in option and "department" in option:
        salary_sum=re.search(r"all salary from  (.*?)$ department",option).group(1)
        return dataConnect.total_salary_expense(salary_sum)
    

    elif "hired after date" in option:
        date_hired=re.search(r"employees hired after (.*?)$",option).group(1)
        return dataConnect.employees_hired_after(date_hired)
    else:
        return "Didnt understand sorry"