#!/usr/bin/env python
'''
FuncionesDescriptivas
---------------------------
Autor: Johana Rangel
Version: 1.0
Descripcion:
Módulo con algunas de las funciones que ejemplifican
las herramientas módulo que utilizará para resolver 
los ejercicios_practica.py del módulo "Funciones"..
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.0"

import random

#-------------------Declarando las variables----------
numeros = list()
inicio = int()
fin = int()
cantidad = int()
lista_numeros = list()
numero = int()
dados_guardados = list()
cantidad_guardados = list()
numero_repetido = int()
segundo_repetido = int()
#-------------------Formación de funciones----------

def promedio(numeros):
    '''Función que permite calcular el promedio de varios números'''
    cantidad_numeros = len(numeros)
    sumatoria_numeros = sum(numeros)
                   
    for numero in numeros:
        promedio = sumatoria_numeros / cantidad_numeros
        print('El promedio de {} es: {}'.format(numeros, round(promedio, 2)))
        return promedio
        
    if numeros == []:
        print('No tiene notas para calcular el promedio, la lista está vacía')
        

def ordenar(numeros, operador=1):
    '''ordena los numeros de menor a mayor'''
          
    if operador == 1:
        lista_numeros = sorted(numeros)
        print('lista ordenada en forma creciente:', lista_numeros)
        return lista_numeros

    elif operador == 2:
        lista_numeros = sorted(numeros, reverse=True)
        print('lista ordenada en forma decreciente:', lista_numeros)
        return lista_numeros

    else: 
        print('El operador ingresado no corresponde con los indicados, intente nuevamente.')
           
            
def lista_aleatoria(inicio, fin, cantidad):
    '''Función que arroja una lista de números al azar, la cantidad depende de la introducida'''
    mi_lista_aleatorio = []
     
    for numero in range(cantidad):
        numero = random.randrange(inicio, fin+1)
        mi_lista_aleatorio.append(numero)
    
    return mi_lista_aleatorio

      
def contar(lista_numeros, numero):
    '''Función que permite contar números'''
    cantidad_veces = lista_numeros.count(numero)
    return cantidad_veces

def evaluar_dados(dados_guardados):
    '''Función que evalúa sin los cinco elementos de una lista son iguales'''
    for i in dados_guardados:
        if (len(dados_guardados) == 5 and i == numero_repetido):
            return True
        else:
          return False


if __name__ == "__main__":

    promedio(numeros)

    ordenar(numeros)

    mi_lista_aleatorio = lista_aleatoria(inicio, fin, cantidad)
    print(mi_lista_aleatorio)

    cantidad_numero = contar(lista_numeros, numero)
    print(cantidad_numero)

    evaluar_dados(dados_guardados)