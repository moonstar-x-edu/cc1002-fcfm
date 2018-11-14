# aislarUnidad : int -> int
# Recibe un entero positivo y devuelve su unidad (ultimo digito). (FUNCION AUXILIAR)
# aislarUnidad(4) -> 4
# aislarUnidad(123) -> 3
def aislarUnidad(entero) :
    assert type(entero) == int and entero >= 0
    if entero < 10 :
        return entero
    else :
        paraAislar = entero / 10 # separamos todos los digitos ademas del ultimo
        return entero - paraAislar*10 # aislamos el ultimo digito
assert aislarUnidad(4) == 4
assert aislarUnidad(123) == 3

# correcto: int, int -> bool
# Recibe dos enteros positivos: un numero y una base, se asegura que el numero entero positivo que se entrega sea valido para la base que se entrega. La base puede ser un entero entre 2 y 10.
# correcto(45, 2) -> False
# correcto(45, 10) -> True
# correcto(45, 6) -> True
def correcto(numero, base) :
    # precondiciones: se asegura que el numero sea entero positivo y que la base sea un entero entre 2 y 10.
    assert type(numero) == int and numero >= 0
    assert type(base) == int and 2 <= base and base <= 10
    # si la base es 10, no tiene sentido continuar
    if base == 10 :
        return True
    if numero > 9 :
        unidad =  aislarUnidad(numero)
        # se prueba si es un numero inferior a la base
        if unidad / base < 1 :
            return correcto(numero/10, base) # se vuelve a correr la funcion sin el ultimo digito
        else :
            return False
    else :
        # se prueba si es un numero inferior a la base
        if numero / base < 1:
            return True
        else :
            return False
assert not correcto(45, 2)
assert correcto(45, 10)
assert correcto(45, 6)

# base10: int, int -> int
# Recibe dos argumentos: un entero positivo y una base (entero del 2 al 10), convierte un numero de base dada a su equivalente en decimal (base 10).
# base10(100110101, 2) -> 309
# base10(2375, 8) -> 1277
def base10(numero, base) :
    # precondiciones: se asegura que el numero sea entero positivo, que la base sea un entero entre 2 y 10 y que el numero corresponda efectivamente a la base especificada.
    assert type(numero) == int and numero >= 0
    assert type(base) == int and 2 <= base and base <= 10
    assert correcto(numero, base)
    # si la base es 10, no tiene sentido continuar
    if base == 10 :
        return numero
    # se define una funcion interna para guardar el nivel y la suma.
    def funcionSuma(numero, base, nivel=0, suma=0) :
        if numero > 9 :
            unidad = aislarUnidad(numero) # obtenemos solo la unidad
            suma += unidad*base**nivel # sumamos lo que teniamos antes como suma y la unidad multiplicada por la base elevada al numero de iteracion.
            nivel += 1 # le agregamos uno al numero de iteracion.
            return funcionSuma(numero/10, base, nivel, suma) # volvemos a realizar base10() con el numero dividido por 10.
        else :
            suma += numero*base**nivel
            return suma
    return funcionSuma(numero, base) # llamamos a la funcion interna
assert base10(100110101, 2) == 309
assert base10(2375, 8) == 1277

# otraBase: int, int -> int
# Recibe dos argumentos: un entero positivo y una base (entero del 2 al 10), convierte un decimal (base 10) a su equivalente en otra base dada.
# otraBase(45, 2) -> 101101
# otraBase(101101, 8) -> 305355
def otraBase(decimal, base) :
    # precondiciones: se asegura que el decimal sea entero positivo, que la base sea un entero entre 2 y 10 y finalmente que el decimal sea efectivamente un decimal.
    assert type(decimal) == int and decimal >= 0
    assert type(base) == int and 2 <= base and base <= 10
    assert correcto(decimal, 10)
    # si la base es 10, no tiene sentido continuar
    if base == 10 :
        return decimal
    # se define una funcion interna para guardar el valor del resultado entre iteraciones
    def funcionResultado(decimal, base, resultado="") :
        if decimal > 0 :
            tempDecimal = decimal / base # divide el decimal por la base para obtener el siguiente decimal que se asignara a la funcion
            tempResultado = str(decimal % base) + resultado  # concatena el resultado que se obtiene en esta iteracion y el resultado previo en un string
            return funcionResultado(tempDecimal, base, tempResultado)
            # el final de esta funcion recursiva se marca cuando decimal es 0
        else :
            return int(resultado) #entrega el resultado convertido en int (antes era str)
    return funcionResultado(decimal, base, resultado="") # llamamos a la funcion interna
assert otraBase(45, 2) == 101101
assert otraBase(101101, 8) == 305355
