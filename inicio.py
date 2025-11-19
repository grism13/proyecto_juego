def mostrar_inicio():
    import os
    def clear_screen():
        if os.name == 'nt':  # Check if the operating system is Windows
            os.system('cls')
        else:  # Assume Unix-like (Linux, macOS)
            os.system('clear')

    # Mostramos la historia y el contexto
    def texto_introduccion():
        print(
        r"""

    ____  _                           _     _        
    | __ )(_) ___ _ ____   _____ _ __ (_) __| | ___   
    |  _ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \  
    | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) | 
    |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/  
                                                    

            
                
                  /\
                  ||
                  ||
                 /||\
                /:||:\
                |:||:|
                |/||\|
                 **
                **


            """
        )

        # Texto de historia (Parte 1)
        print(
            """
        Año 2045

        Donde los DOWNS están llamados a poblar el espacio exterior

        Un BASTARDO peruano con depresión decidió postularse a una investigación
        Pero no sabía que llegaría tan lejos...
        """
        )

        print(
            """
            .       * .            +           .          *
        """
        )

        # Texto de historia (Parte 2)
        print(
            """
        Cansado de estar sumergido en la indigencia y el alcohol
        Decide aceptar la propuesta que puede cambiar la humanidad como la conocemos

        Ahora eres una IA encargada de cuidar la nave y las decisiones que tome el peruano para llegar con la tripulación cuidando los recursos
        """
        )

        # Pausa para el jugador
        input("\nPresiona ENTER para continuar...")
        clear_screen()

        # Divisor de sección
        print(
            """
        ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
        """
        )

        # Texto de objetivo (Parte 1)
        print(
            """
        TU ayudarás a EL BASTARDO
        Tienes una unica misión
        Debes llegar al planeta "GARIMÉ"
        """
        )

        # Pequeño planeta/destino
        print(
            r"""
                .
            .   |   .
          .     |     .
         .      |      .
        .------( )------.
         '      |      '
          .     |     .
            .   |   .
                '
        """
        )
        # Pausa para el jugador
        input("\nPresiona ENTER para continuar...")

        clear_screen()

        # Texto de objetivo (Parte 2)
        print(
            """
        Tu objetivo es cuidar de tu tripulación y de los recursos que dispones
        Estas a cargo de 4 DOWNS PERUANOS que deben llegar contigo a "GARIME"
        """
        )

        # Pequeños tripulantes
        print(
            r"""
              .         .
             / \       / \
            |   |     |   |
            | O |     | O |
            |   |     |   |
           /| ~ |\   /| ~ |\     
          / |   | \ / |   | \     
         *  |___|  *  |___|  *  
         o/
        /|      \o/        o
        / \      |        /|\
                / \       / \        
            """
        )

        # Texto de objetivo (Parte 3)
        print(
            """
        Ellos son la prueba para saber si somos capaces de adaptarnos a esas condiciones planetarias
        ¿Eres capaz de cumplir esta mision?
        """
        )
        input("\nPresiona ENTER para continuar...")
    clear_screen()
    texto_introduccion() 

    # iniciamos el juego
    def comienzo_juego():
        inicio = input("Selecciona el 1 para comenzar tu aventura por el espacio: ")
        while inicio != "1":
            print("Error, selecciona el 1")
            inicio = input("Selecciona el 1 para comenzar tu aventura por el espacio: ")

        print("Perfecto, iniciando tu propia aventura")
    comienzo_juego()

    print("")

    # elegimos la dificultad ajajaj
    def seleccionar_dificultad():

        print(
            """    ===== SELECCIONAR DIFICULTAD =====

        1) :) Facil: Ganas con mínimo 20% de Oxígeno y 20% de Energía
        2) :/ Medio: Ganas con mínimo 30% de Oxígeno y 40% de Energía
        3) :( Difícil: Ganas con mínimo 40% de Oxígeno y 60% de Energía
            """
        )

        opcion = ""
        while opcion != "1" and opcion != "2" and opcion != "3":
            opcion = input("Elige tu dificultad: 1, 2 o 3: ")

            if opcion != "1" and opcion != "2" and opcion != "3":
                print("ERROR, debes elegir 1, 2 o 3")

        energia = 100
        combustible = 100
        oxigeno = 100
        estado_tripulacion= 100

        if opcion == "1":
            print(
                "Dificultad fácil seleccionada. Requisitos mínimos para ganar, 20% Energía, 20% Oxigeno"
            )
           
        elif opcion == "2":
            print(
                "Dificultad media seleccionada. Requisitos mínimos para ganar, 40% Energía, 30% Oxigeno"
            )

        elif opcion == "3":
            print(
                "Dificultad dificil seleccionada. Requisitos mínimos para ganar, 60% Energía, 40% Oxigeno"
            )

        return energia, combustible, oxigeno, estado_tripulacion

# los valores que se retornaron
    (energia, combustible, oxigeno, estado_tripulacion) = (
        seleccionar_dificultad()
    )
mostrar_inicio()