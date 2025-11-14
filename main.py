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
        energia, comb, oxigeno, estado_tripulacion , dificultad = inicio.obtener_recursos_iniciales()
        
        dia_actual = 1
        estado_juego = "jugando" 
        # Estado puede ser "jugando", "derrota", "victoria"

        # 2. BUCLE PRINCIPAL DE LA PARTIDA
        while estado_juego == "jugando":
            
            # 2a. Mostrar el estado actual
            recursos.mostrar_estado_actual(energia, comb, oxigeno, moral, integ)
            
            # 2b. Pausa para el jugador
            input(f"\n--- Presiona ENTER para avanzar al Día {dia_actual} de {DIAS_TOTALES_MISION} ---")
            
            
            # 'eventos' nos devuelve los *cambios* (deltas)
            d_e, d_c, d_o, d_m, d_i = eventos.seleccionar_y_manejar_evento(dia_actual)
            
            # Aplicamos los cambios (deltas) a nuestras variables principales
            energia += d_e
            comb += d_c
            oxigeno += d_o
            moral += d_m
            integ += d_i
            
            # 4b. Limitar recursos (no pueden pasar de 100)
            energia, comb, oxigeno, moral, integ = recursos.limitar_recursos(energia, comb, oxigeno, moral, integ)
            
            estado_juego = recursos.verificar_derrota(energia, comb, oxigeno, moral, integ)
            
            if estado_juego == "derrota":
                break # Sale del bucle de partida

            # 6. REVISAR CONDICIÓN DE VICTORIA (Último día)
            if dia_actual >= DIAS_TOTALES_MISION:
                estado_juego = recursos.verificar_victoria_final(energia, moral, integ, dificultad)
                break # Sale del bucle de partida
            
            # 7. AVANZAR AL SIGUIENTE DÍA
            dia_actual += 1
            
        
        # El bucle de partida terminó (por victoria o derrota)
        final.mostrar_resultado(estado_juego, energia, comb, oxigeno, moral, integ)
        
        
        jugar_de_nuevo = final.preguntar_reinicio()

    # Mensaje de despedida final
    print("\nGracias por jugar 'Salvando al Bastardo'. Fin de la simulación.")

# --- Punto de entrada ---
# Esta línea asegura que la función main() se llame solo
# cuando se ejecuta este archivo directamente.
if __name__ == "__main__":
    main()


    # asi es por ahora, las variables se establecieron en whiteboard de discord profe, la ia nos dio los algoritmos y estableció la lógica, nosotros solo sufrimos y fallabamos a cada rato