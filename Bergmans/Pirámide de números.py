try:
  N = int(input("Introduce un número entero positivo: "))
  if N <= 0:
    print("Por favor, introduce un número entero positivo.")
  else:
    for i in range(N, 0, -1):
      for j in range(1, i + 1):
        print(j, end=" ")
      print()
except ValueError:
  print("Entrada inválida. Por favor, introduce un número entero.")