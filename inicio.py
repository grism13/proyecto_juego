
"""este es un evento que se caracterisa por una falla en la ventilacion de oxigeno donde 
los tripulantes tienen que decidir si asumir reparar la falla o esperar a ver que sucede ,
esto pudiendo afectar al jugar de manera positiva o negativa."""

delta_oxigeno = 0
delta_combustible = 0
delta_moral = 0
delta_energia = 0
    
print("""¡ALERTA! Se detecto una un atasco en el filtro de CO2 , se estaca el aire.
""")
#alerta del evento de la obstrucuion del filtro
eleccion = ""

while eleccion != "1" and eleccion != "2" :
        
    eleccion = (input("joa"))
    
    if eleccion == "1" :
        print ("me gusta")
    elif eleccion == "2" :
        print("pene")
    else :
        print("me gusta el bicho")