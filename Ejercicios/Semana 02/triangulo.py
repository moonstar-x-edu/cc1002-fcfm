# perimetro: num, num, num -> num
# calcular perimetro de un triangulo.
# ej: perimetro(3, 4, 5) -> 12
def perimetro(a, b, c) :
    assert a > 0 and b > 0 and c > 0 # asegurarse que los valores insertados sean positivos y no nulos.
    return a+b+c
assert perimetro(3, 4, 5) == 12

# area: num, num, num -> float
# calcular el area de un triangulo.
# ej: area(3, 4, 5) -> 6.0
def area(a, b, c) :
    assert a > 0 and b > 0 and c > 0 # asegurarse que los valores insertados sean positivos y no nulos.
    s = perimetro(a, b, c)/2.0
    return (s*(s-a)*(s-b)*(s-c))**0.5
assert area(3, 4, 5) == 6.0

# esTriangulo: num, num, num -> bool
# verificar que los valores insertados forman un triangulo valido segun el teorema de la desigualdad triangular.
# ej: esTriangulo(3, 4, 5) -> True
# ej: esTriangulo(1, 2, 3) -> False
def esTriangulo(a, b, c) :
    if a > 0 and b > 0 and c > 0:
        if a+b>c and b+c>a and a+c>c:
            return True
        else :
            return False
    else :
        return False
assert esTriangulo(3, 4, 5)
assert not esTriangulo(1, 2, 3)

# tipo: num, num, num -> str
# ver si un triangulo es equilatero, escaleno o isosceles.
# ej: tipo(3, 3, 3) -> "equilatero"
# ej: tipo(3, 5, 4) -> "escaleno"
# ej: tipo(3, 3, 4) -> "isosceles"
def tipo(a, b, c) :
    if a == b and a == c :
        return "equilatero"
    elif a != b and a != c :
        return "escaleno"
    else :
        return "isosceles"
assert tipo(3, 3, 3) == "equilatero"
assert tipo(3, 5, 4) == "escaleno"
assert tipo(3, 3, 4) == "isosceles"
