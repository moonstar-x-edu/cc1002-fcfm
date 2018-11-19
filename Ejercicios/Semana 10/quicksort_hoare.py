from random import randint

# generarListaRandom : int -> list(int)
# Entrega una lista de tamano n de enteros aleatorios entre 1 y 100.
# ej: generarListaRandom(2) -> [34, 61]
def generarListaRandom(n) :
  assert type(n) == int and n > 0
  lista = []
  for i in range(n) :
    lista += [randint(1, 100)]
  return lista

# ordenada : list(any) -> bool
# Entrega True si la lista esta ordenada.
# ej: ordenada([1, 2, 3, 4, 5]) -> True
# ej: ordenada([1, 3, 6, 2, 1]) -> False
def ordenada(lista) :
  assert type(lista) == list
  for i in range(1, len(lista)-1) :
    if lista[i] > lista[i+1] : 
      return False
  return True
assert ordenada([1, 2, 3, 4, 5])
assert not ordenada([1, 3, 6, 2, 1])

# Quicksort de Bentley
def quicksort(L) :
  def particionar(L, ip, iu) :
    pivote = L[ip]
    i = ip + 1
    j = iu
    while i <= j :
      while i <= j and L[i] < pivote : 
        i += 1
      while i <= j and L[j] >= pivote : 
        j -= 1
      if i <= j :
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1
    L[ip] = L[j]
    L[j] = pivote
    return j
  
  def qsort(L, ip, iu) :
    if ip >= iu : return
    i = particionar(L, ip, iu)
    qsort(L, ip, i-1)
    qsort(L, i+1, iu)
  assert type(L) == list
  qsort(L, 0, len(L)-1)

# Testing
listaRandom = generarListaRandom(100)

print listaRandom
print ordenada(listaRandom)

quicksort(listaRandom)

print listaRandom
print ordenada(listaRandom)