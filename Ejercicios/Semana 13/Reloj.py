#manejo de un contador modulo limite
#__valor: int
#__limite: int
class Contador:
    #__init__: int int -> Contador
    # contador con valor en rango [0,limite[
    #ej: C=Contador(0,10)
    def __init__(self,valor=0,limite=100):
        assert type(limite)==int and limite>0
        self.__limite=limite
        assert type(valor)==int and \
               0<=valor and valor<limite 
        self.__valor=valor
    
    #getValor: -> int
    # devuelve valor de objeto self
    # ej: C.getValor() -> 50
    def getValor(self):
        return self.__valor
    
    #setValor: int -> 
    # reemplaza valor de objeto self
    # si es >= limite, no hacer nada
    # ej: C.setValor(10) -> C.getValor()==10
    def setValor(self,valor):
        assert type(valor)==int and valor>=0
        if valor<self.__limite:
            self.__valor=valor
    
    #incrementar: -> 
    #suma 1 a valor de self (modulo limite)
    #ej: C.incrementar() -> C.getValor()==1
    def incrementar(self):
      self.__valor=(self.__valor+1) % self.__limite

    #__str__: -> str
    #string con valor de self 
    #(si menor que 10 anteponer 0)
    #ej: str(C) -> "08"
    def __str__(self):
        n=self.__valor
        if n<10:
            return "0"+str(n)
        else:
            return str(n)

#clase para test de clase Contador
class TestContador:
    def __init__(self):
        self.C = Contador(0,limite=3)
    def test(self):
        assert self.C.getValor()==0
        self.C.incrementar()
        assert self.C.getValor()==1
        self.C.incrementar()
        assert self.C.getValor()==2
        self.C.incrementar()
        assert self.C.getValor()==0
        self.C.incrementar()
        assert str(self.C)=="01"
        self.C.setValor(2)
        assert self.C.getValor()==2
test=TestContador()
test.test()


#__horas:   Contador (modulo 24)
#__minutos: Contador (modulo 60)
#__segundos: Contador (modulo 60)
class Reloj:
  #__init__: int, int -> Reloj
  #crear reloj a la hora y minutos indicados
  #ej: R=Reloj(23,58)
  def __init__(self,horas=0,minutos=0,segundos=0):
    assert type(horas)==int and type(minutos)==int and type(segundos)==int
    self.__horas=Contador(horas,24)
    self.__minutos=Contador(minutos,60)
    self.__segundos=Contador(segundos,60)

  #tic: ->
  #avanzar el reloj en un minuto
  #ej: R.tic() -> str(R)=="23:59"
  def tic(self):
    self.__segundos.incrementar()
    if self.__segundos.getValor()==0:
      self.__minutos.incrementar()
      if self.__minutos.getValor()==0:
        self.__horas.incrementar()

  #setReloj: int int -> None
  #fijar la hora del reloj en horas y minutos
  #ej: R.setReloj(23,58) -> str(R)=="23:58"
  def setReloj(self,horas=0,minutos=0,segundos=0):
    assert type(horas)==int and type(minutos)==int and type(segundos)==int
    self.__horas.setValor(horas)
    self.__minutos.setValor(minutos)
    self.__segundos.setValor(segundos)

  #__str__: None -> str
  #string con valor de self
  #ej: str(R) -> "23:58"
  def __str__(self):
    return str(self.__horas) + ":" + \
           str(self.__minutos) + ":" + \
           str(self.__segundos)

# clase para test de Reloj
class TestReloj:
  def __init__(self):
    self.R = Reloj(23,58,58)
  def test(self):
    assert str(self.R)=="23:58:58"
    self.R.tic()
    self.R.tic()
    assert str(self.R)=="23:59:00"
    for _ in range(0,60) :
      self.R.tic()
    assert str(self.R)=="00:00:00"
    self.R.setReloj(15,35,10)
    assert str(self.R)=="15:35:10"
    self.R.tic()
    assert str(self.R)=="15:35:11"