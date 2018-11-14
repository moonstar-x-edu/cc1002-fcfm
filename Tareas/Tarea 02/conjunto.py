# modulo: lista.py
# modulo: lista.py
import estructura

#lista: valor(any) siguiente(lista)
estructura.crear("lista","valor siguiente")
listaVacia=None #lista sin valores

#cabeza: lista -> any
#primer valor de una lista
#ej: cabeza(lista("a",lista("b",None)))->"a"
def cabeza(L):
    assert type(L)==lista
    return L.valor
assert cabeza(lista("a",lista("b",None)))=="a"

#cola: lista -> lista
#devuelve lista sin primer valor
#ej: cola(lista("a",lista("b",None)))->lista("b",None)
#ej: cola(lista("a",None))->None
def cola(L):
    assert type(L)==lista
    return L.siguiente
assert cola(lista("a",lista("b",None))) == lista("b",None)
assert cola(lista("a",None))==None

#esLista: lista -> bool
#True si L es una lista
#ej: esLista(lista(1,None)) -> True
#ej: esLista(0) -> False
def esLista(L) :
  return type(L) == lista or L == None
assert esLista(lista(1, None))
assert not esLista(0)

#enLista: any lista -> bool
#True si x esta en L
#ej: si L=lista(4,lista(5,None)) entonces
#    enlista(5,L)->True, enLista(3,L)->False
def enLista(x,L):
  assert esLista(L)
  if L==None: return False
  if cabeza(L)==x: 
    return True
  else: 
    return enLista(x,cola(L))
L=lista(4,lista(5,None))
assert enLista(5,L)
assert not enLista(3,L)

# modulo: conjunto.py

# esConjunto : lista -> bool
# True si la lista entregada forma un conjunto (no se aceptan elementos repetidos).
# ej: esConjunto(lista(1, lista(2, None))) -> True
# ej: esConjunto(lista(1, lista(1, None))) -> False
def esConjunto(x) :
  assert esLista(x)
  if x == None : return True
  if enLista(cabeza(x), cola(x)) : return False
  else : return esConjunto(cola(x))
assert esConjunto(lista(1, lista(2, None)))
assert not esConjunto(lista(1, lista(1, None)))

# pertenece : int, lista -> bool
# True si el primer argumento pertenece al conjunto (segundo argumento).
# ej: pertenece(1, lista(1, lista(2, None))) -> True
# ej: pertenece(3, lista(1, lista(2, None))) -> False
def pertenece(a, x) :
  assert esConjunto(x) and type(a) == int
  return enLista(a, x)
assert pertenece(1, lista(1, lista(2, None)))
assert not pertenece(3, lista(1, lista(2, None)))

# cardinal : lista -> int
# Entrega el cardinal (numero de elementos) de un conjunto dado.
# ej: cardinal(lista(1, lista(2, None))) -> 2
# ej: cardinal(lista(1, lista(2, lista(3, None)))) -> 3
def cardinal(x) :
  assert esConjunto(x)
  # contarElementos() se encarga de contar los elementos dentro del conjunto, esta funcion interna sirve para proteger el valor i del usuario)
  def contarElementos(x, i=0) :
    if x == None : return i
    return contarElementos(cola(x), i+1)
  return contarElementos(x)
assert cardinal(lista(1, lista(2, None))) == 2
assert cardinal(lista(1, lista(2, lista(3, None)))) == 3

# sub : lista, lista -> bool
# True si el primer conjunto dado es subconjunto del segundo conjunto.
# ej: sub(lista(1, None), lista(1, lista(2, None))) -> True
# ej: sub(lista(1, None), lista(2, lista(3, None))) -> False
def sub(x, y) :
  assert esConjunto(x) and esConjunto(y)
  if x == None : return True
  if pertenece(cabeza(x), y) : return sub(cola(x), y)
  else : return False
assert sub(lista(1, None), lista(1, lista(2, None)))
assert not sub(lista(1, None), lista(2, lista(3, None)))

# igual : lista, lista -> bool
# True si los dos conjuntos dados son iguales.
# ej: igual(lista(1, lista(2, None)), lista(1, lista(2, None))) -> True
# ej: igual(lista(1, lista(2, None)), lista(1, lista(2, lista(3, None)))) -> False
def igual(x, y) :
  assert esConjunto(x) and esConjunto(y)
  if sub(x, y) and sub(y, x) : return True
  else : return False
assert igual(lista(1, lista(2, None)), lista(1, lista(2, None)))
assert not igual(lista(1, lista(2, None)), lista(1, lista(2, lista(3, None))))

# aString : lista -> str
# Transforma un conjunto (lista) a un string con los elementos separados por un espacio.
# ej: aString(lista(1, lista(2, None))) -> "1 2"
# ej: aString(lista(1, None)) -> "1"
def aString(x) :
  assert esConjunto(x)
  if x == None : return ""
  if cola(x) == None : return str(cabeza(x))
  else : return str(cabeza(x)) + " " + aString(cola(x))
assert aString(lista(1, lista(2, None))) == "1 2"
assert aString(lista(1, None)) == "1"

# union : lista, lista -> lista
# Recibe dos conjuntos y entrega la union entre ellos. (Los entrega en el orden inverso del que fueron entregados).
# ej: union(lista(1, lista(2, None)), lista(3, lista(4, None))) -> lista(4, lista(3, lista(2, lista(1, None))))
# ej: union(lista(1, lista(2, lista(3, None))), lista(2, lista(4, None))) -> lista(4, lista(2, lista(3, lista(1, None))))
def union(x, y) :
  assert esConjunto(x) and esConjunto(y)
  # unir() se encarga de unir los dos conjuntos con un parametro por omision, es funcion interna para proteger el valor resultado del usuario.
  def unir(x, y, resultado=None) :
    if x == None : 
      if y == None : return resultado
      resultado = lista(cabeza(y), resultado)
      return unir(None, cola(y), resultado)
    if pertenece(cabeza(x),y) : return unir(cola(x), y, resultado)
    else: 
      resultado = lista(cabeza(x), resultado)
      return unir(cola(x), y, resultado)
  return unir(x, y)
assert union(lista(1, lista(2, None)), lista(3, lista(4, None))) == lista(4, lista(3, lista(2, lista(1, None))))
assert union(lista(1, lista(2, lista(3, None))), lista(2, lista(4, None))) == lista(4, lista(2, lista(3, lista(1, None))))

# inter : lista, lista -> lista
# Recibe dos conjuntos y entrega la interseccion entre ellos. (Los entrega en el orden inverso del que fueron entregados).
# ej: inter(lista(1, lista(2, lista(3, None))), lista(1, lista(3, lista(4, None)))) -> lista(1, lista(3, None))
# ej: inter(lista(1, lista(2, None)), lista(1, lista(2, None))) -> lista(2, lista(1, None))
# ej: inter(lista(1, lista(2, None)), lista(3, lista(4, None))) -> None
def inter(x, y) :
  assert esConjunto(x) and esConjunto(y)
  # intersectar() se encarga de intersectar los dos conjuntos con un parametro por omision, es funcion interna para proteger el valor resultado del usuario.
  def intersectar(x, y, resultado=None) :
    if x == None : return resultado
    if pertenece(cabeza(x),y) :
      resultado = lista(cabeza(x), resultado)
    return intersectar(cola(x), y, resultado)
  return intersectar(x, y)
assert inter(lista(1, lista(2, lista(3, None))), lista(1, lista(3, lista(4, None)))) == lista(3, lista(1, None))
assert inter(lista(1, lista(2, None)), lista(1, lista(2, None))) == lista(2, lista(1, None))
assert inter(lista(1, lista(2, None)), lista(3, lista(4, None))) == None

# resta : lista, lista -> lista
# Recibe dos conjuntos y entrega la resta entre ellos. (Los entrega en el orden inverso del que fueron entregados).
# ej: resta(lista(1, lista(2, None)), lista(2, lista(3, None))) -> lista(1, None)
# ej: resta(lista(1, lista(2, lista(3, None))), lista(3, lista(4, None))) -> lista(1, lista(2, None))
def resta(x, y) :
  assert esConjunto(x) and esConjunto(y)
  # restar() se encarga de hacer la resta de los dos conjuntos con un parametro por omision, es funcion interna para proteger el valor resultado del usuario.
  def restar(x, y, resultado=None) :
    if x == None : return resultado
    if not pertenece(cabeza(x),y) :
      resultado = lista(cabeza(x), resultado)
    return restar(cola(x), y, resultado)
  return restar(x, y)
assert resta(lista(1, lista(2, None)), lista(2, lista(3, None))) == lista(1, None)
assert resta(lista(1, lista(2, lista(3, None))), lista(3, lista(4, None))) == lista(2, lista(1, None))