import time
import numpy as np
import math

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

inicio = time.time()

numeros = np.arange(1, 100001)
primos = [n for n in numeros if es_primo(n)]

fin = time.time()

print("Total de primos encontrados:", len(primos))
print("Duración total:", round(fin - inicio, 2), "segundos")
