from funciones import *


def main():
  palabra = seleccionarpalabra()
  alfabeto = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
  jugada = ["_"] * len(palabra)
  #seleccionar palabra e inicializar el alfabeto y jugada
  for turno in range(5):
    print(f'\nTurno: {turno+1}')
    print("_" * 20)
    #imprimir alfabeto y jugada
    imprimirActualizacion(alfabeto, jugada)
    #entrada usuario
    letra = entradaUsuario()
    #actualizar jugada y alfabeto
    jugada = actualizarjugadas(palabra, letra, jugada)
    alfabeto = actualizarAlfabeto(letra, alfabeto)
    #imprimir actiualizacion
    imprimirActualizacion(alfabeto, jugada)
    #preguntar si desea adivinar o no la palabra
    check = input("desea adivinar la palabra? (s/n")
    if check.lower() == "s":
      suposicion = input("introduzca su respuesta: ").lower()
      success = verificarJugada(suposicion, palabra)
      if success:
        print("+" * 20)
        print("SIUUU GANOO")
        print("+" * 20)
        break
      else:
        print("+" * 20)
        print("la suposicion  es incorrecta...")
        print("+" * 20)
    if turno == 4:
      print("-" * 20)
      print(":( :( horcado")
      print("-" * 20)


if __name__=="__main__":
  main()
