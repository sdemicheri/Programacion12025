usuario = input("Ingrese el nombre de usuario: ")
contraseña = input("Ingrese la contraseña: ")
if usuario == "admin" and contraseña == "123456":
    print("Acceso concedido")
else:
    print("Acceso denegado")