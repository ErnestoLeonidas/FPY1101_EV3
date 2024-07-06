import json
import globales
import random

def asignar_montos():
    productos = [
        "Café Americano",
        "Té Chai",
        "Croissant",
        "Jugo Naranja",
        "Panini de Pavo y Queso",
        "Pastel de Zanahoria",
        "Espresso Doble",
        "Ba;do de Frutas",
        "Muffin",
        "Ensalada",
        "Chocolate Caliente",
        "Tarta de Frambuesa",
        "Sándwich de Huevo",
        "Galletas de Avena",
        "Frappé de Caramelo"
    ]

    todos_los_productos = []
    for producto in productos:
        nombre = producto
        valor = random.randint(20, 100) * 100
        iva = int(valor * 0.19)

        nuevo_producto = {
            "nombre": nombre,
            "valor": valor,
            "iva": iva
        }
        
        todos_los_productos.append(nuevo_producto)
    
    globales.guardar_archivo_json("productos.json", todos_los_productos)
    print("Productos Registrados")

asignar_montos()