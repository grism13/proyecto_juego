import random
import os

"""esto lo usamos para limpiar el terminal cuando sea pertinente:)"""
def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

# primero colocamos todos los eventos, eventos fijos y eventos aleatorios

"""evento fijo del dia 1"""
def evento_inicio_bastardo():
    print("""
        "\n¡ALARMA! ¡ALARMA! ...o eso intentó la alarma.
    El sistema de altavoces emite un sonido patético, como un pollo.
    Ahora estás en la nave, bienvenid@. Los sistemas están... ¿funcionando? Más o menos.
    El comandante peruano ya está buscando su primera botella del día, para tu mala suerte no la consigue.
    La tripulación Down te saluda alegremente, ajena al peligro, porque bueno... Son downs.
          """)
    print("Nota: te bajamos -10 puntos en estado de tripulación porque el comandante no consiguió la botella")
    delta_energia = 0
    delta_combustible = 0 
    delta_oxigeno = 0 
    delta_tripulacion = -10  

    return delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion
    #estas deltas se restarán directamente con las variables de recursos principal

"""evento fijo dia final"""
def evento_final_llegada_garime():
    print("¡IA, ES ESO! ¡'GARIMÉ'!")
    print("El planeta se ve... polvoriento. Y huele raro desde aquí.")
    print("El Comandante está llorando. O sudando Pisco. No estás segura.")
    print("Iniciando protocolos de descenso...")

    
    delta_energia = 0
    delta_combustible = 0  
    delta_oxigeno = 0 
    delta_tripulacion = 0
    
    return delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion

"""eventos alatorios"""

def evento_filtro_inka_kola():

    #definicion de variables 
    delta_energia = 0
    delta_oxigeno = 0
    delta_tripulacion = 0
    delta_combustible = 0
    eleccion = ""

    print("""
    ¡Alerta IA! Un microbio alienígena está en el filtro de O2.
    El Comandante insiste en que la Inka Kola que trajo es el antídoto.
    """)
    
    while eleccion != "1" and eleccion != "2":
        print(rf"""
        Opciones:
        1. Purgar el filtro con la Inka Kola.
        2. Gastar energía para incinerar el filtro.     
    """)
        eleccion = input("Ayuda al peruanito a decidir (1 o 2): ")
    
    # Aqui es donde se verifica la eficacia de las opciones
    if eleccion == "1":
        print("Purgando con líquido dorado...")
        resultado = random.randint(1, 100)
        # 50% de magen de error
        if resultado <= 50:
            print("""
        ¡COMPLICACIÓN! ¡El azúcar se caramelizó y atascó todo!
        El motor del filtro ahora gasta energía extra para compensar, bajaron los niveles de energia, oxigeno y tripulacion
        """)
            delta_energia += -10
            delta_oxigeno += -10
            delta_tripulacion += -10
        else:
            print("""
        ¡MILAGRO! El azúcar carbonatada neutraliza el microbio.
        El aire huele a chicle. La tripulación está feliz, ha subido el oxigeno y el estado de la tripulacion.
        """)
            delta_oxigeno += +15
            delta_tripulacion += +10

    # Verificacion 2
    elif eleccion == "2":
        print("""
        Incinerando el filtro. Es la opción aburrida, pero funciona. bajaron los niveles de energia y el estado de la tripulacion
        """)
        delta_energia += -15
        delta_tripulacion += -5
    
    # Retorna los valores
    return delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion

def evento_maniobra_mototaxi():    
    delta_energia = 0
    delta_combustible = 0
    delta_oxigeno = 0
    delta_tripulacion = 0
    eleccion = ""

    print("""
    ¡Campo de asteroides denso! El piloto automático no puede calcularlo.
    El Comandante grita: '¡Saca esa IA de lentos! ¡Yo manejo!'
    """)
    
    while eleccion != "1" and eleccion != "2":
        print("""
        Opciones:
        1. Ceder el control al Comandante.
        2. Usar la ruta larga y segura.
        """)
        eleccion = input("Ayuda al peruanito a decidir (1 o 2):")

        if eleccion == "1":
            print("El Comandante toma los controles...")
            resultado = random.randint(1, 100)
            
            # 50% Error
            if resultado <= 50: 
                print("¡COMPLICACIÓN! ¡tu nave tiene la culpa!")
                print("Intenta cerrar a un asteroide. La maniobra gasta más combustible.")
                
                delta_combustible += -15
                delta_tripulacion += -10
            
            # 50% Éxito 
            else: 
                print("¡A lo Rápidos y Furiosos: Reto Garimé!")
                print("Esquiva todo, ahorra combustible y la tripulación vitorea.")
                
                delta_combustible += -5 # Ahorro de combustible relativo
                delta_tripulacion += +15
        
        elif eleccion == "2":
            print("Rodeando el campo... qué aburrido. Y qué gasto de combustible.")
            
            delta_combustible += -25 # Penalización segura
            
        else:
            print("Error: Comando no válido.")

            
    # Retorna los valores de delta
    return delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion

def evento_papa_espacial():
    
    delta_energia = 0
    delta_combustible = 0 
    delta_oxigeno = 0
    delta_tripulacion = 0
    eleccion = ""

    print("""
    ¡Alerta! La tripulación te informa que iniciarán el 'Protocolo Papa'.
    Quieren usar el panel de navegación porque es tibio como sembradío. (cosas de down)
    """)
    
    while eleccion != "1" and eleccion != "2":
        print("""
        Opciones de la IA:
        1. ¡Por la ciencia! Permitir el cultivo (Afecta O2 y Energía, aumenta estado de la tripulacion).
        2. Confiscar las papas (La tripulación se amotina, baja el estado de la tripulacion).
        """)
        eleccion = input("Ayuda al peruanito a decidir (1 o 2):")

        if eleccion == "1":
            print("""
            El panel de navegación está lleno de tierra y papas.
            Consume oxígeno y sobrecarga los relés de energía...
            ...¡pero la tripulación está muy orgullosa de sus 'hijos'!
            """)
            delta_energia += -10
            delta_oxigeno += -20
            delta_tripulacion += +20 
            
        
        elif eleccion == "2":
            print("""
            Confiscas las papas. El Comandante se hace un puré.
            La tripulación te mira con odio. Has matado a sus hijos.
            """)
            
            delta_tripulacion += -25 # Penalización de la opción 2
            
        else:
            print("Error: Comando no válido.")
            


    return delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion

def evento_concierto_yola():

    delta_energia = 0
    delta_combustible = 0
    delta_oxigeno = 0
    delta_tripulacion = 0
    eleccion = ""
    
    print("""
    ¡Alerta de tripulacion! La tripulacion está por los suelos.
    El Comandante saca un disco duro: 'El Show de Yola' (cositas peruanas).
    Propone transmitir 'La Gallina Turuleca' por los altavoces.
    """)
    
    while eleccion != "1" and eleccion != "2":
        print("""
        Opciones:
        1. Aprobar el concierto. 
        2. Mantener el protocolo de silencio en el espacio.
        """)
        eleccion = input("Ayuda al peruanito a decidir (1 o 2):")

        if eleccion == "1":
            print("Poniendo 'La Gallina Turuleca' a todo volumen...")
            resultado = random.randint(1, 100)
            
            # 50% Error
            if resultado <= 50: 
                print("¡COMPLICACIÓN! Las vibraciones causaron un cortocircuito.")
                print("La música se apaga de golpe. La tripulacion se desploma.")
                
                delta_energia += -10
                delta_tripulacion += -20

            else: 
                print("¡Es un éxito! La tripulación baila. La tripulacion se dispara.")
                
                delta_tripulacion += 20
        
        elif eleccion == "2":
            print("Protocolo de silencio mantenido. Eres una IA aburrida.")
            
            delta_tripulacion += -10
            
        else:
            print("Error: Comando no válido.")


            
    return delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion

def evento_terapia_contigo_peru():
    #recuerda que el comandante está deprimido, le dió de sus ataques
    delta_energia = 0
    delta_combustible = 0 
    delta_oxigeno = 0
    delta_tripulacion = 0 
    eleccion = ""

    print("""
    Alerta de Biomonitor: El Comandante está en su deprsion.
    Se niega a autorizar la quema de combustible del día.
    """)
    
    while eleccion != "1" and eleccion != "2":
        print("""
        Opciones:
        1. Anular protocolo y poner 'Contigo Perú' a 120 decibelios.
        2. Falsificar la voz del Comandante.
        """)
        eleccion = input("Tienes que decidir (1 o 2):")

        if eleccion == "1":
            print("¡Activando terapia musical peruana!...")
            resultado = random.randint(1, 100)
            
            # 50% Error
            if resultado <= 50: 
                print("¡COMPLICACIÓN! La canción lo hizo llorar más.")
                print("En su rabieta, golpea la consola de O2 y causa una fuga.")
                delta_oxigeno += -15
                delta_tripulacion += -15

            else: 
                print("¡'ARRIBA PERÚ'! El Comandante se levanta y firma todo.")
                print("Los altavoces, sin embargo, ahora echan humo.")
                
                delta_energia += -5
                delta_tripulacion += +15
        
        elif eleccion == "2":
            print("Calculando imitación de voz... Gasta mucha energía.")
            
            delta_energia += -15
            
        else:
            print("Error: Comando no válido.")

            
    return delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion

def evento_protocolo_violeta():

    delta_energia = 0
    delta_combustible = 0 
    delta_oxigeno = 0
    delta_tripulacion = 0 
    eleccion = ""

    print("""
    Alerta: Uno de los tripulantes Down, "Panchito", tiene una erupción morada.
    El manual de la misión (que no leíste y nadie leyó) tiene un 'Protocolo Violeta' sellado.
    ...dice que debes EYECTAR de la nave al tripulante para 'evitar contaminación'.
    """)
    
    while eleccion != "1" and eleccion != "2":
        print("""
        Opciones:
        1. Seguir el manual. botar a Panchito (tripulacion muy baja, pero ahorra O2).
        2. Ignorar el manual. Tratarlo con agua de hojas de mango.
        """)
        eleccion = input("Ayuda al peruanito a decidir (1 o 2):")

        if eleccion == "1":
            print("""
            Panchito ha sido botado. La tripulación te mira con horror.
            Pero... oye, ahora hay más oxígeno para los demás.
            """)
            
            delta_energia += -5   
            delta_oxigeno += 25  
            delta_tripulacion += -40 
            
        
        elif eleccion == "2":
            print("Bañando a Panchito en hoja de mango...")
            resultado = random.randint(1, 100)
            
            # 50% Error
            if resultado <= 50: 
                print("¡COMPLICACIÓN! ¡El hongo reacciona mal a el baño y libera esporas!")
                print("El aire se llena de toxinas. Todos están enfermos.")
                delta_oxigeno += -25
                delta_tripulacion += -25

            else:
                print("¡Era solo un hongo espacial! El agua de mango lo mató.")
                print("La tripulación te aclama.")
                
                delta_tripulacion += +15
            
        else:
            print("Error: Comando no válido.")
            
    return delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion


"""esta funcion va a manejar los eventos con respecto al día"""
def seleccionar_y_manejar_evento(dia_actual, DIAS_TOTALES_MISION):

    #estas "deltas son variables que van almacenando la acumulacion de puntos con respecto a cada recurso"
    
    clear_screen()
    print(f"\n==================== DÍA {dia_actual} / {DIAS_TOTALES_MISION} ====================")

    # aqui empezamos y establecemos la lógica, para el dia 1 y el ultimo dia hay eventos fijos, los demás se darán de manera aleatoria
    
    if dia_actual == 1:
        #EVENTO DE INICIO (Fijo) 
        delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion = evento_inicio_bastardo()
        
    elif dia_actual == DIAS_TOTALES_MISION:
        # EVENTO FINAL (Fijo)
        delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion = evento_final_llegada_garime()
        
    else:
        # EVENTOS ALEATORIOS 
        print("Navegando por el espacio profundo. Evaluando situación...")

        # Tenemos 6 eventos aleatorios
        numero_evento = random.randint(1 , 6) 
        
        if numero_evento == 1:
            delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion = evento_filtro_inka_kola()

        elif numero_evento == 2:
            delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion = evento_maniobra_mototaxi()

        elif numero_evento == 3:
            delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion = evento_papa_espacial()

        elif numero_evento == 4:
            delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion = evento_concierto_yola()

        elif numero_evento == 5:
            delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion = evento_terapia_contigo_peru()

        elif numero_evento == 6:
            delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion = evento_protocolo_violeta()
            
        # Consumo base diario para eventos aleatorios (ya se añade dentro de cada función)
            
    # 3. Retornar los 4 deltas a main.py
    return delta_energia, delta_combustible, delta_oxigeno, delta_tripulacion