# Prueba técnica SysTienda

El siguiente documento contiene un breve desarrollo de la solución a la prueba 
técnica proporcionada, para reproducir los scripts, se recomienda utilizar python 3.12.4.

### Ejercicio 1
1. Dada una cadena de expresión exp, escriba un programa para examinar si los pares y los órdenes de "{", "}", "(", ")", "[", "]" son correctos en exp.

Ejemplo: 
- correcto (({{[]}}))
- incorrecto ([({))}

El script de éste ejercicio se encuentra en el archivo <code>primer_ejercicio.py</code>,
y su solución se abordó con una clase, y dos funciones, la clase se utilizó
simplemente para mapear el simbolo de apertura y cierre, en el caso de los simbolos de
apertura como <pre>({[</pre> se inicializaban en éste clase y servía para obtener
los simbolos de cierre <pre>}])</pre>
Adicionalmente existe una función llamada remove_elements que lo que hace es recibir
una expresion como cadena, y devolver la expresión quitandole los simbolos de
apertura y cierre que se le hayan solicitado a traves del parámetro symbol, en dado
caso de que en el inicio y en el fin de la expresión, no se encuentren los mismos 
simbolos, la función arroja una excepción.
Por último se utiliza una función check, que lo que hace es validar la lógica inicial
de una expresión validable, es decir, si una expresión tiene una cantidad de strings 
impar, significa que de entrada es incorrecta, si la expresión que se recibe cuenta
con una longitud cero, significa que es incorrecta, y posteriormente, se extrae, 
considerando que la longitud de la expresión es par, la mitad de los elementos, lo cual 
representa la primera mitad de la expresión que debe de ser replicada, como si 
fuera un espejo, posteriormente, se recorre uno por uno y se pasan a la función
<code>remove_elements</code>, que va eliminando par por par desde afuera hacia adentro, 
ahora, como es posible que ésta función arroje una excepción, se controla con un
<code>try...catch</code>, y si recorre completamente la cadena, significa que la cadena
es correcta y devuelve true, ésto se refleja con dos llamadas en las lineas 45 y 46 
donde envío una cadena correcta y una cadena incorrecta para que arroje los resultados
esperados.

### Ejercicio 2

2. Hay un trabajador que trabaja en una fábrica de planchas y necesita comprobar la resistencia de las planchas. 
Hay un edificio de 1000 pisos y tienes que saber tirando las placas de los pisos, de qué piso se rompió exactamente la placa. En cada lanzamiento que no se rompa el plato puedes bajar a recogerlo y volver a tirarlo.

#### Ejercicio 2.1
- Primera parte: solo tiene un plancha y tiros ilimitados. ¿qué harías?

La solución a éste ejercicio está en el archivo <code>segundo_ejercicio_caso_1.py</code>,
y se solucionó con dos funciones, una que simula el tiro de la plancha 
utilizando una función random, para obtener un resultado positivo o negativo, con el
propósito de que determinar si se rompió o no se rompió, ésta función solo devuelve un 
un tipo de dato positivo o negativo. 
Posteriormente se utilizó una función llamada verificar, que lo que hace es recibir 3
parámetros, start, stop y step, los cuales van a representar lo siguiente:

- **start:** Representará a partir de que piso se comenzará a hacer pruebas.
- **stop:** Representará hasta que piso se dejarán de hacer pruebas.
- **step:** Es un número que representa el intervalo por el cual se dividirá la información por lotes, es decir, si utilizaremos lotes de 10, de 100, de 50.

La idea es la siguiente, tenemos 1000 pisos pero solo tenemos una plancha, y tiros ilimitados,
la idea es armar bloques de 100, para reducir la busqueda lo más posible, por ejemplo, si tenemos los siguientes
bloques <code>[100,200,300,400,...900,1000]</code>, la idea es lanza la plancha desde 
el piso 100, si no se rompe, desde el piso 200, sino desde el 300, y asi, cuando se rompa, 
por ejemplo en el 400, entonces tenemos un rango de datos donde podemos determinar que 
la plancha no se rompe bajo cualquier piso 300, pero se rompe entre el piso 301 y 400, pero
como solo tenemos una plancha, cuando se quiebra, termina el algoritmo.

#### Ejercicio 2.2
- Segunda parte: hay platos ilimitados. ¿Cuál es el número mínimo de disparos para encontrar el suelo?

La solución a éste ejercicio está en el archivo <code>segundo_ejercicio_caso_2.py</code>,
y se solucionó también con dos funciones que hacian algo similar al ejercicio uno, 
agregando un contador de disparos, para saber cuantas veces es necesario lanzar planchas
para saber en que piso especificamente se rompe, basicamente la idea es muy similar 
a la anterior solución, se usan 3 parámetros para determinar rangos de lotes de datos, 
y lanzar la plancha desde los rangos con un intervalo de 100, por ejemplo:

<pre>[100,200,300,400,500,600,700,800,900,1000]</pre>

La ventaja que tenemos acá, es que tenemos planchas ilimitadas, entonces, a traves de
un algoritmo recursivo con la misma función de <code>verificar</code>, podemos 
condicionar de que cuando se haya roto entre un intervalo determinado, por ejemplo, entre 
el **401** y el **500**, entonces buscar dentro de éste lote de datos, ya ignorando los 
consecuentes, pero reduciendo en intervalos divisibles entre 10, hasta llegar a 
1, entonces buscariamos por lotes de: 

<pre>
[
    {inicio: 401, fin: 410},
    {inicio: 411, fin: 420},
    {inicio: 421, fin: 430},
    {...},
]
</pre>

Y ésto permitirá que cuando el algoritmo nos arroje por ejemplo, que la plancha se rompió
en el intervalo de 421 y 430, entonces, de manera recursiva, dividirá entre 10, y el 
intervalo será 1, permitiendonos buscar de la siguiente manera:
<pre>
[
    {inicio: 421, fin: 421}, //Esto representará un solo piso
    {inicio: 422, fin: 422},
    {inicio: 423, fin: 423},
    {...},
]
</pre>
Cuando conluya el algoritmo recursivo, podremos identificar exactamente no solo el piso 
exacto donde se rompe la plancha, sino cuantas veces se tuvo que hablar así mismo
el algoritmo recursivo, entonces, en lugar de recorrer 1000 veces, recorremos solo
las veces que se hayan dividido por lotes, por ejemplo, 8,4,7 
(datos obtenidos de las pruebas realizadas)

#### Ejercicio 2.3
- Tercera parte: ahora solo tiene 2 platos. ¿Cuál es el número mínimo de lanzamientos para encontrar el suelo

La solución a éste ejercicio está en el archivo <code>segundo_ejercicio_caso_3.py</code>,
y una vez teniendo los primeros dos ejercicios éste realmente fue muy rápido, solo tuve que 
agregar un contador de cuantas planchas tenia disponibles para romper, y entonces, apliqué
el mismo algoritmo recursivo, con la diferencia, de que cada vez que el algoritmo
me devolvía que se había roto el plato, incrementaba el contador, hasta que se rompían los
dos platos, entonces, el algoritmo en ese punto se detiene, arrojando los resultados
del número de lanzamientos que se pudieron realizar solo con dos platos.