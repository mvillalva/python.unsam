import rebotes
import hipoteca
import informe_funciones
from fileparse import parse_csv

# help(informe_funciones)
# dir(informe_funciones)

# help(fileparse)
# dir(fileparse)

camion = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
print(camion)

lista_precios = parse_csv('../Data/precios.csv', types = [str, float], has_headers = False)
print(lista_precios)

precios = dict(lista_precios)
print(precios['Naranja'])