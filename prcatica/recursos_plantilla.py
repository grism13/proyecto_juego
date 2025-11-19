import random

import os

# No tocar 
def clear_screen():
    if os.name == 'nt':  # Check if the operating system is Windows
        os.system('cls')
    else:  # Assume Unix-like (Linux, macOS)
        os.system('clear')
        
"""( descripción del evento que van que van a transcurrir en el def.)"""


#Estas son las sumatorias de los numeros
#Que se suman y restan
delta_oxigeno = 0
delta_combustible = 0
delta_tripulacion = 0
delta_energia = 0
    
print("""(print de que da aviso del evento que esta ocurriendo).
          """)
#alerta del evento de la obstrucuion del filtro
    
    
eleccion = ""

while eleccion != "1" and eleccion != "2" :
        print("""El sitema analizo el problema puedes tomar estas desiciones :
              1) opcion 1
              2) opcion 2
              """)
        
        eleccion = (input("Que disicion tomas tripulante(1 o 2) : "))
        
        clear_screen()
        
        if eleccion == "1" :
             n = random.randint(0 , 1) 
             if n == 0  :
            
              delta_oxigeno = -5 # oxigeno perdido en la reparacion 
              delta_energia = -10 #energia perdida por la soldadura 
              delta_tripulacion = 5 #incremento de moral debido a la buena decision 
              print("tus nivele de oxigeno bajo -5 puntos , la energia en -10 puntos , se añadio 5 puntos de moral ")
              print("""conclusion de la desicion""")
             elif n == 1 :
               delta_oxigeno = -10 # oxigeno perdido en la reparacion 
               delta_energia = -15 #energia perdida por la soldadura 
               delta_tripulacion = 5 #incremento de moral debido a la buena decision 
               print(f"tus nivele de oxigeno bajo -10 puntos , la energia en -15 puntos , se añadio 5 puntos de moral ")
               print("""conclusion de la desicion.""")
        
        elif eleccion == "2" :
              delta_oxigeno = -15 # oxigeno perdido en la desion de ahorro de energia
              delta_tripulacion = -10 #moral perdida por la falta de un nuvo filtro
              print("Bajaron en -15 puntos el oxigeno y bajo -10 puntos la moral") 
              print("""conclusion de la desicion.""")
              
        else :
            print("introdusca bien la eleccion (1 o 2)")


