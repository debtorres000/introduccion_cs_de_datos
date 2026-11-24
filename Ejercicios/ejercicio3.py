tiempo = float(input("Ingrese las horas de permanencia : "))
pagar = int(tiempo + 0.99)
importe = pagar * 15
print("Importe a pagar: $", importe)
#lo que hace el +0.99 es redondear hacia arriba, ya que si el tiempo es 1.1 horas, se cobrará como 2 horas.