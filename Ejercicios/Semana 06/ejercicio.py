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

#AB: valor(any), izq(AB), der(AB)
estructura.crear("AB","valor izq der")

A=AB(4, \
  AB(2,AB(1,None,None),AB(3,None,None)),\
  AB(6,AB(5,None,None),None))

#esAB: any -> bool
#True si x es un AB
#ej: esAB(A)->True
#ej: esAB(None)->True
def esAB(x):
  return x==None or type(x)==AB
assert esAB(A)
assert esAB(None)


#--------------- Ejercicio ---------------#

# aLista : AB -> lista
# Convertir A a lista (ordenada por valores).
# aLista(AB(4,AB(2,AB(1,None,None),AB(3,None,None)), AB(6,AB(5,None,None),None))) -> lista(1, lista(2, lista(3, lista(4, lista(5, lista(6, None))))))
def aLista(A) :
  assert esAB(A)
  if A == None : return
  aLista(A.der, l)
  l = lista(A.valor, l)
  aLista(A.izq,l)
  if A == None : return l
