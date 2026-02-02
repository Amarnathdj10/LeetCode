import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates()
    salaries = salaries.sort_values(ascending=False)
    column_name = f'getNthHighestSalary({N})'
    if N <= 0:
        return pd.DataFrame({column_name: [None]})
    if len(salaries) >= N:
        return pd.DataFrame({column_name : [salaries.iloc[N-1]]})
    else:
        return pd.DataFrame({column_name: [None]})