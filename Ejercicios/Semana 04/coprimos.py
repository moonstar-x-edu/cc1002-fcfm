# mayorComunDivisor : int, int -> int
# calcula el mayor comun divisor entre dos enteros positivos
# mayorComunDivisor(12, 25) -> 1
def mayorComunDivisor(a, b) :
    assert type(a) == int and a>=0
    assert type(b) == int and b>=0
    # caso base, llegamos al resultado
    if b == 0 :
        return a
    if a == b :
        return a
    # necesitamos que a sea mayor que b para continuar
    elif a>b :
        r = a%b # resto de la division a por b
        # si el resto es nulo, llegamos al mayor comun divisor
        if r == 0 :
            return b
        # b toma el valor de a y r toma el valor de b para continuar
        else :
            return mayorComunDivisor(b, r)

        print mayorComunDivisor(12, 25)
    # si b es mayor que a, se llama la misma funcion pero con los valores invertidos
    else :
        return mayorComunDivisor(b, a)
assert mayorComunDivisor(134, 28) == 2
assert mayorComunDivisor(12, 25) == 1

# coprimosEnRango : int, int -> None
# escribe coprimos en el rango de enteros entre x e y
# ej: coprimosEnRango(2, 5) -> 2,3 2,5, 3,4 3,5 4,5
def coprimosEnRango(x, y) :
    assert type(x) == int and x>=0
    assert type(y) == int and y>=x # rango tiene que ser valido
    # funcion auxiliar para imprimir los coprimos
    def iterandoEnRango(x, y, xi=x, yi=y) :
        # si x llega al valor y que fue pasado en coprimosEnRango(), termina el ciclo
        if x>yi :
            return "Terminado."
        # si y pasado en iterandoEnRango() llega a ser mayor al y en iterandoEnRango(), se vuelve a iterar esta funcion con un valor de x+1
        if y>yi :
            return iterandoEnRango(xi+1, xi+1, xi+1, yi)
        # si son coprimos, los imprimimos
        if mayorComunDivisor(x, y) == 1 :
            print x, y
        # volvemos a iterar con y+1
        return iterandoEnRango(x, y+1, xi, yi)
    # ejecutamos la funcion auxiliar
    return iterandoEnRango(x, x, x, y)

#print coprimosEnRango(2, 5)
