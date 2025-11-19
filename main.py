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
        
        # Obtenemos los valores iniciales y la dificultad del módulo 'inicio'
        inicio.mostrar_introduccion()
        energia, combustible, oxigeno, estado_tripulacion , opcion = inicio.obtener_recursos_iniciales()
        
        dia_actual = 1
        estado_juego = "jugando" 
        # Estado puede ser "jugando", "derrota", "victoria", este cambia cuando se determine la victoria o derrota del juego

        # BUCLE PRINCIPAL DE LA PARTIDA
        while estado_juego == "jugando":
            
            # Mostrar el estado actual
            recursos.mostrar_estado_actual(energia, combustible, oxigeno, estado_tripulacion)
            
            # Pausa para el jugador
            input(f"\n--- Presiona ENTER para avanzar al Día {dia_actual}---")
            
            # eventos nos devuelve los deltas, que son los cambios que ocurren en los recursos
            delta_oxigeno, delta_combustible, delta_enegía, delta_tripulacion = eventos.seleccionar_y_manejar_evento(dia_actual)
            
            # Aplicamos los cambios (deltas) a nuestras variables principales
            energia += delta_enegía
            combustible += delta_combustible
            oxigeno += delta_oxigeno
            estado_tripulacion += delta_tripulacion
            
            """#  Limitar recursos (no pueden pasar de 100)
            energia, combustible, oxigeno, estado_tripulción = recursos.limitar_recursos(energia, combustible, oxigeno, estado_tripulacion)   NO TOCAR POR AHORA""" 
            
            estado_juego = recursos.verificar_derrota(energia, combustible, oxigeno, estado_tripulacion)
            
            if estado_juego == "derrota":
                break # Sale del bucle de partida

            # 6. REVISAR CONDICIÓN DE VICTORIA (Último día)
            elif estado_juego == "victoria":
                
                break # Sale del bucle de partida
            
            # 7. AVANZAR AL SIGUIENTE DÍA
            dia_actual += 1
            
        
        # El bucle de partida terminó (por victoria o derrota)
        final.mostrar_resultado(estado_juego, energia, combustible, oxigeno, estado_tripulacion)
        
        
        jugar_de_nuevo = final.preguntar_reinicio()

    # Mensaje de despedida final
    print("\nGracias por jugar nuestro juego de mierda: 'Salvando al Bastardo'. Fin de la simulación.")

# --- Punto de entrada ---
# Esta línea asegura que la función main() se llame solo
# cuando se ejecuta este archivo directamente.
if __name__ == "__main__":
    main()


    # asi es por ahora, las variables se establecieron en whiteboard de discord profe, la ia nos dio los algoritmos y estableció la lógica, nosotros solo sufrimos y fallabamos a cada rato

    # ya aqui terminamos de estructurar teniendo todos los modulos listos