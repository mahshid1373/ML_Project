import pandas as pd


def clean_age_column(data):
    data['AgeGroup'] = pd.cut(data['Age'], bins=[0, 18, 35, 50, 65, 100], labels=[0, 1, 2, 3, 4])
    data['AgeGroup'] = data['AgeGroup'].astype('int64') 

    return data
