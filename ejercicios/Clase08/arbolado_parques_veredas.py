import os
import pandas as pd


def comparacion(especies):
    '''
    Realiza un gráfico comparativo de una especie
    
    Pre: recibe una lista de especies a buscar
    Pos: Muestra un gráfico con la comparativa entre los dos archivos.
    '''
    
    directorio = '../Data'
    archivo = 'arbolado-en-espacios-verdes.csv'
    archivo2 = 'arbolado-publico-lineal-2017-2018.csv'
    
    fname = os.path.join(directorio,archivo)
    df_parques = pd.read_csv(fname, low_memory=False)
    
    fname = os.path.join(directorio,archivo2)
    df_veredas = pd.read_csv(fname, low_memory=False)
    
    cols_parques = ['nombre_cie', 'altura_tot', 'diametro']
    cols_veredas = ['nombre_cientifico', 'altura_arbol', 'diametro_altura_pecho']
    
    df_tipas_parques = df_parques[cols_parques].copy()
    df_tipas_parques.columns = cols_veredas
    df_tipas_parques = df_tipas_parques[df_tipas_parques['nombre_cientifico'].isin(especies)]
    df_tipas_parques['ambiente'] = 'parque'
    
    df_tipas_veredas = df_veredas[cols_veredas].copy()
    df_tipas_veredas = df_tipas_veredas[df_tipas_veredas['nombre_cientifico'].isin(especies)]
    df_tipas_veredas['ambiente'] = 'vereda'
    
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])    
    df_tipas.boxplot('diametro_altura_pecho', by = 'ambiente')
    
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])    
    df_tipas.boxplot('altura_arbol', by = 'ambiente')


if __name__ == '__main__':
    especies = ['Tipuana tipu','Tipuana Tipu']
    comparacion(especies)