import fractalCuadrado
import turtle

# inicializacion de turtle
turtle.getscreen()
turtle.resetscreen()

# pedir valores de orden y de largo al usuario
n = input("nivel: ")
L = input("largo: ")

# inicia el trazado
fractalCuadrado.fractal(n)

# marca el final del trazado y mantiene la ventana del turtle abierta hasta que se cierre por el usuario
turtle.done()
