def mostrar_estado_actual(energia, combustible, oxigeno, estado_de_tripulacion):
    text_energia = f"Energia = {energia}"
    text_combustible = f"Combustible = {combustible}"
    text_oxigeno = f"Oxigeno = {oxigeno}"
    text_tripulacion = f"Estado Tripulacion = {estado_de_tripulacion}"

    #Aqui esta el print de la animacion
    print(rf"""
    -------------------------->ESTADO ACTUAL DE LA NAVE<-------------------
    
    Energia = {energia}                                   
    Combustible = {combustible}                        
    Oxigeno = {oxigeno}                                 
    Estado Tripulacion= {estado_de_tripulacion}                
                                                     
         /\
        |==|
       /|()|\
      / |  | \ 
     // |**| \\
""")



#Recursos del video juego
def verificar_derrota (opcion, energia, combustible, oxigeno, estado_de_tripulacion):
    
    #Verificacion de derrota en modo Facil
    if opcion == 1:
        razon = ""
        if energia < 20:
            razon += "\n\n Energia baja\n"
        if combustible <= 0:
            razon += " Combustible en 0\n "
        if oxigeno < 30:
            razon += "Oxigeno bajo\n " 
        if estado_de_tripulacion < 30:
            razon += "Tripulacion descontenta\n"
        else:
            return jugar
        
        print(f"Has perdido ya que tienes: {razon}")
    
    #Verificacion de derrota en modo Medio
    elif opcion == 2:
        razon = ""
        if energia < 40:
            razon += "\n\nEnergia baja\n"
        if combustible <= 0:
            razon += "Combustible en 0\n"
        if oxigeno < 50:
            razon += "Oxigeno bajo\n" 
        if estado_de_tripulacion < 40:
            razon += "Tripulacion descontenta\n"
        else:
            return jugar
        
        print(f"Has perdido ya que tienes: {razon}")

    #Verificacion de derrota en modo Dificil
    elif opcion == 3:
        razon = ""
        if energia < 60:
            razon += "\n\nEnergia baja\n"
        if combustible <= 0:
            razon += "Combustible en 0\n"
        if oxigeno < 70:
            razon += "Oxigeno bajo\n" 
        if estado_de_tripulacion < 50:
            razon += "Tripulacion descontenta\n"
        else:
            return jugar
        
        print(f"Has perdido ya que tienes: {razon}")


