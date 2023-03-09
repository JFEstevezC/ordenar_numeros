

print("------------------------------------------")
print("---ORDERNAR NÚMEROS EN ORDEN ASCENDENTE---") 
print("------------------------------------------")

a=int(input("Escriba el primer número: "))
b=int(input("Escriba el segundo número: "))
c=int(input("Escriba el tercer número: "))

if a > b:
    if a > c:
        if b > c:
            print("Los números en orden ascendente es")
            print(c)
            print(b)
            print(a)
        else:
            print("Los números en orden ascendente es")
            print(b)
            print(c)
            print(a)
    else:
        print("Los números en orden ascendente es")
        print(b)
        print(a)
        print(c)
elif b > c:
    if c > a:
        print("Los números en orden ascendente es")
        print(a)
        print(c)
        print(b)
    else:
        print("Los números en orden ascendente es")
        print(c)
        print(a)
        print(b)
else:
    print("Los números en orden ascendente es")
    print(a)
    print(b)
    print(c)
