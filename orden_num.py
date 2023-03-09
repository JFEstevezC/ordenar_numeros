print("------------------------------------------")
print("---ORDERNAR NÚMEROS EN ORDEN ASCENDENTE---") 
print("------------------------------------------")

a=int(input("Escriba el primer número: "))
b=int(input("Escriba el segundo número: "))
c=int(input("Escriba el tercer número: "))

if a > b:
    if a > c:
        if b > c:
            r = c, b, a
        else:
            r = b, c, a
    else:
        r = b, a, c
elif b > c:
    if c > a:
        r = a, c, b
    else:
        r = c, a, b
else:
    r = a, b, c
print("Los números en orden ascendente es")
print(r)