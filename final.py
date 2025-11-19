# inicio,mostramos un buen encabezado para el final del juego,
print(
    """=================
  FIN DEL JUEGO
================="""
)

# ahora comprobamos el estado del juego

def final_juego(estado_juego):
    if estado_juego == "victoria":
        print("VICTORIA, cumpliste tu objetivo felicidades :)")
        
    elif estado_juego == "derrota":
        print("DERROTA, no lograste cumplir el objetivo, intentalo de nuevo :(")

def mostrar_resultado(energia,combustible,oxigeno,estado_tripulacion):
    # ahora se muestra el reporte final de los recursos
    print(
        f"""Reporte final de la partida
    Energia: {energia}% 
    Combustible: {combustible}% 
    Oxigeno: {oxigeno}%
    Estado de la tripulación: {estado_tripulacion}% 
    ----------------------------------"""
    )

# ahora se pregunta si quieren jugar de nuevo
def preguntar_reinicio():
    eleccion = ""

    while eleccion != 1 and eleccion != 2:
        print(
            """¿Deseas Reiniciar e intentarlo de nuevo?
        Introduce 1 para si y 2 para no """
        )

        eleccion = input("¿Deseas Reiniciar?: ")

        if eleccion == "1":
            print("Reiniciando partida, suerte en tu nueva aventura")
            return True

        elif eleccion == "2":
            return False

        else:
            print("ERROR, comando no reconocido. Por favor, ingresa 1 o 2")

        if preguntar_reinicio == True:
            print("El juego se reiniciara")

        else:
            print("Gracias por jugar, adios...")

preguntar_reinicio()




# fin del final xd