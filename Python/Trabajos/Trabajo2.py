AcumChicago1=0
AcumChicago2=0
AcumChicago3=0
ContLibresChicago = 0
ContDobleChicago = 0
ContTripleChicago = 0
AcumAngeles1=0
AcumAngeles2=0
AcumAngeles3=0
ContLibresAngeles = 0
ContDobleAngeles = 0
ContTripleAngeles = 0
while(True):
  Dato = int(input("Diga El Equipo: \n [1] Chicago Bulls \n [2] Angeles Lakers \n [0] Fin Del Juego \n"))
  if(Dato == 1):
     PuntosChicago = int(input("Diga la cantidad de puntos \n[1] Lazamiento Libre \n[2] Lazamiento Doble \n[3] Lazamiento Triple \n"))
     if(PuntosChicago ==1):
      ContLibresChicago+=1
      AcumChicago1+=PuntosChicago
     elif(PuntosChicago == 2):
      ContDobleChicago +=2
      AcumChicago2+=PuntosChicago
     elif(PuntosChicago == 3):
      ContTripleChicago +=3
      AcumChicago3 +=PuntosChicago
     TotalPuntosChicago = AcumChicago1 + AcumChicago2 + AcumChicago3
     
  elif(Dato == 2):
      PuntosAngeles = int(input("Diga la cantidad de puntos \n[1] Lazamiento Libre \n[2] Lazamiento Doble \n[3] Lazamiento Triple \n"))
      if(PuntosAngeles ==1):
       ContLibresAngeles+=1
       AcumAngeles1+=PuntosAngeles
      elif(PuntosAngeles == 2):
       ContDobleAngeles +=2
       AcumAngeles2+=PuntosAngeles
      elif(PuntosAngeles == 3):
       ContTripleAngeles +=3
       AcumAngeles3 +=PuntosAngeles
      TotalPuntosAngeles = AcumAngeles1 + AcumAngeles2 + AcumAngeles3

  elif(Dato == 0):
    break

print("-------------------------------------------------------------")
print("                            DATOS                            ")
print("-------------------------------------------------------------\n")
print("-------------------------------------------------------------")
print(f"Cantidad De Tiros Libres De Chicago Bulls: {ContLibresChicago}")
print(f"Cantidad De Tiros Dobles De Chicago Bulls: {ContDobleChicago}")
print(f"Cantidad De Tiros Triples De Chicago Bulls: {ContTripleChicago}")
print(f"Total Puntos De Chicago Bulls: {TotalPuntosChicago}")
print("------------------------------------------------------------- \n")

print("-------------------------------------------------------------")
print(f"Cantidad De Tiros Libres de Angeles Lakers: {ContLibresAngeles}")
print(f"Cantidad De Tiros Dobles de Angeles Lakers: {ContDobleAngeles}")
print(f"Cantidad De Tiros Triples de Angeles Lakers: {ContTripleAngeles}")
print(f"Total Puntos De Angeles Lakers: {TotalPuntosAngeles}")
print("------------------------------------------------------------- \n")

print("-------------------------------------------------------------")
print("                            GANADOR                          ")
print("-------------------------------------------------------------\n")

if(TotalPuntosChicago > TotalPuntosAngeles):
    for mensaje in "CHICAGO BULLS":
     print(mensaje," ",end='')
elif(TotalPuntosChicago < TotalPuntosAngeles):
   for mensaje in "ANGELES LAKERS":
     print(mensaje," ",end='')
else:
    for mensaje in "TIEMPO EXTRA":
     print(mensaje," ",end='')
    

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
