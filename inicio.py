# Mostramos la historia y el contexto
print(
    """==========================================
             SALVANDO AL BASTARDO          
==========================================
Año 2045
Donde los DOWNS están llamados a poblar el espacio exterior
Un BASTARDO peruano decidió postularse a una investigación
Pero no sabía que llegaría tan lejos...
Cansado de estar sumergido en la indigencia y el alcohol
Decide aceptar la propuesta que puede cambiar la humanidad como la conocemos
"""
)

# mostramos el objetivo

print(
    """TU ERES EL BASTARDO
Tienes una unica misión
Debes llegar al planeta KEPLER-452b
Tu objetivo es cuidar de tu tripulación y de los recursos que dispones
Estas a cargo de 4 DOWNS PERUANOS que deben llegar contigo a KEPLER-452b
Ellos son la prueba para saber si somos capaces de adaptarnos a esas condiciones planetarias
¿Eres capaz de cumplir esta mision?
"""
)

# iniciamos el juego

inicio = int(input("Selecciona el 1 para comenzar tu aventura por el espacio: "))
while inicio != 1:
    print("Error, selecciona el 1")
    inicio = int(input("Selecciona el 1 para comenzar tu aventura por el espacio: "))

print("Perfecto, iniciando tu propia aventura")

print("")

# fin de la bienvenida

# elegimos la dificultad


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
        opcion = input("Elige tu dificultad: 1, 2 o 3: ").strip()

        if opcion != "1" and opcion != "2" and opcion != "3":
            print("ERROR, debes elegir 1, 2 o 3")

    energia = 100
    combustible = 100
    oxigeno = 100

    if opcion == "1":
        print(
            "Dificultad fácil seleccionada. Requisitos mínimos para ganar, 20% Energía, 20% Oxigeno"
        )
        min_energia_ganar = 20
        min_oxigeno_ganar = 20

    elif opcion == "2":
        print(
            "Dificultad media seleccionada. Requisitos mínimos para ganar, 40% Energía, 30% Oxigeno"
        )
        min_energia_ganar = 40
        min_oxigeno_ganar = 30

    elif opcion == "3":
        print(
            "Dificultad dificil seleccionada. Requisitos mínimos para ganar, 60% Energía, 40% Oxigeno"
        )
        min_energia_ganar = 60
        min_oxigeno_ganar = 40

    return energia, combustible, oxigeno, min_energia_ganar, min_oxigeno_ganar


(energia, combustible, oxigeno, min_energia_ganar, min_oxigeno_ganar) = (
    seleccionar_dificultad()
)
