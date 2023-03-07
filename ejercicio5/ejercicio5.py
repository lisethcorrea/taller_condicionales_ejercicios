# programa para definir el precio a pagar de la factura del agua
print("-----------------------------")
print("-----digite su consumo-------")
print("-----------------------------")
# input

co=int(input("digite su consumo: "))

# processing
cf=10000
vco=cf
vco1=cf+((co-50)*2000)
vco2=cf+((co-200)*3000)+300000

if co<=50:
    total_pagar=("su total a pagar es: " + str(vco))
else:
    if co>50 and co<=200:
        total_pagar=("su total a pagar es: " + str(vco1))
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