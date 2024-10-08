xi = 2.6
xf =  2.8
xm = (xi + xf)/2 
funcionxi = (xi**3)-((1/2**(1/2))*xi**2)-5*xi
funcionxf = (xf**3)-((1/2**(1/2))*xf**2)-5*xf
funcionxm = (xm**3)-((1/2**(1/2))*xm**2)-5*xm
numero_iteraciones_max = 999
iteraciones = 1
ErrorAbsoluto = 10**-5
errorIteracion = abs(xf-xm)
raiz = None
while(numero_iteraciones_max > 0 and errorIteracion > ErrorAbsoluto and raiz == None):
    funcionxi = (xi**3)-((1/2**(1/2))*xi**2)-5*xi
    funcionxf = (xf**3)-((1/2**(1/2))*xf**2)-5*xf
    funcionxm = (xm**3)-((1/2**(1/2))*xm**2)-5*xm
    errorIteracion = abs(xf-xm)
    if funcionxi*funcionxm<0:
        if funcionxi == 0:
            raiz= xi
        if funcionxm == 0:
            raiz= xm
        xi = xi
        xf = xm
        xm = (xi + xf)/2 
    elif(funcionxf*funcionxm)<0:
        if funcionxm == 0:
            raiz= xm
        if funcionxf == 0:
            raiz= xf
        xi = xf
        xf = xm
        xm = (xi + xf)/2 
    iteraciones += 1
if raiz != None:
    print(f'La raiz se encuentra exactamente cuando x vale: {raiz}, se halló en {iteraciones} iteraciones')
else:
    print(f'La raiz se encuentra aproximadamente cuando x vale:{xm}, se halló en {iteraciones} iteraciones')