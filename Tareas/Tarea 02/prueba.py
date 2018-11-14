from conjunto import *

# lectura: None -> lista
# Realiza la lectura de los elementos de un conjunto, cuando se inserta el 0, se termina la lectura y se entrega el conjunto generado.
# lectura() -> lista(1, lista(2, None))
def lectura() :
  def obtenerElementos(con=None) :
    assert esConjunto(con)
    nuevoElemento = input("elemento? ")
    if nuevoElemento == 0 : return con
    return obtenerElementos(lista(nuevoElemento, con))
  return obtenerElementos()

# operacion: lista, lista -> lista
# Lee y realiza las operaciones entre dos conjuntos A y B (hasta ingresar la operacion punto) y entrega el conjunto resultado de la operacion.
# operacion(lista(1, None), lista(2, None), suma) -> lista(1, lista(2, None))
def operacion(conjuntoA, conjuntoB) :
  assert esConjunto(conjuntoA)
  assert esConjunto(conjuntoB)
  op = raw_input("Operacion(+*-=<>.)? ")
  if op == "+" :
    resultado = union(conjuntoA, conjuntoB)
    print "A union B=", aString(resultado), "Cardinal=", cardinal(resultado)
    return operacion(conjuntoA, conjuntoB)
  elif op == "*" :
    resultado = inter(conjuntoA, conjuntoB)
    print "A interseccion B=", aString(resultado), "Cardinal=", cardinal(resultado)
    return operacion(conjuntoA, conjuntoB)
  elif op == "-" :
    resultado = resta(conjuntoA, conjuntoB)
    print "A - B=", aString(resultado), "Cardinal=", cardinal(resultado)
    return operacion(conjuntoA, conjuntoB)
  elif op == "=" :
    if igual(conjuntoA, conjuntoB) : resultado = "Si"
    else : resultado = "No"
    print "A = B es ", resultado
    return operacion(conjuntoA, conjuntoB)
  elif op == "<" :
    if sub(conjuntoA, conjuntoB) : resultado = "Si"
    else : resultado = "No"
    print "A subconjunto de B es ", resultado
    return operacion(conjuntoA, conjuntoB)
  elif op == ">" :
    if sub(conjuntoB, conjuntoA) : resultado = "Si"
    else : resultado = "No"
    print "A superconjunto de B es ", resultado
    return operacion(conjuntoA, conjuntoB)
  elif op == "." :
    return
  else :
    print "Operacion invalida."
    return operacion(conjuntoA, conjuntoB)

# escaparDialogo: None -> None
# Sirve para escapar el dialogo prueba(), al entregar "si" se reinicia el dialogo, si se entrega "no" se escapa del dialogo, cualquier otra cosa vuelve a preguntar.
# escaparDialogo()
def escaparDialogo() :
  opcion = raw_input("Otros conjuntos(si/no)? ")
  if opcion == "si" : return prueba()
  elif opcion == "no" : return
  else :
    print "Opcion invalida."
    return escaparDialogo()

# prueba: None -> None
# Realiza un dialogo recursivo para realizar operaciones entre conjuntos.
# prueba()
def prueba() :
  # Se realiza la lectura de ambos conjuntos.
  print "Ingrese elementos Conjunto A (o 0 para terminar)."
  conjuntoA = lectura()
  print "A=", aString(conjuntoA), "Cardinal=", cardinal(conjuntoA)
  print "Ingrese elementos Conjunto B (o 0 para terminar)."
  conjuntoB = lectura()
  print "B=", aString(conjuntoB), "Cardinal=", cardinal(conjuntoB)
  
  # Se realizan las operaciones.
  operacion(conjuntoA, conjuntoB)

  # Se pide al usuario si quiere repetir el dialogo o no.
  escaparDialogo()
  return

# test #
prueba()