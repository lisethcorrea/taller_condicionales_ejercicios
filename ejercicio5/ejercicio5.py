# programa para definir el precio a pagar de la factura del agua
print("-----------------------------")
print("-----digite su consumo-------")
print("-----------------------------")
# input

co=int(input("digite su consumo: "))

# processing
cf=10000

if co<=50:
    msj= cf
else:
    if co<=200:
        msj= cf+2000(co-50)
    else:
        if co>200:
         total_pagar=("su total a pagar es: " + str(vco2))
        
  

# output

print("")
print("----------------------------")
print("este es el valor de su factura")
print("-----------------------------")
print("")
print(total_pagar)