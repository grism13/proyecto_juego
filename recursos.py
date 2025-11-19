def mostrar_estado_actual(energia, combustible, oxigeno, estado_tripulacion):
    text_energia = f"Energia = {energia}"
    text_combustible = f"Combustible = {combustible}"
    text_oxigeno = f"Oxigeno = {oxigeno}"
    text_tripulacion = f"Estado Tripulacion = {estado_tripulacion}"

    #Aqui esta el print de la animacion
    print(rf"""
    -------------------------->ESTADO ACTUAL DE LA NAVE<-------------------
    
    Energia = {energia}                                   
    Combustible = {combustible}                        
    Oxigeno = {oxigeno}                                 
    Estado Tripulacion= {estado_tripulacion}                
                                                     
         /\
        |==|
       /|()|\
      / |  | \ 
     // |**| \\
""")



#Recursos del video juego
def verificar_derrota (estado_juego, opcion, energia, combustible, oxigeno, estado_tripulacion):
    
    #Verificacion de derrota en modo Facil
    if opcion == "1":
        razon = ""
        num_derrotas = 0

        if energia < 20:
            razon += "\n\n Energia baja\n"
            num_derrotas += 1
        if combustible <= 0:
            razon += " Combustible en 0\n "
            num_derrotas += 1
        if oxigeno < 30:
            razon += "Oxigeno bajo\n " 
            num_derrotas += 1
        if estado_tripulacion < 30:
            razon += "Tripulacion descontenta\n"
            num_derrotas += 1

        if num_derrotas > 0:
            print(f"Has perdido ya que tienes: {razon}")
            estado_juego = "derrota"

        else:
            estado_juego = "victoria"

    #Verificacion de derrota en modo Medio
    elif opcion == "2":
        #Razon indica todas las deficiencias de recursos 
        razon = ""
        #num_derrotas indica numero de veces en las que
        #el usuario comete esas deficiencias
        num_derrotas = 0

        if energia < 40:
            razon += "\n\nEnergia baja\n"
            num_derrotas += 1
        if combustible <= 0:
            razon += "Combustible en 0\n"
            num_derrotas += 1
        if oxigeno < 50:
            razon += "Oxigeno bajo\n"
            num_derrotas += 1 
        if estado_tripulacion < 40:
            razon += "Tripulacion descontenta\n"
            num_derrotas += 1
        
        #Corrobora que el usuario pierda con un contador llamado
        #num_derrotas (Si es mayor a 0) se marca derrota
        if num_derrotas > 0:
            print(f"Has perdido ya que tienes: {razon}")
            estado_juego = "derrota"
        
        else:
            estado_juego = "victoria"


    #Verificacion de derrota en modo Dificil
    elif opcion == "3":
        razon = ""
        num_derrotas = 0

        if energia < 60:
            razon += "\n\nEnergia baja\n"
            num_derrotas += 1
        if combustible <= 0:
            razon += "Combustible en 0\n"
            num_derrotas += 1
        if oxigeno < 70:
            razon += "Oxigeno bajo\n"
            num_derrotas += 1 
        if estado_tripulacion < 50:
            razon += "Tripulacion descontenta\n"
            num_derrotas += 1
        
        if num_derrotas > 0:
            print(f"Has perdido ya que tienes: {razon}")
            estado_juego = "derrota"
        else:
            estado_juego = "victoria"


