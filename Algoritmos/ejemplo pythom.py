pD1=100
pD2=100
pD3=100
pD4=100
pD5=100

produccionsemanal=  pD1 + pD2 + pD3 + pD4 + pD5 

if produccionsemanal >= 500:
    recibe_incentivo = True

else:
     recibe_incentivo = False


if recibe_incentivo:
  print("El empleado recibe incentivo")
else:
  print("El empleado no recibe incentivo")
    