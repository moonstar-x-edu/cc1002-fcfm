#agenda: list(list)
agenda=[["a", 2],["c", 1],["d", 4]]

# buscar: str, list -> int
# Entrega el telefono del nombre (argumento) en una agenda (argumento), si no existe, entrega None.
# ej: buscar("a", agenda) -> 2
# ej: buscar("b", agenda) -> None
def buscar(nombre, agenda) :
  assert type(nombre) == str and type(agenda) == list
  for entrada in agenda :
    if nombre == entrada[0] : return entrada[1]
  return None
assert buscar("a", agenda) == 2
assert buscar("b", agenda) == None

# agregar: str, int, list -> list
# Agrega una entrada con nombre y telefono a una agenda, entrega esta nueva agenda ordenada.
# ej: agregar("b", 23, agenda) -> [['a', 2], ['b', 23], ['c', 1], ['d', 4]]
def agregar(nombre, telefono, agenda) :
  assert type(nombre) == str and type(telefono) == int and type(agenda) == list
  agenda.append([nombre, telefono])
  agenda.sort()
  return agenda
assert agregar("b", 23, agenda) == [['a', 2], ['b', 23], ['c', 1], ['d', 4]]

# borrar: str, list -> list
# Borra una entrada (usando solo el nombre) de una agenda y entrega esta nueva agenda sin la entrada especificada (si aplica).
# ej: borrar("a", agenda) -> [["b", 23], ["c", 1],["d", 4]]
def borrar(nombre, agenda) :
  assert type(nombre) == str and type(agenda) == list
  for entrada in agenda :
    if nombre == entrada[0] : agenda.remove(entrada)
  return agenda
assert borrar("a", agenda) == [["b", 23], ["c", 1],["d", 4]]

# cambiar: str, int, list -> list
# Cambia el telefono de la entrada correspondiente al nombre en una agenda. Entrega la agenda actualizada si aplica.
# ej: cambiar("b", 42, agenda) -> [["b", 42], ["c", 1],["d", 4]]
def cambiar(nombre, telefono, agenda) :
  assert type(nombre) == str and type(telefono) == int and type(agenda) == list
  for entrada in agenda :
    if nombre == entrada[0] : entrada[1] = telefono
  return agenda
assert cambiar("b", 42, agenda) == [['b', 42], ['c', 1], ['d', 4]]
