import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)
dh = df['12-25-2014':].copy()