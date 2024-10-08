import math

x = 0.5
gfuncion = math.exp(-x)
numero_iteraciones_max = 999
ErrorAbsoluto = 10**-5
iteraciones = 1
errorIteracion = abs(x - gfuncion)
while(ErrorAbsoluto<errorIteracion):
    x = gfuncion
    gfuncion = math.exp(-x)
    iteraciones += 1
    errorIteracion = abs(x - gfuncion)

print(f'La raiz se encuentra cuando x vale aproximadamente: {x} y el total de iteraciones fueron de {iteraciones}')