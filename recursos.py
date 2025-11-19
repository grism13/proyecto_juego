def mostrar_estado_actual(energia, combustible, oxigeno, estado_tripulacion):
    text_energia = f"Energia = {energia}"
    text_combustible = f"Combustible = {combustible}"
    text_oxigeno = f"Oxigeno = {oxigeno}"
    text_tripulacion = f"Estado Tripulacion = {estado_tripulacion}"

    #Aqui esta el print de la animacion
    print(rf"""
    -------------------------->ESTADO ACTUAL DE LA NAVE<-------------------
    
    Energia = {energia}%                                   
    Combustible = {combustible}%                        
    Oxigeno = {oxigeno}%                                 
    Estado Tripulacion= {estado_tripulacion}%                
                                                     
         /\
        |==|
       /|()|\
      / |  | \ 
     // |**| \\
    """)

    return energia, combustible, oxigeno, estado_tripulacion  

def limitar_recursos(energia, combustible, oxigeno, estado_tripulacion):
    # Los recursos no pueden pasar de 100
    if energia > 100:
        energia = 100
    if combustible > 100:
        combustible = 100
    if oxigeno > 100:
        oxigeno = 100
    if estado_tripulacion > 100:
        estado_tripulacion = 100
        
    # Combustible no puede ser negativo
    if combustible < 0:
        combustible = 0

    return energia, combustible, oxigeno, estado_tripulacion

#Recursos del video juego
def verificar_derrota (dia_actual, dias_totales_mision, opcion, energia, combustible, oxigeno, estado_tripulacion):
    
    estado_juego = "jugando" # Estado por defecto

    # Definir umbrales de DEFECCIÓN (derrota inmediata) y UMBRALES DE VICTORIA/DERROTA FINAL
    
    # Derrota Inmediata (Cualquier recurso <= 0) - Regla 6 del README
    if energia <= 0 or combustible <= 0 or oxigeno <= 0 or estado_tripulacion <= 0:
        print("\n¡ALERTA MÁXIMA! ¡Un recurso ha llegado a 0! ")
        
        if energia <= 0:
            print("❌ ENERGÍA AGOTADA: Los sistemas de soporte vital fallan.")
        if combustible <= 0:
            print("❌ COMBUSTIBLE AGOTADO: La nave está a la deriva en el vacío.")
        if oxigeno <= 0:
            print("❌ OXÍGENO AGOTADO: Asfixia inminente.")
        if estado_tripulacion <= 0:
            print("❌ ESTADO DE LA TRIPULACIÓN EN CERO: El Comandante y los Downs han colapsado.")

        estado_juego = "derrota"
        return estado_juego

    # --------------------------------------------------------------------------------------
    # LÓGICA DE DERROTA POR RECURSOS BAJOS (Durante el juego o Derrota Final)
    # --------------------------------------------------------------------------------------

    # Umbrales basados en la lógica de 'verificar_derrota' del código original 
    # (Usaremos estos para la DEFECCIÓN POR RECURSOS BAJOS)
    
    umbral_energia_baja = 0
    umbral_oxigeno_bajo = 0
    umbral_tripulacion_baja = 0
    
    if opcion == "1": # Fácil
        umbral_energia_baja = 20
        umbral_oxigeno_bajo = 30
        umbral_tripulacion_baja = 30
    elif opcion == "2": # Medio
        umbral_energia_baja = 40
        umbral_oxigeno_bajo = 50
        umbral_tripulacion_baja = 40
    elif opcion == "3": # Difícil
        umbral_energia_baja = 60
        umbral_oxigeno_bajo = 70
        umbral_tripulacion_baja = 50
        
    # Se añade el umbral de combustible <= 0 ya verificado, solo para mostrar la razón
    
    razon = ""
    num_deficiencias = 0

    if energia < umbral_energia_baja:
        razon += "\n Energia baja"
        num_deficiencias += 1
    # Nota: Combustible <= 0 es una derrota automática ya verificada arriba
    if oxigeno < umbral_oxigeno_bajo:
        razon += "\n Oxigeno bajo" 
        num_deficiencias += 1
    if estado_tripulacion < umbral_tripulacion_baja:
        razon += "\n Tripulacion descontenta"
        num_deficiencias += 1
        
    # --------------------------------------------------------------------------------------
    # LÓGICA FINAL (Día 8)
    # --------------------------------------------------------------------------------------
    
    if dia_actual == dias_totales_mision:
        
        print("\n--- ¡LLEGADA A GARIMÉ! Verificando estado final de la nave... ---")

        # Verifica si cumple con *todas* las condiciones mínimas del nivel (Derrota Final)
        # La lógica se invierte: si hay deficiencias, es derrota.
        
        if num_deficiencias > 0:
            print(f"\n❌ DERROTA FINAL: Llegaste a Garimé, pero tus recursos son insuficientes. Faltó: {razon}")
            estado_juego = "derrota"
        
        # El combustible siempre debe ser > 0, lo cual ya se maneja en la derrota inmediata.
        
        else:
            print("\n🎉 ¡CONDICIONES CUMPLIDAS! Tienes recursos suficientes para el asentamiento.")
            estado_juego = "victoria"

    # Si no es el último día, y no hay derrota inmediata, se sigue jugando
    return estado_juego