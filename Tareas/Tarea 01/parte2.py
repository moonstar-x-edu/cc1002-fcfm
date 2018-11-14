import sistemasPosicionales

# aislarBase : int -> int
# Recibe un entero positivo expresado de la forma BNNNNN... donde B corresponde a la base y los N a los digitos del numero. Devuelve la base (el primer digito).
# ej: aislarBase(21010) -> 2
def aislarBase(numero) :
    assert type(numero) == int and numero >= 0
    if numero < 10 :
        return numero
    else :
        return aislarBase(numero/10)
assert aislarBase(21010) == 2

# aislarDigitos : int -> int
# Recibe un entero positivo expresado de la forma BNNNN... donde B corresponde a la base y los N a los digitos del numero. Devuelve los digitos que van despues de la base.
# ej: aislarDigitos(514123) -> 14123
def aislarDigitos(numero) :
    assert type(numero) == int and numero >= 0
    exponente = len(str(numero))-1
    base = aislarBase(numero)
    return numero - base*10**(exponente)
assert aislarDigitos(514123) == 14123

# binario : None -> None
# Convierte a binario enteros positivos expresados en bases numericas posicionales del 3 al 10 y muestra finalmente la cantidad de conversiones correctas.
# ej: binario()
def binario() :
    # usamos una funcion interna para contar cuantas iteraciones correctas se realizan
    def binarioContador(contador=0) :
        base = input("base? ")
        # queremos romper el ciclo si la base es 0
        if base == 0 :
            print contador # mostramos el contador
            return
        # si la base es no esta en el rango 3 - 10, recomenzamos
        elif base < 3 or base > 10 :
            print "base incorrecta"
            return binarioContador(contador)
        n = input("n? ")
        # si el numero no esta bien expresado en su base correspondiente, recomenzamos
        if not sistemasPosicionales.correcto(n, base) :
            print "numero incorrecto"
            return binarioContador(contador)
        # si el numero es un decimal, entonces podemos convertirlo directo en binario
        if base == 10 :
            bin = sistemasPosicionales.otraBase(n, 2)
            print bin
            return binarioContador(contador+1) # contamos esta iteracion exitosa
        # si el numero no es un decimal, lo convertimos en un decimal primero y luego lo pasamos a binario
        else :
            decimal = sistemasPosicionales.base10(n, base)
            bin = sistemasPosicionales.otraBase(decimal, 2)
            print bin
            return binarioContador(contador+1) # contamos esta iteracion exitosa
    return binarioContador() # se ejecuta la funcion interna

#binario()

# menorDecimalLista : None -> None
# Al invocarse, se abre un sistema de dialogo, el usuario inserta un numero expresado de la forma BNNNN... con B la base (de 2 a 9) y N los digitos del entero positivo en aquella base. Este numero es convertido en decimal, luego, si el usuario inserta 0 como su numero, el dialogo termina imprimiendo la informacion del decimal menor convertido.
# ej: menorDecimalLista()
def menorDecimalLista() :
    # usamos una funcion interna para guardar los valores del menor decimal, de su base y de sus digitos
    def guardarMenor(menor=-1, b=0, dig=0) :
        n = input("n? ")
        base = aislarBase(n)
        digitos = aislarDigitos(n)
        # cerramos el ciclo si la base es 0
        if base == 0 :
            print "menor: base=", b, "digitos=", dig, "decimal=", menor
            return
        # si la base esta fuera del rango especificado, recomenzamos
        elif base < 2 or base > 9 :
            print "base incorrecta"
            return guardarMenor(menor, b, dig)
        # si el numero no esta expresado en una base correcta, recomenzamos
        elif not sistemasPosicionales.correcto(digitos, base) :
            print "numero incorrecto"
            return guardarMenor(menor, b, dig)
        else :
            # calculamos el decimal
            decimal = sistemasPosicionales.base10(digitos, base)
            print "decimal=", decimal
            # si el decimal obtenido es inferior al que estaba guardado, se reemplaza por el nuevo decimal inferior. (el caso menor == -1 quiere decir que queremos excluir el valor inicial de menor, dado a que ningun decimal nos puede salir negativo, -1 no puede corresponder a decimal)
            if decimal < menor or menor == -1:
                return guardarMenor(decimal, base, digitos)
            else:
                return guardarMenor(menor, b, dig)
    return guardarMenor() # ejecutamos funcion interna

#menorDecimalLista()
