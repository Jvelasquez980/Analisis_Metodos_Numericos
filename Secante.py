import math 
x0 = 0
x1 = 1
funcionx0 = math.exp(-x0) - x0
funcionx1 = math.exp(-x1) - x1
gx = x1 - (((x1 - x0)/funcionx1-funcionx0)*funcionx1)
toleracia = 10**-5
errorIteracion = abs(gx)
x0 = x1
x1 = gx
iteraciones = 1
while(toleracia<errorIteracion):
    funcionx0 = math.exp(-x0) - x0
    funcionx1 = math.exp(-x1) - x1
    gx = x1 - (((x1 - x0)*funcionx1/funcionx1-funcionx0))
    errorIteracion = abs(gx-x1)
    x0 = x1
    x1 = gx
    iteraciones += 1

print(f'La raiz de la funcion es aproximadamente: {x0} numero de iteraciones {iteraciones}')