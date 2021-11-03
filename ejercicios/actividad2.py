#1 Pide un numero por consola
#Si es un 9 o superior muestra el texto Sobresaliente
#Si es mauor o igual de 5 y menor de 9, muestra el texto aprobado
#Si es menor de 5, muestra suspenso

def notas():
    nota=int(input("Dime un numero "))
    print(nota)

    if nota>0 and nota<5:
        print("Suspenso")
    elif nota>=5 and nota<9:
        print("Aprobado")
    elif nota>=9 and nota<=10:
        print("Sobresaliente")
    else:
        print("numero incorrecto")

notas()

#2Mostrar los numeros impares que hay en los 100 primeros numeros
#Muestra cuanto tiempo ha tardado en ejecutarse ese programa
import time
print(time.time())
time.sleep(1)
for i in range(1,101):
	if i%2!=0:
		print(i)

print(time.time())


#3Programa una funcion que realiza la suma de los 100 primeros numeros


def sumaNumeros():
    final= int(input("Hasta que numero quieres sumar?: "))
    suma=0
    for i in range(1,final+1):
        suma=suma+i
    print("Suma = ",suma)


sumaNumeros()

#4Por consola te pide las unidades y luego el precio
#Si las unidades son mayor de 10 tienes un descuento del 20%
#muestra por consola el total y el total con el iva
#programa la funcion para permitir modificar el tipo de descuento e iva

def programa(descuento=1, iva=1.21):
    unidades=int(input("Dime las unidades: "))
    precio=float(input("Dime el precio: "))

    if unidades>10:
        descuento=0.3

    total=unidades*precio*descuento
    total1=unidades*precio*iva
    print(f"Total con descuento {total}")
    print(f"Total con iva {total1}")

programa()


#5 Por consola realizas una pregunta donde el usuario debe responder
#Sigue mostrando la pregunta hasta el usuario responde
#si han pasado 10 segundos, se cierra la consola

def preguntas():
    pregunta=""

    while(pregunta!="si"):
       pregunta = input("Sevilla tiene un color especial? ")


preguntas()