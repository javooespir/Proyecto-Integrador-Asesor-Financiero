#Comienzo del proyecto
'''Ejercicio Integrador Python Inicial
Autor: Javier Espir
Descripcion: El programa funciona como un asesor financiero dependiendo del tipo de inversion que se quiera realizar. En donde se consultara con el usario ciertas caracteristicas para definir el tipo de inversor en caso de no tener experiencia. En el caso de tenerla, se aportan diferentes opciones o sugerencias de inversiones.
En el programa se utilizan:
    - Variables
    - Condicionales
    - Bucles
    - Funciones
    - Manejo de listas
    - Manejo de archivos CSV'''

import csv
from typing import final
import auxiliares

def bienvenida(): 
    # La funcion se encarga de mostrar en pantalla como interactuar con el programa
    print("\n"
    "Bienvenido a Javito's, tu nuevo Asesor Financiero"
    "\nPor favor, ingrese a continuación la opcion que corresponda: ")
    return perfil()

    

def perfil():
    #segun el conocimiento del usuario, se dervia a las partes del programa
    print('Tiene experiencia en Inversiones?',
          "\n1: Ninguna",
          "\n2: Poca",
          "\n3: Algun Conocimiento"
          "\n4: Mucha",)
    while True:
        try:
            opcion_1 = int(input('Eliga una opcion:' (1,2,3,4)))
            break
        except:
            print("Por favor, vuelva a intentar e ingrese alguna de las opciones")
            return bienvenida          
    if type (opcion_1) == int:
        if opcion_1 == 1:
                conocer_perfil()  # Funcion de preguntas de perfil

        elif opcion_1 == 2:
                conocer_perfil()  # Funcion de preguntas de perfil

        elif opcion_1 == 3:
                conocer_perfil()  # Funcion de preguntas de perfil

        elif opcion_1 == 4:
               opciones_inversion()  # Opciones para invertir
        else:
            print("Por favor, vuelva a intentar e ingrese alguna de las opciones")
            return bienvenida
    else:
        print("Por favor, vuelva a intentar e ingrese alguna de las opciones")
        return bienvenida
    


def conocer_perfil():
    print("Por favor, para definir el tipo de perfil de inversion que desea, responda las siguientes preguntas eligiendo la opcion que corresponda: ",
          "\n1) ¿Cuál es el plazo que planteas para invertir?",
          "\na) Entre uno y cinco años",
          "\nb) Entre cinco y diez años",
          "\nc) Más de 10 años")
    Respuestas = []
    while True:
        try:
            pregunta_1 = str(input('a', 'b','c'))
            break
        except: 
            print("No ha ingresado un ninguna de las opciones de la pregunta 1, vuelva a intentar")
            return conocer_perfil()

            

    print("\n2) ¿Qué porcentaje de tus ahorros invertirías?",
          "\na) Menos del 30%",
          "\nb) Entre un 30 y un 60%",
          "\nc) Más del 60%")
    
    while True:
        try:
            pregunta_2 = str(input('a', 'b', 'c'))
            break
        except:
            print(
                "No ha ingresado un ninguna de las opciones de la pregunta 1, vuelva a intentar")
            return conocer_perfil()

    print("\n3) ¿Con qué te sientes más identificado?",
          "\na) Prefiero obtener una rentabilidad reducida pero que mi dinero esté garantizado",
          "\nb) Estoy dispuesto a asumir algo de riesgo a cambio de una mejor rentabilidad",
          "\nc) Busco la máxima rentabilidad. Quien no arriesga no gana")
    while True:
        try:
            pregunta_3 = str(input('a', 'b', 'c'))
            break
        except:
            print(
                "No ha ingresado un ninguna de las opciones de la pregunta 1, vuelva a intentar")
            return conocer_perfil()


    print("\n4) ¿Qué te suscita la palabra «riesgo»?",
          "\na) Pérdida",
          "\nb) Inseguridad",
          "\nc) Oportunidad")
    while True:
        try:
            pregunta_4 = str(input('a', 'b', 'c'))
            break
        except:
            print(
                "No ha ingresado un ninguna de las opciones de la pregunta 1, vuelva a intentar")
            return conocer_perfil()

    if pregunta_1 == 'a':
        Respuestas.append(pregunta_1)
    elif pregunta_1 == 'b':
        Respuestas.append(pregunta_1)
    elif pregunta_1 == 'c':
        Respuestas.append(pregunta_1)
    else:
        print(
            "No ha ingresado un ninguna de las opciones de la pregunta 1, vuelva a intentar")
        return conocer_perfil()

    if pregunta_2 == 'a':
        Respuestas.append(pregunta_2)
    elif pregunta_2 == 'b':
        Respuestas.append(pregunta_2)
    elif pregunta_2 == 'c':
        Respuestas.append(pregunta_2)
    else:
        print(
            "No ha ingresado un ninguna de las opciones de la pregunta 2, vuelva a intentar")
        return conocer_perfil()

    if pregunta_3 == 'a':
        Respuestas.append(pregunta_3)
    elif pregunta_3 == 'b':
        Respuestas.append(pregunta_3)
    elif pregunta_3 == 'c':
        Respuestas.append(pregunta_3)
    else:
        print(
            "No ha ingresado un ninguna de las opciones de la pregunta 3, vuelva a intentar")
        return conocer_perfil()

    if pregunta_4 == 'a':
        Respuestas.append(pregunta_4)
    elif pregunta_4 == 'b':
        Respuestas.append(pregunta_4)
    elif pregunta_4 == 'c':
        Respuestas.append(pregunta_4)
    else:
        print(
            "No ha ingresado un ninguna de las opciones de la pregunta 4, vuelva a intentar")
        return conocer_perfil()

    total_a = Respuestas.count('a')
    total_b = Respuestas.count('b')
    total_c = Respuestas.count('c')
    if total_c <= total_a and total_a >= total_b:     # de esta manera siempre priorizo que la respuesta sea CONSERVADOR para no arriesgar los fondos del usuario
        print("Su perfil es: CONSERVADOR. Claramente, tu perfil de inversor es conservador si valoras la seguridad por encima de la rentabilidad. Eres más afín a productos de ahorro que garanticen tu dinero como las cuentas de ahorro y los depósitos bancarios o productos de inversión que inviertan en renta fija. Infórmate siempre antes de elegir un producto de inversión.")
        print("Felicidades, su perfil esta definido como CONSERVADOR. Estas son sus recomendaciones de inversión: ")
        auxiliares.divisas()
        auxiliares.bonos()
    elif total_c <= total_b > total_a:  # de esta manera siempre priorizo que la respuesta sea MODERADO para no arriesgar los fondos del usuario
        print("Su perfil es: MODERADO. Buscas un crecimiento de tus ahorros y estás dispuesto a asumir algo de riesgo. Contemplas la posibilidad de invertir en productos como los planes de pensiones o fondos de inversión con un porcentaje equilibrado o acorde a tu aversión al riesgo en activos de renta fija y variable. Antes de invertir, fíjate en quién gestiona el producto, las comisiones y en qué estás invirtiendo.")
        print("Felicidades, su perfil esta definido como MODERADO. Estas son sus recomendaciones de inversión: ")
        auxiliares.etf(),
        auxiliares.materia_prima()
    elif total_a < total_c > total_b:
        print("Su perfil es: AGRESIVO. Quieres aumentar tu patrimonio al máximo y estás dispuesto a invertir a largo plazo asumiendo el riesgo necesario para ello. Entiendes el riesgo que conlleva invertir, el mercado y el funcionamiento de las herramientas de inversión. Este tipo de perfil suele invertir con un mayor porcentaje de la inversión en activos de renta variable.")
        print("Felicidades, su perfil esta definido como AGRESIVO. Estas son sus recomendaciones de inversión: ")
        auxiliares.acciones()
        auxiliares.cryptomonedas()
    finalizacion()



def seleccion_inversiones(numero):
    # Con el numero ingresado por el usuario, se ingresa de acuerdo a la condicion que cumple.

    if numero == 1:
        auxiliares.acciones()
    elif numero == 2:
        auxiliares.divisas()
    elif numero == 3:
        auxiliares.etf()
    elif numero == 4:
       auxiliares.bonos()
    elif numero == 5:
        auxiliares.cryptomonedas()
    elif numero == 6:
        auxiliares.materia_prima()
    else:
        print("Vuelva a intentar",
        "\n")
        bienvenida()
    finalizacion()


def opciones_inversion():
    print("En que desea Invertir?",
          "\n1: Acciones",
          "\n2: Divisas",
          "\n3: ETF"
          "\n4: Bonos",
          "\n5: Cryptomonedas",
          "\n6: Materia Prima")    
    while True:
     try:
         numero = int(input("Ingrese la opcion que desee: "))
         seleccion_inversiones(numero)
         break
     except ValueError:
         print("No ha ingresado un numero de las opciones, vuelva a intentar")


def finalizacion():
    print("Gracias por confiar en nosotros. ",
          "\n¿Desea salir o volver al inicio?",
          "\n1: Salir.",
          "\n2: Inicio.")
    finalizar = int(input())
    while True:
        try:
            if finalizar == 1:
                print('Adios!')
                quit()
                break
            elif finalizar == 2:
                bienvenida()
        except ValueError:
            print("Por favor, ingrese las opciones 1 o 2")
            return finalizacion()


if __name__ == "__main__":
    bienvenida()
    perfil()
    finalizacion()