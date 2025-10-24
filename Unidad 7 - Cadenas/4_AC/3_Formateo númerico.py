"""
Una empresa exportadora genera reportes de facturación en diferentes sistemas contables. Al consolidar la información, detectan que algunos documentos presentan los importes con distintos formatos numéricos:

En ciertos reportes, los números utilizan la coma para separar miles y el punto para indicar decimales (formato anglosajón).

En otros, se emplea el punto para separar miles y la coma para indicar decimales (formato hispano).

Esto provoca errores al momento de cargar los datos en un sistema de gestión, ya que el software no logra interpretar correctamente los montos.

Por ejemplo, se observan los siguientes casos:

📄 Reporte A (formato anglosajón)

Total (ARS): 33,916,828.12

📄 Reporte B (formato hispano)

Total (ARS): 46.506.748,86

El área administrativa necesita unificar los reportes para que todos utilicen el mismo formato numérico y garantizar que los cálculos de IVA y Totales sean correctos.

Se solicita que ingresado un total en formato anglosajón, se visualice en formato hispano.
"""
cadena = input()        #  33,916,828.12 SE INGRESA ASI
                        #  33.916.828,12 DEBE SALIR ASI
nueva_salida = ""
for i in range(len(cadena)):
    if cadena[i] != "," and cadena[i] != ".":
        nueva_salida += cadena[i]
    elif cadena[i] == ",":
        nueva_salida += "."
    if cadena[i] == ".":
        nueva_salida += ","
    
print(nueva_salida)