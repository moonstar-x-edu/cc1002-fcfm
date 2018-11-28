from Tkinter import *
import math

# h, v: int (coordenadas horizontal y vertical)
# cv : Canvas
# angulo : float (en radianes)
class Tortuga:
    # __init__ : int, int, Canvas -> Tortuga
    # Crea tortuga en coordenadas (x, y) de canvas cv con angulo 0.
    # ej: t = Tortuga(W / 2, H / 2, cv)
    def __init__(self, x, y, cv) :
        self.__h = x
        self.__v = y
        self.__cv = cv
        self.__angulo = 0
    
    # girar : int -> None
    # Girar tortuga en angulo x, (sumar x al angulo).
    # ej: t.girar(45)
    def girar(self, x) :
        self.__angulo += x
    
    # avanzar : int -> None
    # Avanzar tortuga x pixeles. (dibujando linea)
    # ej: t.avanzar(50)
    def avanzar(self, x) :
        hNuevo = self.__h + math.cos(self.__angulo) * x
        vNuevo = self.__v + math.sin(self.__angulo) * x
        self.__cv.create_line(self.__h, self.__v, hNuevo, vNuevo)
        self.__h = hNuevo
        self.__v = vNuevo

ventana = Tk()
ancho = 200
alto = 200
cv = Canvas(ventana, width=ancho, height=alto)
cv.pack()

# Cuadrado
t1 = Tortuga(ancho * 0.25, alto * 0.25, cv)
t1.avanzar(20)
t1.girar(math.pi / 2)
t1.avanzar(20)
t1.girar(math.pi / 2)
t1.avanzar(20)
t1.girar(math.pi / 2)
t1.avanzar(20)

# Triangulo
t2 = Tortuga(ancho * 0.75, alto * 0.25, cv)
t2.avanzar(20)
t2.girar(2 * math.pi / 3)
t2.avanzar(20)
t2.girar(2 * math.pi / 3)
t2.avanzar(20)

# Pentagono
t3 = Tortuga(ancho * 0.5, alto * 0.75, cv)
t3.avanzar(20)
t3.girar(0.4 * math.pi)
t3.avanzar(20)
t3.girar(0.4 * math.pi)
t3.avanzar(20)
t3.girar(0.4 * math.pi)
t3.avanzar(20)
t3.girar(0.4 * math.pi)
t3.avanzar(20)

ventana.mainloop()