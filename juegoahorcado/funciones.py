"""
1. la palabra a divinar se debe seleccionar aleatoriamente del listado disponible en un archivo de texto.
2 el jugador tendra 5 turnos para adivinar la palabra(independiente si en cada jugada  tiene un acierto o un fallo).
3.En cada turno:
se debe mostrar al usario la actualizacion de la palabra que esta intentndo adivinar y el alfabeto actualizando ( ES decir las letras que se encuentran disponibles)
Se debe preguntar al usuario si desea adivinar la apalabra, y de ser asi realizar la verificacion correspondiente.
4. el juego termina:
Cuando se completan los 5 turnos y el jugador no acierta.
_ El jugador decide adivinar la palabra y acierta.
"""
import random

alfabeto = "a b c d e f g h i j k l m n o p q r s t u v w x y z"


#funcion para escoger una palabra random
def seleccionarpalabra():
  lineas = open("frutas_verduras.txt").readlines()
  palabra = random.choice(lineas).rstrip()
  return palabra


#funcion entrada del teclado
def entradaUsuario():
  letra = input("introduzca una letra:")
  return letra.lower()


#actiualizar jugadas
def actualizarjugadas(palabra, letra, jugada):
  n_letras = len(palabra)
  for i in range(0, n_letras):
    if palabra[i] == letra:
      jugada[i] = letra

  return jugada

#actualizar alfabeto
def actualizarAlfabeto(letra,alfabeto):
  alfabeto = alfabeto.replace(letra," ")
  return alfabeto

#imprimir resultado de la jugada
def imprimirActualizacion(alfabeto,jugada):
  print (f"jugada:{jugada}")
  print (f"letras disponibles: {alfabeto}")

#imprimirActualizacion(alfabeto, jugada)

#verificarjugada
def verificarJugada(suposicion, palabra):
  success = False
  if suposicion == palabra:
    success = True
  return success

#success= verificarJugada("tomate", palabra)
#print (success)