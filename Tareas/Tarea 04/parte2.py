from Tkinter import *
from Cola import *
from time import time

# Colas
cola1 = Cola(5)
cola2 = Cola(10)
tiempo1 = Cola(cola1.max)
tiempo2 = Cola(cola2.max)
tiempoInicial = time()

# Funciones Datos
# loggingCola : ->
# Imprime en la consola los clientes y sus tiempos de llegada correspondientes cada vez que se hace un cambio en la cola.
def loggingCola() :
    print "Cola(s) modificadas..."
    print " - Clientes en Cola 1:", str(cola1)
    print " - Clientes en Cola 2:", str(cola2)
    print " - Tiempos de llegada 1:", str(tiempo1)
    print " - Tiempos de llegada 2:", str(tiempo2)

# actualizarReloj: ->
# Actualiza el labelReloj, debe ser llamado al final de cada funcion evento. Debe llamarse al final de atenderCola() y agregarCola() [eventos].
def actualizarReloj() :
    tiempoActual = int(time() - tiempoInicial)
    labelReloj.config(text="Reloj: " + str(tiempoActual))
    return

# actualizarLargoCola: ->
# Actualiza los labelLargoCola1 y labelLargoCola2 cada vez que se realiza un cambio en las colas 1 y 2 respectivamente. Debe llamarse al final de atenderCola() y agregarCola() [eventos].
def actualizarLargoCola() :
    labelLargoCola1.config(text=len(cola1))
    labelLargoCola2.config(text=len(cola2))
    return

# actualizarNombreClientes: ->
# Actualiza los labelClientesEsperando1 y labelClientesEsperando2 cada vez que se realiza un cambio en las colas 1 y 2 respectivamente. Debe llamarse al final de atenderCola() y agregarCola() [eventos].
def actualizarNombreClientes() :
    labelClientesEsperando1.config(text=str(cola1))
    labelClientesEsperando2.config(text=str(cola2))
    return

# atenderCaja: ->
# Realiza la accion de atender al primero de la cola 1, si esta cola esta vacia, entonces se atiende al primero de la cola 2.
def atenderCaja() :
    assert isinstance(cola1, Cola) and isinstance(cola2, Cola)
    if not cola1.vacia() :
        labelAtendiendo.config(text="Atendiendo a: " + str(cola1.sacar()))
        tiempoEsperado = int((time() - tiempoInicial) - tiempo1.sacar())
        labelSegundos.config(text="Segundos que espero: " + str(tiempoEsperado))
    else :
        labelAtendiendo.config(text="Atendiendo a: " + str(cola2.sacar()))
        tiempoEsperado = int((time() - tiempoInicial) - tiempo2.sacar())
        labelSegundos.config(text="Segundos que espero: " + str(tiempoEsperado))
    
    loggingCola()
    actualizarNombreClientes()
    actualizarLargoCola()
    actualizarReloj()
    return

# agregarCliente: Cola, Cola, Entry ->
# Agrega el cliente especificado en la entrada(Entry) a la cola(Cola) y su tiempo de llegada a tiempo(Cola).
def agregarCliente(cola, tiempo, entrada) :
    nombre = entrada.get()
    if not nombre == "":
        cola.poner(nombre)
        tiempo.poner(int(time() - tiempoInicial))
        entrada.delete(0, END)

        loggingCola()
        actualizarNombreClientes()
        actualizarLargoCola()
        actualizarReloj()    
    return

# Ventana
ventana = Tk()
ancho = 20

# Marcos
fila1 = Frame(ventana)
fila1.pack()
fila2 = Frame(ventana)
fila2.pack()
fila3 = Frame(ventana)
fila3.pack()
fila4 = Frame(ventana)
fila4.pack()

# Items Marco 1
botonCaja = Button(fila1, text="Caja", width=ancho, command=atenderCaja)
botonCaja.grid(row=0, column=0)
labelAtendiendo = Label(fila1, width=ancho)
labelAtendiendo.grid(row=0, column=1)
labelSegundos = Label(fila1, width=ancho)
labelSegundos.grid(row=0, column=2)
labelReloj = Label(fila1, width=ancho)
labelReloj.grid(row=0, column=3)

# Items Marco 2
Label(fila2, text="Cola", width=ancho).grid(row=1, column=0)
Label(fila2, text="Clientes en la cola", width=ancho).grid(row=1, column=1)
Label(fila2, text="Largo de la cola", width=ancho).grid(row=1, column=2)
Label(fila2, text="Cliente que llega", width=ancho).grid(row=1, column=3)

# Items Marco 3
Label(fila3, text="Cola 1", width=ancho).grid(row=2, column=0)
labelClientesEsperando1 = Label(fila3, width=ancho)
labelClientesEsperando1.grid(row=2, column=1)
labelLargoCola1 = Label(fila3, text=0, width=ancho)
labelLargoCola1.grid(row=2, column=2)
nombreCola1 = Entry(fila3, width=ancho)
nombreCola1.bind("<Return>", (lambda evento: agregarCliente(cola1, tiempo1, nombreCola1)))
nombreCola1.grid(row=2, column=3)

# Items Marco 4
Label(fila4, text="Cola 2", width=ancho).grid(row=3, column=0)
labelClientesEsperando2 = Label(fila4, width=ancho)
labelClientesEsperando2.grid(row=3, column=1)
labelLargoCola2 = Label(fila4, text=0, width=ancho)
labelLargoCola2.grid(row=3, column=2)
nombreCola2 = Entry(fila4, width=ancho)
nombreCola2.bind("<Return>", (lambda evento: agregarCliente(cola2, tiempo2, nombreCola2)))
nombreCola2.grid(row=3, column=3)

ventana.mainloop()