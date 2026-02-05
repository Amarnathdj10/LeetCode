import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee.groupby('departmentId')['salary'].max().reset_index()
    top_emp = pd.merge(employee, max_salary, on=['departmentId','salary'])
    result = pd.merge(top_emp, department, left_on='departmentId', right_on='id')
    return result[['name_y','name_x','salary']].rename(columns={'name_y':'Department', 'name_x':'Employee', 'salary':'Salary'})
 