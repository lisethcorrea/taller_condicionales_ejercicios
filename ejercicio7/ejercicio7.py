# programa para mirar si dados 3 numeros, la suma de los 2 primeros es igual al tercero
print("------------------------------")
print("-----digite los numeros-------")
print("------------------------------")
# input

a=int(input("digite el 1 numero: "))
b=int(input("digite el 2 numero: "))
c=int(input("digite el 3 numero: "))


# processing
p1=a+b
p2=a+c
p3=b+c
if p1 ==c:
    suma=("la suma de c es a+b ")
else:
    if p2 == b:
        suma=("la suma de b es a + c")
    else:
        if p3 == a:
         suma=("la suma de a es a + c")
        else:
           suma=("la suma no equivale a otro entero de la suma")

        
  

# output

print("")
print(suma)