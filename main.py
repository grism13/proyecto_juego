import inicio
import eventos
import recursos
import final

# total de dias y eventos que tendrá el usuario
DIAS_TOTALES_MISION = 8
# El juego durará 8 turnos (días)

def main():

    jugar_de_nuevo = True
    while jugar_de_nuevo:
        
        # 1. INICIO DEL JUEGO
        
        # Obtenemos los valores iniciales y la dificultad del módulo 'inicio'
        inicio.texto_introduccion()
        inicio.comienzo_juego()

        # Corregido: seleccionar_dificultad ahora retorna 5 valores (incluyendo opcion)
        energia, combustible, oxigeno, estado_tripulacion, opcion = inicio.seleccionar_dificultad()
        
        dia_actual = 1
        estado_juego = "jugando" 
        # Estado puede ser "jugando", "derrota", "victoria"
        
        # Para evitar el error en la primera llamada de mostrar_resultado
        # (aunque en la versión corregida de final.py esto no es tan crítico)
        final.final_juego(estado_juego) 

        # 2. BUCLE PRINCIPAL DE LA PARTIDA
        while estado_juego == "jugando":
            
            # 2a. Mostrar el estado actual
            recursos.mostrar_estado_actual(energia, combustible, oxigeno, estado_tripulacion)
            
            # 2b. Pausa para el jugador
            input(f"\n--- Presiona ENTER para avanzar al Día {dia_actual} de {DIAS_TOTALES_MISION} ---")
            
            
            # 'eventos' nos devuelve los *cambios* (deltas)
            delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion = eventos.seleccionar_y_manejar_evento(dia_actual, DIAS_TOTALES_MISION)
            
            # 3. Aplicamos los cambios (deltas) a nuestras variables principales
            energia += delta_energia
            combustible += delta_combustible
            oxigeno += delta_oxigeno
            estado_tripulacion += delta_tripulacion
            
            # 4a. Limitar recursos (no pueden pasar de 100 ni ser negativos)
            energia, combustible, oxigeno, estado_tripulacion = recursos.limitar_recursos(energia, combustible, oxigeno, estado_tripulacion)
            
            # 5. REVISAR CONDICIÓN DE DERROTA/VICTORIA
            # Corregido: enviar todos los argumentos necesarios
            estado_juego = recursos.verificar_derrota(dia_actual, DIAS_TOTALES_MISION, opcion, energia, combustible, oxigeno, estado_tripulacion)
            
            # Si el estado_juego ya ha cambiado a "derrota" o "victoria"
            if estado_juego != "jugando":
                recursos.mostrar_estado_actual(energia, combustible, oxigeno, estado_tripulacion) # Mostrar estado final
                break # Sale del bucle de partida
            
            # 6. AVANZAR AL SIGUIENTE DÍA
            dia_actual += 1
            
        
        # 7. FIN DE PARTIDA
        # Corregido: llamar a mostrar_resultado con el estado_juego y los recursos finales
        final.mostrar_resultado(estado_juego, energia, combustible, oxigeno, estado_tripulacion)
        
        # 8. PREGUNTAR REINICIO
        jugar_de_nuevo = final.preguntar_reinicio()

    # Mensaje de despedida final
    print("\nGracias por jugar 'Salvando al Bastardo'. Fin de la simulación.")

# --- Punto de entrada ---
if __name__ == "__main__":
    main()