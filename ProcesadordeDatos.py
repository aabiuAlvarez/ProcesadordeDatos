def eliminar_duplicados(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado


def frecuencia_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(".,!?()[]{}\":';")
        if palabra:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


def invertir_diccionario(diccionario):
    invertido = {}
    for clave, valor in diccionario.items():
        if valor not in invertido:
            invertido[valor] = [clave]
        else:
            invertido[valor].append(clave)
    return invertido


if __name__ == "__main__":
    while True:
        print("\nMenú:")
        print("1. Eliminar duplicados de una lista")
        print("2. Contar frecuencia de palabras en un texto")
        print("3. Invertir un diccionario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            lista = input("Ingrese los elementos de la lista separados por espacio: ").split()
            print("Lista sin duplicados:", eliminar_duplicados(lista))
        
        elif opcion == "2":
            texto = input("Ingrese el texto: ")
            print("Frecuencia de palabras:", frecuencia_palabras(texto))
        
        elif opcion == "3":
            diccionario = {}
            n = int(input("Ingrese el número de elementos del diccionario: "))
            for _ in range(n):
                clave = input("Clave: ")
                valor = input("Valor: ")
                diccionario[clave] = valor
            print("Diccionario invertido:", invertir_diccionario(diccionario))
        
        elif opcion == "4":
            print("Saliendo del programa....")
            break
        else:
            print("Opción no válida, intente de nuevo.")