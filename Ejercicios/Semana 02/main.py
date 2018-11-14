import triangulo #importar modulo triangulo

#pedir valor de lados al usuario.
print "Inserte valores de los lados de su triangulo:"
a = input()
b = input()
c = input()

#calcular perimetro y area.
perimetro = triangulo.perimetro(a, b, c)
area = triangulo.area(a, b, c)
tipo = triangulo.tipo(a, b, c)

#verificar que el triangulo es valido.
if triangulo.esTriangulo(a, b, c) :
    print "El triangulo es de tipo:", tipo
    print "El perimetro del triangulo es:", perimetro
    print "El area del triangulo es:", area
else :
    print "Triangulo invalido por el teorema de la desigualdad de triangulos."
