# Abrir archivos.
A = open(raw_input("Archivo input? "), "r")
B = open(raw_input("Archivo output? "), "w")
grabadas = 0
leidas = 0

buscar = raw_input("Copiar valores con string: ")

for linea in A :
  if buscar in linea: 
    B.write(linea)
    grabadas += 1
  leidas += 1

print "Lineas leidas", leidas
print "Lineas grabadas", grabadas
  
A.close()
B.close()