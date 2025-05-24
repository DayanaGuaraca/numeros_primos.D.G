# Documentación del Proyecto

## Introducción
El código original verificaba si un número era primo haciendo muchas comprobaciones, desde 2 hasta el número menos uno. Esto hacía que el programa tardara mucho cuando trabajaba con números grandes, porque revisaba divisores innecesarios.

## Optimización
Para mejorar el rendimiento, modifiqué la función para que sólo revise divisores hasta la raíz cuadrada del número, ya que si un número tiene un divisor mayor que su raíz cuadrada, también tendrá uno menor. Además, descarté todos los números pares excepto el 2, porque sabemos que no son primos. Para manejar mejor la lista de números, usé NumPy y una lista por comprensión para filtrar los primos, lo que dejó el código más limpio y mucho más rápido.

## Resultados
Antes, encontrar todos los primos hasta 100,000 tardaba más de 30 segundos. Después de optimizarlo, el tiempo bajó a sólo 0.14 segundos. Usando cProfile confirmé que la función de verificar primos sigue siendo la parte que consume más tiempo, pero ahora es mucho más eficiente que antes. Esto muestra que la optimización realmente funcionó.

## Conclusiones
La optimización hizo que el código sea significativamente más rápido sin perder claridad ni legibilidad. Para futuras mejoras, recomiendo explorar métodos más avanzados como la Criba de Eratóstenes o implementar paralelización, para poder trabajar con números aún más grandes sin que se incremente demasiado el tiempo de ejecución.


