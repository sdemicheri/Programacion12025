# los nombres son las key, mientras que sus respectivos puntajes, son los Value
prueba_deportiva = {'jorge': 500, 'diana': 600, 'Rodrigo': 800}
prueba_deportiva['ana']= 1200

print(prueba_deportiva['ana']) # imprime los puntos de ana
print(prueba_deportiva['Rodrigo']) # imprime los puntos de rodrigo

# muestra elemento por elemento
for persona, puntaje in prueba_deportiva.items():
    print(f"La persona {persona} obtuvo {puntaje} puntos")

# muestra todo el diccioanario completo
print(prueba_deportiva)