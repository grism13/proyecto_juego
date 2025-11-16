#inicion de los eventos
import random

def obstrucion_oxigeno() :
    """este es un evento que se caracterisa por una falla en la ventilacion de oxigeno donde 
    los tripulantes tienen que decidir si asumir reparar la falla o esperar a ver que sucede ,
    esto pudiendo afectar al jugar de manera positiva o negativa."""

    delta_oxigeno = 0
    delta_combustible = 0
    delta_tripulacion = 0
    delta_energia = 0
    
    print("""¡ALERTA! Se detecto una un atasco en el filtro de CO2.
          """)
    #alerta del evento de la obstrucuion del filtro
    
    
    eleccion = ""

    while eleccion != "1" and eleccion != "2" :
        print("""El sitema analizo el problema puedes tomar estas desiciones :
              1) Soldar un nuevo filtro de CO2
              2) Esperar a que desatasque solo""")
        
        eleccion = (input("Que disicion tomas tripulante(1 o 2) : "))
        
        if eleccion == 1 :
              delta_oxigeno = -5 # oxigeno perdido en la reparacion 
              delta_energia = -10 #energia perdida por la soldadura 
              delta_tripulacion = 5 #incremento de moral debido a la buena decision 
              print(f"tus nivele de oxigeno bajo -5 puntos , la energia en -10 puntos , se añadio 5 puntos de moral ")
              print("""La masion fue exitosa soldaste el filtro a la perfecion la tripulacion esta contenta 
                    con la desicion que tomaste , Pueden respirar aire fresco.""")
        
        elif eleccion == 2 :
              delta_oxigeno = -15 # oxigeno perdido en la desion de ahorro de energia
              delta_tripulacion = -10 #moral perdida por la falta de un nuvo filtro
              print("Bajaron en -15 puntos el oxigeno y bajo -10 puntos la moral") 
              print("""Apesar de saber soldar el filtro desidiste no hacerlo para ahorrar energia ; lo cual causo 
                    que el aire que respira la tripulacion sea mas denso y bajen los animos debido a la fatiga.""")
              
        else :
            print("introdusca bien la eleccion (1 o 2)")
            
def dow_espacio() :
      
      """este es un evento que se caracterisa por una falla en la chapa ."""

      elta_oxigeno = 0
      delta_combustible = 0
      delta_tripulacion = 0
      delta_energia = 0
    
      print("""¡ALERTA! Se detecto una un atasco en el filtro de CO2.
          """)
    #alerta del evento de la obstrucuion del filtro
    
    
      eleccion = ""

      while eleccion != "1" and eleccion != "2" :
            print("""El sitema analizo el problema puedes tomar estas desiciones :
              1) Soldar un nuevo filtro de CO2
              2) Esperar a que desatasque solo""")
        
            eleccion = (input("Que disicion tomas tripulante(1 o 2) : "))
        
            if eleccion == 1 :
                  delta_oxigeno = -5 # oxigeno perdido en la reparacion 
                  delta_energia = -10 #energia perdida por la soldadura 
                  delta_tripulacion = 5 #incremento de moral debido a la buena decision 
                  print(f"tus nivele de oxigeno bajo -5 puntos , la energia en -10 puntos , se añadio 5 puntos de moral ")
                  print("""La masion fue exitosa soldaste el filtro a la perfecion la tripulacion esta contenta 
                    con la desicion que tomaste , Pueden respirar aire fresco.""")
        
            elif eleccion == 2 :
                  delta_oxigeno = -15 # oxigeno perdido en la desion de ahorro de energia
                  delta_tripulacion = -10 #moral perdida por la falta de un nuvo filtro
                  print("Bajaron en -15 puntos el oxigeno y bajo -10 puntos la moral") 
                  print("""Apesar de saber soldar el filtro desidiste no hacerlo para ahorrar energia ; lo cual causo 
                    que el aire que respira la tripulacion sea mas denso y bajen los animos debido a la fatiga.""")
              
            else :
                  print("introdusca bien la eleccion (1 o 2)")