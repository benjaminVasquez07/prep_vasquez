def datos_archivo(nombre_archivo):
    datos = []
    with open(nombre_archivo, "r") as archivo:
        lineas = [linea.strip() for linea in archivo if linea.strip()]
        for i in range(0, len(lineas), 4):
            bloque = [lineas[i]] 
            for valor in lineas[i+1:i+4]:
                bloque.append(int(valor))
            datos.append(bloque)
    return datos

resultado = datos_archivo("text.txt")
print(resultado)
