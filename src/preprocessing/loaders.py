import pandas as pd

def load_air_data(path: str) -> pd.DataFrame:

    if path.endswith(".csv"):
        return pd.read_csv(path, sep=";", decimal=",")

    elif path.endswith(".xlsx") or path.endswith(".xls"):
        return pd.read_excel(path)

    else:
        raise ValueError("Format non supporté")