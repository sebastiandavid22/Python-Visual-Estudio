import datetime
FechaAactual = datetime.datetime.now()
fecha = datetime.datetime.strftime(FechaAactual, '%d/%m/%Y')
N = int(input("Ingrese la cantidad de estudiantes: "))
for i in range(N):
 Nombre =  input("Diga el nombre del estudiante: ")
 Apellido = input("Diga el apellido del estudiante: ")
 Institucion = input("Diga a la institucion que pertenece: ")
 EmpresaEstudio = input("Diga la empresa donde estudia: ")
 Creditos = int(input("Diga la cantidad de creditos que desea tomar: "))
 TipoMatricula = input("Diga el tipo de matricula \n[Anticipada] \n[Ordinaria] \n[Extemporanea] \n")
 Programa = int(input("Diga al programa que pertenece \n[0]Tecnica \n[1]Tecnologia \n[2]Ingenieria \n[3]Especializacion \n"))
 if Programa == 0:
  Valor = Creditos * 250000   
  Programa = "Tecnica" 
  
 elif Programa == 1:
    Valor = Creditos * 400000
    Programa = "Tecnologia" 
    
 elif Programa == 2:
    Valor = Creditos * 550000
    Programa = "Ingenieria" 
    
 elif Programa == 3: 
    Valor = Creditos * 950000
    Programa = "Especializacion" 
    

 if TipoMatricula == "Extemporanea":
    Total = Valor * 1.10
    
 elif TipoMatricula == "Ordinaria":
    Total = Valor 
    
 elif TipoMatricula == "Anticipada":
    Subtotal = Valor * 0.15
    Total = Valor - Subtotal
    
 print(fecha)
 print(f"Nombre:  {Nombre}  || Apellido:  {Apellido}")
 print(f"Institucion: {Institucion} || Empresa donde estudia: {EmpresaEstudio}")
 print(f"Cantidad de creditos: {Creditos} || Tipo de matricula:  {TipoMatricula} || Programa: {Programa}")
 print(f"Valor de matricula: $ {Total}") 