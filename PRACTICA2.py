print("-------------")
print("Práctica 2")
print("-------------")
print("EJERCICIO 1")
print("Ingrese una contraseña: ")
contraseña = input()
contraseña.lower()
print("Ingrese de nuevo su contraseña: ")
contraseña2 = input()
if (contraseña.lower() == contraseña2.lower()):
    print("Contraseña correcta, su contraseña es: "+contraseña.lower())
else:
    print("Las contraseñas no coinciden")

class personas:
    print("-------------")
    print("Práctica 2")
    print("-------------")
    print("EJERCICIO 2")
    print("¿Cuál es tu nombre?")
    nombre = input()
    x = ord(nombre[0].lower())
    print ("¿Cuál es tu sexo?")
    sexo = input()
    if (sexo[0]=="f".lower()):
        if (x>96 & x<108):
         print(nombre," de sexo femenino pertence al grupo A")
        else: 
         print(nombre," de sexo femenin0 pertence al grupo B")
    if (sexo[0]=="m".lower()):
        if (x>109 & x<122):
         print(nombre," de sexo masculino pertence al grupo A")
        else:
            print(nombre," de sexo masculino pertence al grupo B")
       
    

