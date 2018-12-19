class Barra() :
    def __init__(self, x, y, ancho, alto) :
        self.__x = x
        self.__y = y
        self.__ancho = ancho
        self.__alto = alto
    
    def x(self) :
        return self.__x
    
    def y(self) :
        return self.__y
    
    def ancho(self) :
        return self.__ancho
    
    def alto(self) :
        return self.__alto
    
    def x2(self) :
        return self.__x + self.__ancho

    def y2(self) :
        return self.__y + self.__alto

    def anchoBarra(self) :
        return self.__x + self.__ancho
    
    def altoBarra(self) :
        return self.__y + self.__alto
    
    def actualizarPos(self, dir) :
        if dir == 1 or dir == -1 :
            self.__x += 20*dir
        else : return

class Bola(Barra) :
    def __init__(self, x, y, cv, bar):
        self.__x = x
        self.__y = y
        self.__velx = 3
        self.__vely = 4
        self.__rad = 20
        self.__ancho = cv.winfo_width()
        self.__alto = cv.winfo_height()
        self.__muerto = False
        self.__bar = bar
        self.__puntos = 0

    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def diam(self):
        return 2*self.__rad

    def x2(self):
        return self.__x + self.diam()
    
    def y2(self):
        return self.__y + self.diam()

    def velx(self):
        return self.__velx

    def vely(self):
        return self.__vely

    def rad(self):
        return self.__rad
    
    def muerto(self):
        return self.__muerto

    def puntos(self):
        return self.__puntos

    # Parece que hay un offset raro en el canvas que hace que el 6 sea el numero
    # minimo para hacer que la bola rebote.
    def actualizarPos(self):
        self.__x += self.__velx
        self.__y += self.__vely

        if self.x2() > self.__ancho :
            self.__velx = -self.__velx
        elif self.__x < 6 :
            self.__velx = -self.__velx
            self.__velx = (self.__velx/abs(self.__velx))*abs(self.__velx)+1
        
        if self.__y < 6 :
            self.__vely = -self.__vely
            self.__vely = (self.__vely/abs(self.__vely))*abs(self.__vely)+1
        elif self.y2() > self.__bar.y() :
            if (self.__x > self.__bar.x() and self.__x <= self.__bar.x2()) or (self.x2() >= self.__bar.x() and self.x2() < self.__bar.x2()) :
                self.__vely = -self.__vely
                self.__puntos += 1
        if self.y2() > self.__alto :
            self.__muerto = True
        