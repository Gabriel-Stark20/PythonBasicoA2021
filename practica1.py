print("----------")
print("Ejercicio 1")
x = int(input("Ingrese el nivel de la figura: "))
for i in range(x+1):
    print("*"*i)




print("----------")
print("Ejercicio 2")
y = int(input("Ingrese un número para verificar si es un númeero primo: "))
z = 0
for i in range(1, y+1):
    if y % i  == 0:
        z+=1
if z != 2:
    print("El número ", y, " no es un número primo")
else:
     print("El número ", y, " si es un número primo")