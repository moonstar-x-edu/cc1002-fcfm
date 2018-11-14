import estructura

#fraccion: numerador(int) denominador(int)
estructura.crear("fraccion","numerador denominador")

#esFraccion: fraccion -> bool
#True si x es una fraccion valida
#ej: esFraccion(fraccion(1,2))->True
#ej: esFraccion(fraccion(1,0))->False
def esFraccion(x):
    return type(x)==fraccion \
       and type(x.numerador)==int \
       and type(x.denominador)==int \
       and x.denominador!=0
assert esFraccion(fraccion(1,2))
assert not esFraccion(fraccion(1,0))

# mcd : int, int -> int
# calcula el mayor comun divisor entre dos enteros positivos
# mcd(12, 25) -> 1
def mcd(a, b) :
    assert type(a) == int and a>=0
    assert type(b) == int and b>=0
    # caso base, llegamos al resultado
    if b == 0 :
        return a
    if a == b :
        return a
    # necesitamos que a sea mayor que b para continuar
    elif a>b :
        r = a%b # resto de la division a por b
        # si el resto es nulo, llegamos al mayor comun divisor
        if r == 0 :
            return b
        # b toma el valor de a y r toma el valor de b para continuar
        else :
            return mcd(b, r)

        print mcd(12, 25)
    # si b es mayor que a, se llama la misma funcion pero con los valores invertidos
    else :
        return mcd(b, a)
assert mcd(134, 28) == 2
assert mcd(12, 25) == 1

#simplificar: fraccion -> fraccion
#fraccion con valor de fraccion x simplificada
#ej: simplificar(fraccion(2,4))->fraccion(1,2)
def simplificar(x):
  assert esFraccion(x)
  m=mcd(x.numerador,x.denominador)
  return fraccion(x.numerador/m, x.denominador/m)
assert simplificar(fraccion(2,4))==fraccion(1,2)

#aString: fraccion -> str
#convierte fraccion x a string
#ej: aString(fraccion(1,2))->"1/2"
def aString(x):
  assert esFraccion(x) 
  return str(x.numerador)+"/"+str(x.denominador)
assert aString(fraccion(1,2)) == "1/2"

def mostrar(x,f):
  print x, aString(simplificar(f))

#suma: fraccion fraccion -> fraccion
#suma de fracciones x e y
#ej: suma(fraccion(1,2),fraccion(3,4))->fraccion(10,8)
def suma(x,y):
  assert esFraccion(x)
  assert esFraccion(y)
  num = x.numerador * y.denominador + \
        x.denominador * y.numerador
  den = x.denominador * y.denominador
  return fraccion(num,den)
assert suma(fraccion(1,2),fraccion(3,4))==fraccion(10,8)

#comparar: fraccion fraccion -> int
#0 si x==y, n>0 si x>y, n<0 si x<y
#ej: comparar(fraccion(1,2),fraccion(2,4))->0
#ej: comparar(fraccion(1,2),fraccion(1,3))->n>0
#ej: comparar(fraccion(1,3),fraccion(1,2))->n<0
def comparar(x,y):
  assert esFraccion(x) and esFraccion(y)
  return x.numerador   * y.denominador - \
         x.denominador * y.numerador
assert comparar(fraccion(1,2),fraccion(2,4))==0
assert comparar(fraccion(1,2),fraccion(1,3))>0
assert comparar(fraccion(1,3),fraccion(1,2))<0

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

#filtro: lista (any any->bool) any -> lista
#lista con valores de L que cumplen funcion con x
#ej:filtro(lista(5,lista(4,None)),menorQue,5)->lista(4,None)
def filtro(L,funcion,x):
  assert esLista(L)
  if L==None: return None
  if funcion(cabeza(L),x):
    return lista(cabeza(L),filtro(cola(L),funcion,x))
  else:
    return filtro(cola(L),funcion,x)

#test
def menorQue(x,y): return x<y
assert filtro(lista(5,lista(4,None)),menorQue,5)==lista(4,None)

#mapa: lista (any->any) -> lista
#lista aplicando funcion a valores de L
def mapa(L, funcion):
  assert esLista(L)
  if L==None: 
    return None
  else:
    return lista(funcion(cabeza(L)),\
                 mapa(cola(L),funcion))
from math import *
assert mapa(lista(9,lista(25,None)),sqrt)== \
            lista(3.0,lista(5.0,None))
assert mapa(lista('ana',lista('juan',None)),len) == \
       lista(3,lista(4,None))

#reductor: lista (any any->any) any -> any
#funcion con todos los valores de L
#acumulando en resultado
def reductor(L,funcion,resultado):
  assert type(L)==lista
  r=funcion(resultado,cabeza(L))
  if cola(L)==None:
    return r
  else:
    return reductor(cola(L),funcion,r)

#--------------- Ejercicio ---------------#
def menorQueFrac(f1, f2) :
  # precondiciones se chequean en funcion comparar
  if comparar(f1, f2) < 0 : return True
  else : return False

# selectFracsMenores : lista, fraccion -> lista
# Recibe una lista de fracciones y una fraccion minima, entrega una lista de fracciones que sean inferiores a esta fraccion minima por comparacion.
# selectFracsMenores(lista(fraccion(1,3), None), fraccion(1,2)) -> lista(fraccion(1,3), None)
# selectFracsMenores(lista(fraccion(1,2), None), fraccion(1,3)) -> None
def selectFracsMenores(L, min) :
  assert esFraccion(min) # precondiciones para L se chequean en funcion filtro
  return filtro(L, menorQueFrac, min)
assert selectFracsMenores(lista(fraccion(1,3), None), fraccion(1,2)) == lista(fraccion(1,3), None)
assert selectFracsMenores(lista(fraccion(1,2), None), fraccion(1,3)) == None

# simplificarLista : lista -> lista
# Recibe una lista de fracciones y entrega una lista de aquellas fracciones simplificadas.
# simplificarLista(fraccion(2,4), lista(fraccion(3,6), None)) -> lista(fraccion(1,2), lista(fraccion(1,2), None))
def simplificarLista(L) :
  # precondiciones se chequean en funcion simplificar y mapa
  return mapa(L, simplificar)
assert simplificarLista(lista(fraccion(2,4), lista(fraccion(3,6), None))) == lista(fraccion(1,2), lista(fraccion(1,2), None))

# sumarListaFrac : lista -> fraccion
# Recibe una lista de fracciones y entrega una fraccion simplificada con la suma de todas las fracciones de aquella lista.
# sumarListaFrac(lista(fraccion(1,2), lista(fraccion(2,2), None))) -> fraccion(3,2)
def sumarListaFrac(L) :
  # precondiciones se chequean en funcion suma y reductor
  return simplificar(reductor(L, suma, fraccion(0,1)))
assert sumarListaFrac(lista(fraccion(1,2), lista(fraccion(2,2), None))) == fraccion(3,2)