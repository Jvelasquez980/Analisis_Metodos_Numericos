import numpy as np

def eliminacion_gaussiana(A, b):
    """
    Resuelve el sistema de ecuaciones lineales Ax = b usando el método de eliminación de Gauss.
    
    :param A: Matriz de coeficientes (n x n).
    :param b: Vector de términos independientes (n).
    :return: Vector solución x.
    """
    
    # Obtener el número de filas (ecuaciones)
    n = len(b)
    
    # Combinar la matriz A y el vector b en una matriz aumentada Ab
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    # Paso 1: Transformar la matriz aumentada a una forma triangular superior.
    for i in range(n):
        # Paso 1.1: Pivoteo para evitar división por cero (intercambiar filas si es necesario)
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        if i != max_row:
            Ab[[i, max_row]] = Ab[[max_row, i]]
        
        # Paso 1.2: Hacer ceros debajo del pivote actual
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    # Paso 2: Sustitución regresiva para encontrar las soluciones.
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]
    
    return x

# Ejemplo de uso:
A = np.array([[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]])
b = np.array([8.0, -11.0, -3.0])

# Llamada a la función con la matriz A y el vector b
solucion = eliminacion_gaussiana(A, b)
print(f'La solución del sistema es: {solucion}')
