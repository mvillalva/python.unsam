import numpy as np
import pandas as pd
import seaborn as sns

horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()

w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()
df_walk_suav.to_csv('caminata_apostolica.csv')

#%%
import os
import pandas as pd
import seaborn as sns

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
# print(df.columns)
# print(df.index)
# print(df['nombre_com'].unique())
# print((df['nombre_com'] == 'Ombú').sum())
cant_ejemplares = df['nombre_com'].value_counts()
# print(cant_ejemplares.head(10))

df_jacarandas = df[df['nombre_com'] == 'Jacarandá']

cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
# print(df_jacarandas.tail())

# print(df_jacarandas)

df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()
# print(df_jacarandas)
# df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')
# sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')

cant_ejemplares = df['nombre_com'].value_counts()
# print(cant_ejemplares.index)
# print(df.loc[165])
# print(cant_ejemplares.loc['Eucalipto'])
# print(df_jacarandas.iloc[0])

# print(cant_ejemplares)
# print(cant_ejemplares.iloc[0:3])
print(df_jacarandas)
print(df_jacarandas.iloc[-5:,2])