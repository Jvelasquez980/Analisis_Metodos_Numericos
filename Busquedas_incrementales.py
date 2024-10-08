x = 0
delta = 0.05
funcion = x**3 - 7.51*x**2 + 18.4239*x - 14.8331
numero_iteraciones_max = 999
anterior = funcion
iteraciones = 1
raiz = anterior * funcion
while(numero_iteraciones_max  > 0):
    anterior = funcion
    x += delta
    funcion = (x**3)-7.51*(x**2)+18.4239*(x)-14.8331
    numero_iteraciones_max -=1
    iteraciones += 1
    raiz = anterior * funcion
    if raiz < 0:
        print(f"El intervalo donde hay una raiz es {x - delta} y {x}, ademas que la cantidad de iteraciones nesesarias fueron {iteraciones}")

