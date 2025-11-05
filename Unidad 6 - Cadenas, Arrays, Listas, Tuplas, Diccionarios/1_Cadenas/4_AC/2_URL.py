"""
En una empresa se presenta el siguiente problema de seguridad informatica:

Se han detectado violaciones a la seguridad en diferentes URL, las cuales deberian ser bloqueadas por el firewall. Una URL esta compuesta por un protocolo, un dominio, el camino a la carpeta donde esta la pagina y la pagina junto a variables de acceso. Por ejemplo:

https://cvirtual.frvm.utn.edu.ar/course/modedit.php?update=108669&return=1

donde cvirtual.frvm.utn.edu.ar es el dominio y /course/ es la carpeta donde se aloja la pagina.

Se debe desarrollar un algoritmo que si se ingresa una URL, el resultado debe ser el dominio y las carpetas que deben ser bloqueadas para prevenir el acceso a los usuarios de la empresa y que no caigan en una violacion a la seguridad.

Por ejemplo:

https://cvirtual.frvm.utn.edu.ar/course/modedit.php?update=108669&return=1

debe retornar 

cvirtual.frvm.utn.edu.ar/course/
"""
url = input("Ingresa la url: ").lower()
nueva_url = ""
contador_barra = 0
posicion_barra = 0

for j in range(len(url)):
    if url[0] == "h":
        for i in range(8,len(url)):
            if url[i] == "/":
                posicion_barra = i
        for i in range (8,posicion_barra+1):
            nueva_url += url[i]
    elif url[0] == "f":
        for i in range(6,len(url)):
            if url[i] == "/":
                posicion_barra = i
        for i in range (6,posicion_barra+1):
            nueva_url += url[i]

print(nueva_url)