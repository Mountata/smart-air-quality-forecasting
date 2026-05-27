import pandas as pd 

# verification des doublant 

def check_duplicate(data: pd.DataFrame) -> int:

    #Retourne le nombre de doublons
    return data.duplicated().sum()

def get_duplicate(data: pd.DataFrame) -> pd.DataFrame:
    "retoune les lignes dupliquées "
    
    return data[data.duplicated() ]

def remove_duplicates(data: pd.DataFrame) -> pd.DataFrame:
    """
    Supprime les doublons.
    """
    return data.drop_duplicates()





def get_duplicate_temporel_partiel(data: pd.DataFrame) -> str:
    # retourne les duoblons temporels partiels
    duplicate_temporel = data.duplicated(subset = ['Date', 'Time'], keep = False)

    return duplicate_temporel