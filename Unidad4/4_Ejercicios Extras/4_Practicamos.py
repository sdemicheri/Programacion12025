usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")

nombre = "admin"
contraseña1 = "123456"

if usuario == nombre and contraseña == contraseña1:
 print("Acceso concedido")
else:
 print("Acceso denegado")