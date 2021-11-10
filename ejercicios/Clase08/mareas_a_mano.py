import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)
dh = df['12-25-2014':].copy()

delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 20.5 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()