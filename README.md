# FPY1101_EV3

### Evaluación número 3 - Fundamentos de Programación - Duoc UC SJ 2024

Desarrolle una aplicación en Python utilizando Visual Studio Code como
entorno de desarrollo según el siguiente enunciado:

Una empresa necesita analizar los datos de sus productos para generar
algunos reportes, y le ha solicitado a usted que realice un proto;po en
Python con los siguientes requerimientos:

La aplicación debe permi;r analizar los valores de los productos que se
encuentran en venta.

Solamente tenemos los nombres de los productos en el siguiente array:

### Productos


```python
productos = [
    "Café Americano", "Té Chai", "Croissant", "Jugo Naranja",
    "Panini de Pavo y Queso", "Pastel de Zanahoria", "Espresso Doble",
    "Baño de Frutas", "Muffin", "Ensalada", "Chocolate Caliente",
    "Tarta de Frambuesa", "Sándwich de Huevo", "Galletas de Avena",
    "Frappé de Caramelo"
]
```

Lo primero que hay que realizar asignar aleatoriamente los valores y el iva de
cada producto, este se debe encontrar entre los 2.000 a 10.000 redondeado
a la centena, por ejemplo el valor de un Muffin podría ser de $ 2.400, si el
valor da 2.450 o 2.453 estaría incorrecto. Recordar que el iva corresponde al
19% del valor del producto, este valor no debe tener decimales.

### La aplicación deberá poseer un menú con las siguientes funcionalidades:
1. Asignar montos aleatorios.
2. Ver estadísticas.
3. Salir del programa.
Cada función se detalla a continuación:

### 1. Asignar montos aleatorios
Para la generación de los montos se debe crear una función capaz de generar
los valores e iva de los productos de forma aleatoria, los que serán usados
posteriormente para la ejecución del programa.

### 2. Ver estadísticas
Crear una función que permita mostrar por pantalla los siguientes datos con
respecto a los sueldos:
- Producto con valor más alto.
- Producto con valor del IVA más bajo.
- Promedio del valor de los productos.
- Media geométrica del valor de los productos.
