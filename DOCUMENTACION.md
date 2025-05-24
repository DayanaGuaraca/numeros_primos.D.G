# Documentación del Proyecto
# Introducción
El código original verificaba si un número era primo haciendo muchas comprobaciones, desde 2 hasta el número menos uno. Esto hacía que el programa tardara mucho cuando trabajaba con números grandes, porque revisaba divisores innecesarios.
# Optimización
Para mejorar el rendimiento, modifiqué la función para que sólo revise divisores hasta la raíz cuadrada del número, ya que si un número tiene un divisor mayor que su raíz cuadrada, también tendrá uno menor. Además, descarté todos los números pares excepto el 2, porque sabemos que no son primos. Para manejar mejor la lista de números, usé NumPy y una lista por comprensión para filtrar los primos, lo que dejó el código más limpio y mucho más rápido.
# Resultados
Antes de la optimización, el programa podía tardar varios segundos (incluso más de 32.8) en encontrar todos los números primos hasta 100,000. Después de aplicar los cambios, el tiempo bajó a aproximadamente 0.13 segundos en mi computadora.
Algo que me pareció curioso es que el tiempo cambia un poco dependiendo de dónde lo ejecuto. Por ejemplo, en Visual Studio Code me da un tiempo, y en la terminal (Bash) me da otro, aunque use el mismo código. Supongo que eso se debe a cómo funciona cada programa, pero lo importante es que en los dos casos se nota muchísimo la mejora.
Además, el resultado fue que se encontraron 9,592 números primos entre 1 y 100,000. Al revisar el rendimiento con cProfile, noté que la función para comprobar si un número es primo sigue siendo la que más tiempo toma, pero ahora mucho menos que antes, lo que confirma que la optimización sí sirvió.
# Conclusiones
Con esta mejora, el código funciona mucho más rápido y sin complicarlo tanto. Me ayudó a entender que pequeños cambios, como revisar solo hasta la raíz cuadrada o evitar los pares, hacen una gran diferencia. Aunque los resultados pueden variar un poco, la mejora se nota. Aprendí bastante sobre y estoy satisfecha con lo que logré.


