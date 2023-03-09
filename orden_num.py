print("------------------------------------------")
print("---ORDERNAR NÚMEROS EN ORDEN ASCENDENTE---") 
print("------------------------------------------")

a=int(input("Escriba el primer número: "))
b=int(input("Escriba el segundo número: "))
c=int(input("Escriba el tercer número: "))

if a > b > c:
    r = c, b, a
elif a > c > b:
    r = b, c, a
elif c > a > b:
    r = b, a, c
elif b > c > a:
    r = a, c, b
elif b > a > c:
    r = c, a, b
else:
    r = a, b, c
print("Los números en orden ascendente es")
print(r)