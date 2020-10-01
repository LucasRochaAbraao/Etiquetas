#!/usr/bin/env python3
# coding=utf-8

# ############# PEGAR ARGS ################
# import argparse

# parser = argparse.ArgumentParser(description="Criador de etiquetas")
# parser.add_argument("-i", "-I", type=int, help="Número inicial")
# parser.add_argument("-f", "-F", type=int, help="Número final")
# parser.add_argument("-c", "-C", type=int, help="Modelo da etiqueta")
# parser.add_argument("-d", "-D", type=int, help="Modo debug")
# #parser.add_argument("-a", "-A", type=int, help="Automaticamente gerar 250 etiquetas de cada modelo.")
# args = parser.parse_args()
# # definir args
# inicio, fim, modelo_comum, debug = args.i, args.f, args.c, args.d

############# GERAR ETIQUETAS ###############
from src.etiquetas_novo import Etiquetas

inicio = 10
fim = 12

etiquetas = Etiquetas()
etiquetas.gerar()
#etq.debug()  # Habilite se necessário, mas passando "-d 1" habilita o modo debug.
etiquetas.salvar()


############ PRINTAR COLUNAS #############
'''
# usado para printar o que tem em cada coluna de uma worksheet.
lista = []
def col_print(WS, lista):
    for row in range(2, WS.max_row+1):
        for column in "ABCD":
            cell_name = "{}{}".format(column, row)
            lista.append(WS[cell_name].value)
#col_print(WS, lista)
#for i in lista:
#    print(i)
'''
