import math
print("Dime un numero entero o decimal")
numero= input()


redondeado_abajo = math.floor(float(numero))

print("Redondeado con round: {}".format(redondeado_abajo))

def primos(redondeado_abajo):
    for n in range(2, redondeado_abajo):
        if redondeado_abajo % n == 0:
            print("no es primo",n,"es divisor")
            return False
    print("Es primo")
    return True

primos(redondeado_abajo)

print("Dime un año")
ano= input()
ano2=int(ano)
if ano2 % 4 != 0:
	print("No es bisiesto")
elif ano2 % 4 == 0 and ano2 % 100 != 0:
	print("Es bisiesto")
elif ano2 % 4 == 0 and ano2 % 100 == 0 and ano2 % 400 != 0:
	print("No es bisiesto")
elif ano2 % 4 == 0 and ano2 % 100 == 0 and ano2 % 400 == 0:
	print("Es bisiesto")

suma, extNum=0,0
while ano2 != 0:
    extNum = ano2 % 10
    ano2 //= 10
    suma += extNum
print(suma)