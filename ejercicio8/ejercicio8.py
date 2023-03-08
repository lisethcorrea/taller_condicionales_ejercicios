# programa para calcular si un número entero en multiplo de otro entero

# input
x=int(input("digite el primer numero"))
y=int(input("digite el segundo numero"))

# prossecing

if x%y==0:
    msj= "el numero" ,x, "es multiplo de: " ,y,
else:
    msj= "no son multiplos"
    if y%x==0:
        msj= "el numero" ,y, "es multiplo de: " ,x,
    else: 
        msj= "no son multiplos"


# output

print(msj)