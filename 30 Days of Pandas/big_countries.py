import pandas as pd

def selectBigCountries(world: pd.DataFrame) -> pd.DataFrame:
    return world.query("area >= 3000000 or population >= 25000000")[['name', 'population', 'area']]