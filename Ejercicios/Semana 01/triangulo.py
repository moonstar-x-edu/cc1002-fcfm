# perimetro: num, num, num -> num
# calcular perimetro de un triangulo.
# ej: perimetro(4, 5, 6) -> 15
def perimetro(a, b, c) :
    return a+b+c
assert perimetro(4,5,6) == 15

# area: num, num, num -> float
# calcular el area de un triangulo siempre y cuando este sea valido.
# ej: area(4, 5, 6) -> 9.92
def area(a, b, c) :
    s = perimetro(a, b, c)/2.0
    if a+b>c and b+c>a and a+c>c:
        return (s*(s-a)*(s-b)*(s-c))**0.5
    else:
        return 0
#assert area(4,5,6) == 9.92
