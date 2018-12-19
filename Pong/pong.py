from Tkinter import *
from elementos import *
from random import randint

ANCHO = 400
ALTO = 400
DT = 1000/30

corriendo = False

def actualizarPuntos(puntos) :
  if bola.muerto() :
    labelPuntos.config(text='Game Over, Score = ' + str(puntos))
  else :
    labelPuntos.config(text='Score = ' + str(puntos))

def actualizarBoton() :
  if bola.muerto() :
    boton.config(text='Reset', command=reset)
  else :
    boton.config(text='Run', command=run)

def actualizarCanvas() :
  global corriendo
  if bola.muerto() : 
    corriendo = False
    actualizarPuntos(bola.puntos())
    actualizarBoton()
    return
  cv.after(DT, actualizarCanvas)
  bola.actualizarPos()
  cv.move(elemBola, bola.velx(), bola.vely())
  actualizarPuntos(bola.puntos())
  
def run() :
  global corriendo
  if corriendo : return
  corriendo = True
  actualizarCanvas()

def reset() :
  global corriendo, bola, elemBola
  corriendo = True
  del bola
  cv.delete(elemBola)
  bola = Bola(randint(20, 380), 20, cv, barra)
  elemBola = cv.create_oval(bola.x(), bola.y(), bola.x2(), bola.y2(), fill='red')
  actualizarCanvas()
  actualizarPuntos(bola.puntos())
  actualizarBoton()

def key(event) :
  if bola.muerto() : return
  if event.keysym == 'Left' :
    if barra.x() > 1 :
      barra.actualizarPos(-1) 
      cv.move(elemBarra, -20, 0)
  if event.keysym == 'Right' : 
    if barra.x() + barra.ancho() < ANCHO - 1 :
      barra.actualizarPos(1) 
      cv.move(elemBarra, 20, 0)

ventana = Tk()
frameSuperior = Frame(ventana)
frameSuperior.pack()
labelPuntos = Label(frameSuperior, text='Score = 0', font=('', 20))
labelPuntos.pack(side=LEFT)
boton = Button(frameSuperior, text='Run', height=2, width=10, command=run)
boton.pack()
cv = Canvas(ventana, width=ANCHO, height=ALTO)
cv.pack()
cv.update()

barra = Barra(ANCHO / 2, ALTO - 15, 60, 10)
elemBarra = cv.create_rectangle(barra.x(), barra.y(), barra.anchoBarra(), barra.altoBarra(), fill='black')
bola = Bola(randint(20, 380), 20, cv, barra)
elemBola = cv.create_oval(bola.x(), bola.y(), bola.x2(), bola.y2(), fill='red')

cv.bind('<Key>', key)
cv.focus_set()
ventana.mainloop()