peluche = int(input("ingrese cuanto cuesta el peluche:"))
 
B_cien = 100
B_cincu = 50
B_veinte = 20
B_diez = 10
B_cinco = 5
B_uno = 1

A_ = peluche%B_cien
B_ = peluche//B_cien
C_ = A_%B_cincu
D_ = A_//B_cincu
E_ = C_%B_veinte
F_ = C_//B_veinte
G_ = E_%B_diez
H_ = E_//B_diez
I_ = G_%B_cinco
J_ = G_//B_cinco
K_ = I_%B_uno
L_ = I_//B_uno

print("Necesitas:", B_, "billetes de 100")
print("Necesitas:", D_, "billetes de 50")
print("Necesitas:", F_, "billetes de 20")
print("Necesitas:", H_, "billetes de 10")
print("Necesitas:", J_, "billetes de 5")
print("Necesitas:", L_, "billetes de 1")