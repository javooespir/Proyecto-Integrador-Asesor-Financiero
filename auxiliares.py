'''
Funciones de apoyo para el proyecto integrador, se compone de leer el csv para definir el o los tipos de inversion '''


import csv
from itertools import count

def acciones():
    print('Se recomiendan las siguientes acciones: ')
    csvfile = open("inversiones.csv")
    accion = list(csv.DictReader(csvfile))

    for acc_1 in accion:
        print(acc_1['acciones'])
    csvfile.close()


def divisas():
    print('Se recomiendan las siguientes divisas: ')

    csvfile = open('inversiones.csv')
    divisa = list(csv.DictReader(csvfile))

    for div_1 in divisa:
        print(div_1['divisas'])
    csvfile.close()


def etf():
    print('Se recomiendan los siguientes fondos etf: ')

    csvfile = open('inversiones.csv')
    etfs = list(csv.DictReader(csvfile))

    for etfs_1 in etfs:
        print(etfs_1['etf'])
    csvfile.close()


def bonos():
    print('Se recomiendan los siguientes bonos: ')

    csvfile = open('inversiones.csv')
    bono = list(csv.DictReader(csvfile))

    for bono_1 in bono:
        print(bono_1['bonos'])
    csvfile.close()


def cryptomonedas():
    print('Se recomiendan las siguientes cryptos: ')

    csvfile = open('inversiones.csv')
    crypto = list(csv.DictReader(csvfile))

    for crypto_1 in crypto:
        print(crypto_1['cryptomonedas'])
    csvfile.close()


def materia_prima():
    print('Se recomiendan las siguientes materias primas: ')

    csvfile = open('inversiones.csv')
    materia = list(csv.DictReader(csvfile))

    for mp_1 in materia:
        print(mp_1['materia'])
    csvfile.close()


