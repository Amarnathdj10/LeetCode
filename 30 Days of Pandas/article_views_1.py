import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filtered = views[views['author_id']==views['viewer_id']]
    filtered = filtered.drop_duplicates(subset='author_id',keep='first') 
    filtered = filtered[['author_id']].rename(columns={'author_id':'id'})
    return filtered.sort_values(by='id')
