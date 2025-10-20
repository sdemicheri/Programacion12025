palabra="Si elijes quien uniera ese pedido unificarías escuchando decir escondido solo lugares ofrecidos guiados ruidosos amargos rosados lugares ocultos."
mensajeEscondido=''
for i in range (len(palabra)):
    if i==0 or palabra[i-1]==" ":
        mensajeEscondido+=palabra[i]
print (mensajeEscondido)