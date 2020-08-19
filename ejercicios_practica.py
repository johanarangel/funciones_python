#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de práctica
---------------------------
Autor: Johana Rangel
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.3"


import funciones_descriptivas


def ej1():
    print('Comencemos a crear lo nuestro!')

    '''
    Cree un nuevo archivo el cual será su módulo que utilizará
    para resolver todos los ejercicios de está guía.
    En el módulo implemente todas las funciones que le fueron
    solicitadas en "ejercicios_clase":
    - promedio
    - lista_aleatoria
    - ordenar
    - contar

    Importe el módulo a este programa/documento para su uso
    en el resto de los ejercicios
    '''


def ej2():
    print("Jugando a los dados")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 valores con resultados posibles
    de un dado)
    ejemplo, se tiraron 5 dados y los resultados de lista aleatoria
    se deben parecer a:
    [1, 2, 3, 2, 5]
    Cada valor representa el valor que sacó cada uno de los 5 dados

    1)
    Utilice la función "ordenar" para ordenar la lista
    de números generados.
    Imprimir en pantalla la lista ordenada
    '''

    numeros = funciones_descriptivas.lista_aleatoria(inicio=1, fin=6, cantidad=5)
    print('Resultados del primer tiro de cinco dados:', numeros)
    funciones_descriptivas.ordenar(numeros=numeros, operador=1)
       

def ej3():
    print("Jugando a los dados")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 valores con resultados posibles
    de un dado)
    ejemplo, se tiraron 5 dados y los resultados de lista aleatoria
    se deben parecer a:
    [1, 2, 3, 2, 5]
    Cada valor representa el valor que sacó cada uno de los 5 dados

    1)
    Utilice la función "contar" para contar cuantas veces aparece:
    a - Cuantsa veces aparece el número 1 en su lista de dados tirados
    b - Cuantsa veces aparece el número 2 en su lista de dados tirados
    c - Cuantsa veces aparece el número 3 en su lista de dados tirados
    d - Cuantsa veces aparece el número 4 en su lista de dados tirados
    e - Cuantsa veces aparece el número 5 en su lista de dados tirados
    f - Cuantsa veces aparece el número 6 en su lista de dados tirados


    2)
    Utilice la función de Python max con la key de list.count para
    determinar cual fue el número que más se repitió. Consultar los ejemplos
    vistos en clase para ver como se implementa max con esa key

    '''

    lista_numeros = funciones_descriptivas.lista_aleatoria(inicio=1, fin=6, cantidad=5)
    print('Resultados del primer tiro de cinco dados:', lista_numeros)

    for numero in lista_numeros:
        cantidad_veces = funciones_descriptivas.contar(lista_numeros=lista_numeros, numero=numero)
        print('El numero {} se repite {}'.format(numero, cantidad_veces))

    numero_repetido = max(lista_numeros, key=lista_numeros.count)
    print('El número más repetido es:', numero_repetido)


def ej4():
    #print("Ahora sí! buena suerte :)")

    '''
    Este ejercicio representa ya un problema que forma parte de un juego
    Lo que se desea realizar es una parte del juego "la generala".
    El enunciado está armado a modo de guía, pueden resolver el problema
    de otra forma.
    Si tienen dudas sobre el enunciado o alguno de los puntos por favor
    comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
    puede haber varias interpretaciones de un mismo enunciado.

    Deberá realizar una lista para guardar 5 dados, guardar los números
    sacados en esa tirada de dados (son 5 números del 1 al 6)

    1) El jugador tira la dados y sacar 5 números aleatorios, puede usar
    la función de "lista_aleatoria" para generar dichos números.

    2) Luego debe analizar los 5 números y ver cual es el número que
    más se repitio entre los 5 dados.
    Debe usar la función de Python max con la key de list.count para
    determinar cual fue el número que más se repitió. Consultar los ejemplos
    vistos en clase o el ejercicio anterior de esta guia.

    3) Una vez reconocido el número más repetido entre los 5, debe
    guardar en una lista esos números.
    Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4"
    Debe extrarlos de la lista, quedándole una lista separada
    dados_guardados = [4,4,4]
    Debe realizar un bucle para recorrer la lista de dados_tirados
    y guardar los "4" en nuestra nueva lista dados_guardados
    Utilie append para ir sumando a dados_guardados los valores

    4) Debe volver a tirar los dados, generar nuevos
    números aleatorios.
    Si en la lista "dados_guardados" tengo 3 dados guardados
    significa que ahora deberé tirar dos dados. Puede usar la función
    "len" para ver cuantos elementos hay en "dados_guardados"
    Es decir que en este caso debería generar dos números
    aleatorios nuevos con "lista_generica"
    Ahora tendré una nueva lista de "dados_tirados" en este caso
    de dos nuevos números aleatorios entre 1 y 6 representando a los dados
    tirados.

    5) Luego de tirar nuevamente los datos, por ejemplo digamos
    que salieron los números: 4-1
    Debo volver a quedarme con el "4" ya que es el número que estoy
    buscando.
    Sino salió el "4" vuelvo a tirar todos los dados.
    Si salió un "4" me lo quedo y lo guardo en "dados_guardados".

    5) Debe repetir este proceso hasta que en su lista de "dados
    guardados" tenga "generala", es decir, 5 números iguales.

    '''
   #------------------comenzar el juego---------------
           
    print('Bienvenido al juego: "La Generala".')
    print('El juego tiene una ronda de tres lanzamientos, suerte!')
    usuario = int(input('Ingresa 1, para comenzar a jugar. \nIngresa 4, para salir del programa.\n'))
    
    while usuario:
                     
        if usuario == 1 :
            print('Comienza el juego, suerte!')

            dados_tirados = funciones_descriptivas.lista_aleatoria(inicio=1, fin=6, cantidad=5)
            print('Resultados {}'.format(dados_tirados))
                              
            numero_repetido = max(dados_tirados, key=dados_tirados.count)
            print('El número más repetido es:', numero_repetido)

            dados_guardados = []

            for i in dados_tirados:
                if i == numero_repetido:
                    dados_guardados.append(i)
                                            
            print('Dados guardados:', dados_guardados)

            evaluando_resultados = funciones_descriptivas.evaluar_dados(dados_guardados)
            if evaluando_resultados == True:
                print('Ganaste!!! Es Generala!')
            else:
                print('Te quedan dos lanzamientos')
                usuario = int(input('Ingresa 2, para continuar el segundo tiro, a jugar!\n Ingresa 4, para salir del programa.\n'))

        if usuario == 2:
            print('Continuamos con el segundo lanzamiento, exitos!')
            
            lista_generica = funciones_descriptivas.lista_aleatoria(inicio=1, fin=6, cantidad=(5 - len(dados_guardados)))        
            print('Resultados {}'.format(lista_generica))

            for i in lista_generica:
                if (i == numero_repetido):
                    dados_guardados.append(i)

            print('Dados guardados:', dados_guardados)
            
            evaluando_resultados = funciones_descriptivas.evaluar_dados(dados_guardados)
            if evaluando_resultados == True:
                print('Ganaste!!! Es Generala!')
            else:
                print('Te queda un lanzamiento')
                usuario = int(input('Ingresa 3, para el último tiro de la ronda.\nIngresa 4, para salir del programa.\n'))       

        if usuario == 3:
            print('Suerte, este es el último lanzamiento!')
            
            lista_generica = funciones_descriptivas.lista_aleatoria(inicio=1, fin=6, cantidad=(5 - len(dados_guardados)))        
            print('Resultados {}'.format(lista_generica))

            for i in lista_generica:
                if (i == numero_repetido):
                    dados_guardados.append(i)

            print('Dados guardados:', dados_guardados)
            
            evaluando_resultados = funciones_descriptivas.evaluar_dados(dados_guardados)
            if evaluando_resultados == True:
                print('Ganaste!!! Es Generala!')
            else:
                print('Perdiste, ha finalizado el juego. Lo siento :-(')
                usuario = int(input('Ingresa 1, para comenzar el juego.\n Ingresa 4, para salir del programa.\n'))
                break
            
        if usuario == 4:
            print('Ha salido del programa, adiós.')
            break
        else: 
            print('El valor ingresado no corresponde con los números indicados. Intente nuevamente')
            continue
            
        

       
            
            
            

        
    
    
    
    
        

        
            
                
                
            
            
                
            

            
                
                

            
                    
                

            
                
                                    
                            
           
if __name__ == '__main__':
    print("Ejercicios de práctica")
    # ej1()
    #ej2()
    #ej3()
    ej4()
