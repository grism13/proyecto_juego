# inicio,mostramos un buen encabezado para el final del juego,
print(
    """=================
  FIN DEL JUEGO
================="""
)

# ahora comprobamos el estado del juego


def final_juego(estado_juego):
    if estado_juego == "victoria":
        print("🎉 ¡VICTORIA! Cumpliste tu objetivo, felicidades :)")
        
    elif estado_juego == "derrota":
        print("😢 ¡DERROTA! No lograste cumplir el objetivo, ¡inténtalo de nuevo! :(")

def mostrar_resultado(estado_juego, energia, combustible, oxigeno, estado_tripulacion):
    # Llama a final_juego para mostrar el mensaje de victoria/derrota
    final_juego(estado_juego)
    
    # ahora se muestra el reporte final de los recursos
    print(
        f"""\n--- Reporte final de la partida ---
    Energia: {energia}% 
    Combustible: {combustible}% 
    Oxigeno: {oxigeno}%
    Estado de la tripulación: {estado_tripulacion}% 
    Estado de la tripulación: {estado_tripulacion}% 
    ----------------------------------"""
    )

# ahora se pregunta si quieren jugar de nuevo
def preguntar_reinicio():
    eleccion = ""
    jugar_de_nuevo = False # Valor inicial a retornar

    while eleccion != "1" and eleccion != "2":
        print(
            """\n¿Deseas Reiniciar e intentarlo de nuevo?
        Introduce 1 para sí y 2 para no """
        )

        eleccion = input("¿Deseas Reiniciar?: ")

        if eleccion == "1":
            print("\nReiniciando partida, suerte en tu nueva aventura...")
            jugar_de_nuevo = True
            break

        elif eleccion == "2":
            break

        else:
            print("ERROR, comando no reconocido. Por favor, ingresa 1 o 2")
            
    return jugar_de_nuevo

# Nota: Se comenta la llamada para que se ejecute solo desde main.py
# preguntar_reinicio() 


# fin del final xd