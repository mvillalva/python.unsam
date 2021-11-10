# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:21:22 2021

@author: julid
"""

# vigilante.py
import os
import time


def vigilar(archivo):
    f = open(archivo)
    f.seek(0, os.SEEK_END)
    
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line

if __name__ == '__main__':
    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if volumen > 1000:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')