# proyecto_juego

# PARTICIPANTES
    -*ROAND RODRIGUEZ CI:32.790.788*
    -*GRISANGELY MARTINEZ CI:32.197.707*
    -*ELIEZER RODRIGUEZ CI: 32.486.801*
    -*HAMAD EL TROUDI CI: 31.899.491*


# ROLES DE CADA PARTICIPANTE

**HAMAD**: Encargado de los modulos: **inicio.py y final.py**.
    -inicio.py se encarga de la interfaz inicial del ususario, dando a elegir la dificultad y mostrando los recursos que tiene segun cada dificultad.
    -final.py establece las condiciones en las que el usuario gana o pierde .

-(Se añadió la parte del inicio al main mediante un merch por la compañera gris ya que requería agregar unos dibujitos)

**ELIEZER**: Encargado del módulo: **recursos.py**.
    
    -recursos.py se encarga de administrar los recursos del usuario.

**ROAND**: Encargado del módulo: **eventos.py**.
    
    -eventos.py se encarga de establecer los eventos y la situaciones que se le presentan al jugador en el juego.

# MÓDULO 3: eventos.py
Rol: Presentar eventos, recibir decisiones y retornar 4 deltas: (delta_energia, delta_combustible, delta_oxigeno, delta_moral)
*(Los deltas significan sumatorias, es decir, es la acumulacion de puntos positivos o negativos que vaya acumulando el jugador, estos se sumarán con los valores de los recursos)*

**GRIS**: Encargada del archivo principal del juego: **main.py**.
    -main.py se encarga de juntar todos los módulos y establecer la logica del juego con las funciones importadas.

# INFORMACION DEL JUEGO

Nombre: Salvando al Bastardo

🎯**Objetivo**
    Ayudar al personaje a llegar a su destino mediante preguntas y respuestas, la mision es cuidar el estado de la tripulacion y administrar los recursos.

👨‍🚀**Personajes**
    -Comandante
    -Personajes con Síndrome de down

📦**Recursos**
    -Energía
    -Oxígeno
    -Combustible
    -Estado de la tripulación

🎮**Modalidad de Juego**
    -Preguntas y respuestas.
    -El usuario toma decisiones y, en base a eso, disminuyen o aumentan sus recursos.

📜**Historia y Contexto**
    El personaje peruano con depresión tuvo que salir de la Tierra por una misión para ver y supervisar a la tripulación con Síndrome de down, que fueron enviados de prueba a sobrevivir en un planeta.
    Tiene que sobrevivir en la nave cuidando los recursos y la tripulación. La misión es ayudarle al peruano a tomar decisiones.

🚀**Fases del Juego**

*Inicio*:

    Dar la bienvenida al usuario.
    Dar contexto de la situación.
    Darle (asignar) una dificultad.

*Desarrollo*:

    El juego contará con un desarrollo ubicado en una nave espacial donde se van a plantear diferentes eventos.

    El jugador estará en situaciones que pueden ser adversas para su partida o donde podrá mejorar sus posibilidades de sobrevivir.

    Tiene una gestión de recursos donde cada recurso cuenta para llegar al final.

    Cada dilema irá afectando (subiendo o bajando) los recursos.


🏁 **Final del Juego**

*Ganar*
    Se necesita una cantidad mínima de recursos y  elementos para ganar (todos los elementos).

Nivel Fácil: 30% mínimo (de energía, oxígeno, combustible).

-Oxígeno:
    Fácil: 30% mínimo para ganar
    Medio: 40% mínimo para ganar
    Dificil: 50% mínimo para ganar

-Energía:
    Fácil: 30% mínimo para ganar
    Medio: 40% mínimo para ganar
    Dificil: 50% mínimo para ganar

*Perder*

-Pierdes si no cumples los requisitos

# Reglas del juego:

1. **El Objetivo**: Tu único objetivo es ayudar al Comandante a llegar al planeta "GARIMÉ" y sobrevivir. La misión dura 8 días (turnos).

2. **Tu Rol**: Eres la IA de la nave. No eres el comandante, eres quien gestiona la nave y presenta las opciones ante las crisis.

3. **Los Recursos**: Debes gestionar 4 recursos vitales:

-Energía: Para los sistemas de la nave.

-Combustible: Para mover la nave.

-Oxígeno: Para que la tripulación respire.

-Estado de la Tripulación: Para evitar que el Comandante y la tripulación colapsen.

4. **El Flujo del Juego**:

-Empezarás eligiendo una dificultad (Fácil, Normal, Difícil) que define tus recursos iniciales.

-Cada día, se presentará un evento. El Día 1 y el Día 8 son fijos.

-Los días 2 al 7 serán eventos aleatorios de la lista de 6 crisis que definimos.

Cada evento te dará 2 opciones.

5. **La Tasa de Error** (Complicación Dinámica)

-De todas las opciones, al menos una opcion tendrá una probabilidad de fallo, esta no hará perder al usuario, solo lo retrasará

6. **Cómo Perder** (Derrota Inmediata) 

-Pierdes automáticamente en el momento en que CUALQUIERA de tus 4 recursos llegue a el minimo segun cada dificultad.

7. **Cómo Ganar** (Victoria) 

-Para ganar, debes cumplir DOS condiciones:

-Sobrevivir los 8 días sin que ningún recurso llegue a el minimo.

-Al llegar a "GARIMÉ" en el Día 8, debes tener tus recursos por encima de la "Cantidad Mínima" requerida por tu nivel de dificultad.

8. **Cómo Perder** (Derrota Final) 

-Si sobrevives los 8 días pero tus recursos están debajo de la "Cantidad Mínima", serás recibido con un mensaje de derrota final al llegar a "GARIMÉ".
