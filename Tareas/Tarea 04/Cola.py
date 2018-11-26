# __L : list
# __max : int
class Cola:
  #__init__ : int -> Cola
  # Crea un objeto de clase Cola de largo maximo n. Devuelve una referencia al objeto.
  # ej: Cola() -> referencia a objeto
  def __init__(self, n) :
    assert type(n) == int and n > 0
    self.__max = n
    self.__L = []
  
  # poner : any -> 
  # Agrega un valor al final de la cola.
  # ej: poner(1)
  # ej: poner(2)
  def poner(self, x) :
    assert len(self.__L) <= self.__max-1 
    self.__L.append(x)
  
  # sacar : -> any
  # Saca y entrega el primer valor de la cola.
  # ej: sacar() -> 1
  def sacar(self) :
    return self.__L.pop(0)

  # vacia : -> bool
  # True si la cola esta vacia.
  # ej: vacia() -> False
  def vacia(self) :
    return len(self.__L) == 0
  
  # llena: -> bool
  # True si la cola esta llena.
  # ej: llena() -> False
  def llena(self) :
    return len(self.__L) == self.__max

  # len: Cola -> int
  # Entrega el largo de una cola.
  # ej: len(c) -> 1
  def __len__(self) :
    i = 0
    for item in self.__L :
      i += 1
    return i

  # str : Cola -> str
  # Entrega un string con los elementos de una cola separados por espacio.
  # ej: str(c) -> "2"
  def __str__(self) :
    res = ""
    j = 0
    for i in self.__L :
      res += str(i)
      if j < len(self.__L)-1 : 
        res += " "
        j += 1
    return res

# __c : Cola
class TestCola:
  def __init__(self, n):
    self.__c = Cola(n)
  def test(self):
    self.__c.poner(1)
    assert len(self.__c) == 1
    assert str(self.__c) == "1"
    assert not self.__c.llena()
    self.__c.poner(2)
    assert len(self.__c) == 2
    assert str(self.__c) == "1 2"
    self.__c.poner(3)
    assert len(self.__c) == 3
    assert str(self.__c) == "1 2 3"
    assert not self.__c.vacia()
    assert self.__c.llena()
    assert self.__c.sacar() == 1
    assert self.__c.sacar() == 2
    assert self.__c.sacar() == 3
    assert self.__c.vacia()

# test
t = TestCola(3)
t.test()