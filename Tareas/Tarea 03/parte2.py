from conjunto import *

# Abrir listas de alumnos.
A = open("A.txt", "r")
B = open("B.txt", "r")
C = open("C.txt", "r")

# Cargar listas de alumnos en un list para usar modulo conjunto.

# generarList : file -> list(str)
# Entrega un list a partir de un archivo.
# ej: generarList(A) -> [linea1, linea2, linea3...]
def generarList(archivo) :
  resultado = []
  for linea in archivo :
    resultado += [linea[:-1]] # Quita el \n (newline) del string de cada linea. Los archivos tienen que terminar por una linea en blanco, caso contrario se come el ultimo caracter del string.
  return resultado

listA = generarList(A)
listB = generarList(B)
listC = generarList(C)

# Realizar operaciones conjuntos.
inter1 = inter(listA, listB) # Alumnos en cursos A y B.
inter2 = inter(listB, listC) # Alumnos en cursos B y C.
inter3 = inter(listA, listC) # Alumnos en cursos A y C.
unionAlumnos = union(union(listA, listB), listC) # Lista de todos los alumnos.

# Alumnos en los 3 cursos:
listTresCursos = inter(inter1, listC) # Interseccion entre alumnos en A, B y C.

#Alumnos en los 2 cursos:
listDosCursos = resta(union(union(inter1, inter2), inter3), listTresCursos) # Union de las intersecciones AB, BC y AC y restando la interseccion ABC.

#Alumnos en un solo curso:
listUnCurso = resta(resta(unionAlumnos, listDosCursos), listTresCursos) # Restamos la lista de todos los alumnos con los que se encuentran en dos cursos y los que estan en 3 tambien.

# Entrega de datos

# imprimir : list(str) -> None
# Imprime los datos del list (cardinal y items como string).
# ej: imprimir(listUnCurso)
def imprimir(lista) :
  assert esConjunto(lista)
  print " - Numero de alumnos:", cardinal(lista)
  print " - Nombres de los alumnos:", aString(lista)
  return

print "Alumnos que esten cursando los tres cursos:"
imprimir(listTresCursos)
print "Alumnos que esten cursando solo dos de los tres cursos:"
imprimir(listDosCursos)
print "Alumnos que esten cursando en solo uno de los tres cursos:"
imprimir(listUnCurso)