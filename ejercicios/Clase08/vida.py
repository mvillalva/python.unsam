from datetime import datetime

def vida_en_segundos(fecha_nac):
    hoy     = datetime.today()
    fecha   = datetime.strptime(fecha_nac, '%d/%m/%Y')
    return (hoy - fecha).total_seconds()


if __name__ == '__main__':
    print(vida_en_segundos('04/10/1977'))