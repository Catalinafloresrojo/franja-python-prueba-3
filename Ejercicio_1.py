#Escribir un programa que escriba 20 numeros aleatorios entre 100 y 1000
#  en un archivo llamado numeros_prueba.txt. 
# Luego debe leer desde el archivo esos números y agregarlos a una lista, 
# modifique o cree una nueva lista que contenga solo los nñumeros impares.
#  Finalmente con numpy determinar la dimensión de la lista.
#  Imprimir por consola la lista final y su dimensión.

import random
import numpy as np

def main (): 
    escribir_archivo()

def escribir_archivo():
    nombre_fichero = "./prueba_3.py/numeros_prueba.txt" 
    with open(nombre_fichero, "w") as file:
        for numero_alateorio in range(1,21):
            numero_alateorio = random.randint(100, 1000)
            print(numero_alateorio)
            file.write (str(numero_alateorio))
            file.write('\n')

def leer_numeros ():

    nombre_fichero = "./prueba_3.py/numeros_prueba" + ".txt"
    numeros = []

    with open (nombre_fichero, "r") as file:
        for linea in file:
            numeros.append(int(linea))

        impar = []
        for n in impar:
            if impar % 2 !=0:
                impar.append(n)
    print(impar)
    vector = np.array (impar)
    print(vector.ndim)
#en mi computaor funcionaba 

if __name__ == '__main__':
    main()