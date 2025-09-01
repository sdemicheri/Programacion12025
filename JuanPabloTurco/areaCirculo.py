PI=3.1415
try:
    radio=int(input("ingreso radio "))
except ValueError:
    print("Error ingreso de numero")
else:
    area=PI*(radio*radio)
    print("El area es: ", area)
finally:
    print("garcia")