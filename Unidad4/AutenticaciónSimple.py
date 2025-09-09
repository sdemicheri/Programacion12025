#Sitema de autenticación simple Crear un programa que pida y contraseña. Si son "admin"
# y "123456", mostrar "Acceso concedido", sino "Acceso denegado"

usuario = input()
contraseña = input()
if usuario == "Admin" and contraseña == "123456":
    print("Acceso concedido")
else:
    print("Acceso denegado")
    
    
usuario = input()
contraseña = input()
usuarioOk = "Admin"
contraseñaOk = "123456"
if usuario == usuarioOk and contraseña == contraseñaOk:
    print("Acceso concedido")
else:
    print("Acceso denegado")
    

usuarioOk = "Admin"
contraseñaOk = 123456
usuario = input()
contraseña = input()
if (usuario == usuarioOk and contraseña == str(contraseñaOk)):
    print("Acceso concedido")
else:
    print("Acceso denegado")

