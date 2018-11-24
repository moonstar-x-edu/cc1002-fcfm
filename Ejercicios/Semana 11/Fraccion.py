#numerador : int
#denominador : int
class Fraccion:
  def __init__(self,x=0,y=1):
    if type(x)==str:
      i=x.find("/") 
      self.numerador=int(x[0:i]) 
      self.denominador=int(x[i+1:])

    elif isinstance(x,Fraccion):
      self.numerador=x.numerador
      self.denominador=x.denominador

    else:
      assert type(x)==int and type(y)==int
      self.numerador=x
      self.denominador=y
    assert self.denominador!=0

  def __add__(self,x):
    assert isinstance(x,Fraccion) 
    num=self.numerador * x.denominador + \
        self.denominador * x.numerador
    den=self.denominador * x.denominador
    return Fraccion(num,den)
  
  def __sub__(self,x):
    assert isinstance(x,Fraccion) 
    num=self.numerador * x.denominador - \
        self.denominador * x.numerador
    den=self.denominador * x.denominador
    return Fraccion(num,den)
  
  def __mul__(self,x):
    assert isinstance(x,Fraccion) 
    num=self.numerador * x.numerador
    den=self.denominador * x.denominador
    return Fraccion(num,den)
  
  def __div__(self,x):
    assert isinstance(x,Fraccion) 
    num=self.numerador * x.denominador
    den=self.denominador * x.numerador
    return Fraccion(num,den)

  def __str__(self):
    return str(self.numerador) + "/" + str(self.denominador)

  def __gt__(self,x):
    return self.numerador   * x.denominador \
         > self.denominador * x.numerador

  def __eq__(self,x):
    return self.numerador   * x.denominador \
        == self.denominador * x.numerador

# -------------------- Programa Interactivo -------------------- #
print "Calculadora de Fracciones"
frac1 = Fraccion(raw_input("Fraccion 1(n/n)? "))
frac2 = Fraccion(raw_input("Fraccion 2(n/n)? "))
op = raw_input("Operacion (+ - * /)? ")

def resultado(frac1, frac2, op) :
  assert isinstance(frac1, Fraccion) and isinstance(frac2, Fraccion)
  if op == "+" :
    return frac1 + frac2
  elif op == "-" :
    return frac1 - frac2
  elif op == "*" :
    return frac1 * frac2
  elif op == "/" :
    return frac1 / frac2
  else :
    print "Invalido"

print "Resultado =", resultado(frac1, frac2, op)