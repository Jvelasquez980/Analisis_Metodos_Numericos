import sympy as sp
valor = 0.5
x = sp.Symbol('x')
funcion = sp.exp(-x) - x
derivada = sp.diff(funcion, x)
derivada_2 = sp.diff(derivada, x)
gx = valor - ((funcion.subs(x,valor)*derivada.subs(x, valor))/(pow(derivada.subs(x, valor),2))-(funcion.subs(x,valor)*derivada_2.subs(x,valor)))
ErrorAbsoluto = 10**-5
errorIteracion = abs(valor-gx)
iteracion = 1
while(ErrorAbsoluto < errorIteracion):
    valor = gx
    gx = valor - ((funcion.subs(x,valor)*derivada.subs(x, valor))/(pow(derivada.subs(x, valor),2))-(funcion.subs(x,valor)*derivada_2.subs(x,valor)))
    errorIteracion = abs(valor-gx)
    iteracion += 1
print(f"La raiz se encuentra cuando x vale aproximadamente: {valor} y la cantidad de iteraciones fueron {iteracion}")