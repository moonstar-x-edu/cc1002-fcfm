import turtle

# fractal: int, int -> none
# dibuja un fractal de Koch en version cuadrada haciendo uso de la funcion lado, definida posteriormente, n corresponde al orden del fractal y L al largo de cada segmento principal, si se omite este valor, el lado sera 200 pixeles por defecto.
# fractal(1, 100) -> "se dibuja un cuadrado en la ventana turtle"
def fractal(n,L=200) :
    assert type(n) == int and n>=1
    assert type(L) == int and L>0
    lado(n,L)
    turtle.right(90)
    lado(n,L)
    turtle.right(90)
    lado(n,L)
    turtle.right(90)
    lado(n,L)

# lado: int, int, int -> none
# dibuja cada lado del fractal de Koch version cuadrada, n corresponde al orden del fractal, L al largo de cada lado (en pixeles), si no se define, toma por defecto el valor de 200px, Lmin corresponde al largo minimo de cada lado, por defecto es 6px. debe de invocarse por fractal().
# lado(1, 100, 6) -> "se dibuja una linea"
def lado(n,L=200,Lmin=6) :
    assert type(n) == int and n>=1
    assert type(L) == int and L>0
    if n==1 or L<Lmin :
        turtle.forward(L)
    else :
        lado(n-1,L/3)
        turtle.left(90)
        lado(n-1,L/3)
        turtle.right(90)
        lado(n-1,L/3)
        turtle.right(90)
        lado(n-1,L/3)
        turtle.left(90)
        lado(n-1,L/3)

#-------------------------- programa interactivo --------------------------#

# inicializacion de turtle
turtle.getscreen()
turtle.resetscreen()

# pedir valores de orden y de largo al usuario
n = input("nivel: ")
L = input("largo: ")

# inicia el trazado
fractal(n)

# marca el final del trazado y mantiene la ventana del turtle abierta hasta que se cierre por el usuario
turtle.done()
