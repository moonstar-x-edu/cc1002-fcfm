import triangulo #importar modulo triangulo

#pedir valor de lados al usuario.
print "Inserte valores de los lados de su triangulo:"
a = input()
b = input()
c = input()

#calcular perimetro y area.
perimetro = triangulo.perimetro(a, b, c)
area = triangulo.area(a, b, c)

#verificar que el triangulo es valido.
if area!=0:
    print "El perimetro del triangulo es:", triangulo.perimetro(a, b, c)
    print "El area del triangulo es:", area
else:
    print "Triangulo invalido por el teorema de la desigualdad de triangulos."
