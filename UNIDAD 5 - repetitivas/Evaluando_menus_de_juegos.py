# EVALUACION DE MENUS DE JUEGO DE MIS COMPAÑEROS

#----- VOLVER  A MIRAR SUS CODIGOS PARA RECORDAR QUE USARON Y NO QUE NO DE LAS UNIDADES

# PUNTAJE : RESTA, TENIENDO EN CUENTA QUE 10 ES EL NUMERO MAS ALTO Y 1 EL MAS BAJO
#            DIVIDI EL 10, 4  PUNTOS PRINCIPALES, DEJANDO CADA PUNTO CON UN VALOR MAXIMO DE 2.5
#            Y ME TOME EL ATREVIMIENTO BAJO EL MISMO CRITERIO DE EVALUARME A MI MISMA 

# CRITERIO DE EVALUACION UTILIZADO: 
#    1)  CLARIDAD Y ORGANIZACION : esta bien representado, se entiende?
#    2)  CONTENIDO Y PRECISION   : la informacion es la pedida en la consigna?
#    3)  CREATIVIDAD Y ESFUERZO  : hay un aporte extra aportado?
#    4)  FUNCIONALIDAD:            el codigo corrio bien?

# JOSE : 8.5
#2.5        codigo y explicacion clara, tanto visual como en la lectura en pantalla
#1          completo la tarea, pero sumo cosas que no debia 
#2.5        si bien uno sabe que todo los juegos llevaron tiempo y dedicacion, se nota que uno de los juegos fue mas desafiante (el de las 15 opc)
#2.5        el codigo corre bien

# CAROLINA: 6.5
#1.5        codigo limpio, explicacion no clara oral
#1          completo tarea, pero sumo cosas que no debia y no unio los juegos en un solo bloque  (while, [], ramdom)
#1.5        si bien uno sabe que todo los juegos llevaron tiempo y dedicacion, se nota que uno de los juegos fue mas desafiante con el uso de letras
#2.5        el codigo corre bien

# MIKEAS : 8.5
#2.5        codigo y explicacion clara, tanto visual como en la lectura en pantalla
#1          completo la tarea, pero sumo cosas que no debia ( while, break ramdom )
#2.5        
#2.5        codigo corre BlockingIOError

# CELESTE : 6
#2.5        codigo y explicacion clara, sabe sus errores y limitaciones de su programa
#1          completo consigna, uso cosas que no debiamos y no utilizo for ni contadores/acumuladores
#1.5        hubo esfuerzo, juego simples
#1          el codigo no funciono bien

# THIAGO:   10
#2.5        codigo largo, pero totalmente claro, limpio y excelente desarrollo oral
#2.5        completo tarea y cumplio con lo establecido
#2.5        mucha creatividad con la interacion persona y juego, esfuerzo muy valorado por las +400 lineas de codigo por respetar consigna
#2.5        codigo corrio bien

#   GUILLE: 8.5
#2.5        codigo largo, pero totalmente claro, limpio y excelente desarrollo oral
#1          completo consigna, uso cosas que no debiamos y no utilizo
#2.5        creatividad y esfuerzo 
#2.5        codigo corrio

#   ULISES: 7.5
#1.5        codigo y explicacion clara, EN ALGUNOS MOMENTO NO SUPO EXPLICARSE sabe sus errores y limitaciones de su programa
#1.5        completo consigna, utilizo for pero tambien uso cosas que no debiamos como el WHILE y finalizar USO MAIN() Y LIBRERIA
#2          simple y con esfuerzo
#2.5        corrio bien el codigo

# JUAN PABLO: 8.5
#2.5     codigo limpio y explicacion clara
#1.5     completo tarea, no cumplio con las consignas de uso: falto usar; no debio usar: while true,
#2       creatividad a la hora de elegir y desarrollar consignas e interaccion persona/juego, lo que resalta el esfuerzo
#2.5     el codigo funciona

# YAIR : 9.5
#2.5      CLARIDAD Y ORGANIZACION : CLARO Y CORTO
#2.5      CONTENIDO Y PRECISION   : CUMPLIO CON EL CONTENIDO, EL INGRESO LO HIZO A MEDIDA QUE NECESITABA Y NO AL COMIENZO, ALGO DESORDENADO.
#2        CREATIVIDAD Y ESFUERZO  : CREATIVIDAD EN EL JUEGO Y EN LA DEVOLUCION DE "ERROR/RESPUESTA CORRECTA" AMIGABLE Y PERZONALIZADO. 
#2.5      FUNCIONALIDAD:     EL CODIGO CORRE BIEN Y ES CLARO SIN ROMPER

# LUDMILA : 6.5
#2.5    CLARIDAD Y ORGANIZACION : codigo claro  y organizado, tambien claridad en el oral
#1.5    CONTENIDO Y PRECISION   : CUMPLIO CON CONTENIDO PERO USO =*18 NO LO VIMOS PARA NO TENER TANTAS LINEAS, NO USO NI FOR NI BREAK PARA TERMINAR EL BUCLE Y NO USO BIEN EL CONTADOR DE RONDAS HACIENDO INF. EL BUCLE
#1.5    CREATIVIDAD Y ESFUERZO  : poca creatividad en la eleccion del juego, pero esfuerzo en resolverlo
#1      FUNCIONALIDAD:     EL PROGRAMA CORRE, PERO NO DEJA DE CORRER JAJA



#----------------------------- FINALIZADO EL CRITERIO DE EVALUCION ARME EL CODIGO DE LA EVALUACION:

for i in range(10):
    nombre_estudiante = input("\nIngresa el nombre del estudiante: ")

    # Pedir la nota y convertirla a número con decimales
    try:
        nota = float(input(f"\nIngresa la nota de {nombre_estudiante} (de 1 a 10): "))
    except ValueError:
        print("Error: La nota ingresada no es un número válido, ingrese un número del 1 al 10.")
        # Detenemos la ejecución si la nota no es un número
        exit()

    # 6 se considera aprobado.
    NOTA_MINIMA_APROBACION = 6

    # Usar una estructura condicional (if/else) para determinar si aprobó
    if nota >= NOTA_MINIMA_APROBACION:
        estado = "¡APROBADO! 🎉"
    else:
        estado = "REPROBADO. 😔"

    # Mostrar el resultado final
    print("\n--- Resultado ---")
    print(f"Estudiante: {nombre_estudiante}")
    print(f"Nota obtenida: {nota}")
    print(f"Estado: {estado}")
    print("-----------------")