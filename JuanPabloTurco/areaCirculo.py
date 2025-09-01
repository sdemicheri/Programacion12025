PI=3
try:
    radio=int(input("ingreso radio"))
except ValueError:
    print("Error ingreso de numero")
else:
    area=PI*(radio*radio)
    print(area)
finally:
    print("garcia")