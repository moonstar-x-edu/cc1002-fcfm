# esConjunto : list -> bool
# True si el list entregado forma un conjunto (no se aceptan elementos repetidos).
# ej: esConjunto([1,2,3]) -> True
# ej: esConjunto([1,2,1]) -> False
def esConjunto(x) :
  assert type(x) == list
  for i in x :
    if x.count(i) > 1 : return False
  return True
assert esConjunto([1,2,3])
assert not esConjunto([1,2,1])

# pertenece : any, list -> bool
# True si el primer argumento pertenece al conjunto (segundo argumento).
# ej: pertenece(1, [1, 2, 3]) -> True
# ej: pertenece(4, [1, 2, 3]) -> False
def pertenece(a, x) :
  assert esConjunto(x)
  return a in x
assert pertenece(1, [1, 2, 3])
assert not pertenece(4, [1, 2, 3])

# cardinal : list -> int
# Entrega el cardinal (numero de elementos) de un conjunto dado.
# ej: cardinal([1, 2]) -> 2
# ej: cardinal([1, 2, 3]) -> 3
def cardinal(x) :
  assert esConjunto(x)
  return len(x)
assert cardinal([1, 2]) == 2
assert cardinal([1, 2, 3]) == 3

# sub : list, list -> bool
# True si el primer conjunto dado es subconjunto del segundo conjunto.
# ej: sub([1, 2], [1, 2, 3]) -> True
# ej: sub([1, 2, 3], [1, 2]) -> False
def sub(x, y) :
  assert esConjunto(x) and esConjunto(y)
  for i in x :
    if not i in y : return False
  return True
assert sub([1, 2], [1, 2, 3])
assert not sub([1, 2, 3], [1, 2])

# igual : list, list -> bool
# True si los dos conjuntos dados son iguales.
# ej: igual([1, 2], [1, 2]) -> True
# ej: igual([1, 2], [1, 2, 3]) -> False
def igual(x, y) :
  assert esConjunto(x) and esConjunto(y)
  return sub(x, y) and sub(y, x)
assert igual([1, 2], [1, 2])
assert not igual([1, 2], [1, 2, 3])

# aString : list -> str
# Transforma un conjunto (list) a un string con los elementos separados por un espacio.
# ej: aString([1, 2]) -> "1 2"
# ej: aString([1]) -> "1"
def aString(x) :
  assert esConjunto(x)
  res = ""
  j = 0
  for i in x :
    res += str(i)
    if j < len(x)-1 : 
      res += " "
      j += 1
  return res
assert aString([1]) == "1"
assert aString([1, 2, 3]) == "1 2 3"

# union : list, list -> list
# Recibe dos conjuntos y entrega la union entre ellos.
# ej: union([1, 2, 3], [4, 5, 6]) -> [1, 2, 3, 4, 5, 6]
# ej: union([1, 2, 3], [2, 3, 4]) -> [1, 2, 3, 4]
def union(x, y) :
  assert esConjunto(x) and esConjunto(y)
  for i in y :
    if not pertenece(i, x) :
      x.append(i)
  return x
assert union([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert union([1, 2, 3], [2, 3, 4]) == [1, 2, 3, 4]

# inter : list, list -> list
# Recibe dos conjuntos y entrega la interseccion entre ellos.
# ej: inter([1, 2, 3], [2, 3, 4]) -> [2, 3]
# ej: inter([1, 2, 3], [1, 2, 3]) -> [1, 2, 3]
# ej: inter([1, 2, 3], [4, 5, 6]) -> None
def inter(x, y) :
  assert esConjunto(x) and esConjunto(y)
  res = []
  for i in x :
    if pertenece(i, y) : res.append(i)
  if res == [] : return None
  return res
assert inter([1, 2, 3], [2, 3, 4]) == [2, 3]
assert inter([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
assert inter([1, 2, 3], [4, 5, 6]) == None

# resta : list, list -> list
# Recibe dos conjuntos y entrega la resta entre ellos.
# ej: resta([1, 2], [2, 3]) -> [1]
# ej: resta([1, 2], [3, 4]) -> [1, 2]
# ej: resta([1, 2], [1, 2]) -> None
def resta(x, y) :
  assert esConjunto(x) and esConjunto(y)
  for i in y :
    if pertenece(i, x) :
      x.remove(i)
  if x == [] : return None
  return x
assert resta([1, 2], [2, 3]) == [1]
assert resta([1, 2], [3, 4]) == [1, 2]
assert resta([1, 2], [1, 2]) == None