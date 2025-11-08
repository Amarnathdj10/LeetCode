import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    filtered = customers[~customers['id'].isin(orders['customerId'])]
    filtered = filtered[['name']].rename(columns={'name': 'Customers'})
    return filtered