Codigo1,Unidad1,Precio1 = input().split()
Codigo2,Unidad2,Precio2 = input().split()
Pago = int(Unidad1) * float(Precio1) + int(Unidad2) * float(Precio2)
print('VALOR A PAGAR: R$ %.2f' %Pago)