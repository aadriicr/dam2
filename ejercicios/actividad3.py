#almacenar 5 alumnos con 4 asignaturas : notas del 0 al 10
#media de nota por alumno
#media de nota de la clase
#alumnos son : juan, maría, pedro, laura, manuel
#asignaturas son _ programación, bases de datos, diseño de interfaces, despliegue de aplicaciones
#listas / tuplas / set / dictionary

alumnos=[
    {"juan":{"programacion":8,"bases de datos":7,"diseño interfaces":9,"despliegue":7}},
     {"maria":{"programacion":6,"bases de datos":7,"diseño interfaces":7,"despliegue":6}},
      {"pedro":{"programacion":7,"bases de datos":5,"diseño interfaces":5,"despliegue":7}},
       {"laura":{"programacion":8,"bases de datos":7,"diseño interfaces":5,"despliegue":7}},
        {"manuel":{"programacion":7,"bases de datos":5,"diseño interfaces":7,"despliegue":6}}
]
print(alumnos)

#media del alumno
for alumno in alumnos:
    for alumno,notas in alumno.items():
        print(alumno)
        media = sum(notas.values())
        print(media/len(notas))

#media por asignatura
prog,bbdd,di,desp=0,0,0,0
for alumno in alumnos:
    for alumno, notas in alumno.items():
        prog= prog + notas["programacion"]
        bbdd= bbdd + notas["bases de datos"]
        di= di + notas["diseño interfaces"]
        desp=desp + notas["despliegue"]
print("----------------MEDIAS----------------")
print("Media Programacion: ", prog/len(alumnos))
print("Media Bases de datos: ", bbdd/len(alumnos))
print("Media Despliegue: ", desp/len(alumnos))
print("Media Desarrollo de interfaces: ", di/len(alumnos))



#nota media del curso
total=0
for alumno in alumnos:
    for alumno, notas in alumno.items():
        total += sum(notas.values())/len(notas)

print(f"La media del curso es de {total /5}")









