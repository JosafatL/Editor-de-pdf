# ==========================================================
# 📄 PROYECTO: MI PRIMER EDITOR DE PDF
# Nivel: Principiante (Conceptos 1 al 8 de Python)
# Librería: PyPDF2
# ==========================================================

import PyPDF2


# Dividir el código en funciones (tareas ordenadas)

def mostrar_menu():
    print("\n" + "=" * 45)
    print(" 🛠️ Editor de PDFs Hybridge 📄  ")
    print("=" * 40)
    print("1. 📖 Ver cuántas páginas contiene el PDF")
    print("2. 🔗 Unir dos archivos PDF")
    print("3. 📄 Unir multiples PDFs")
    print("4. ✂️ Extraer una página de un PDF")
    print("5. 📄 Extraer un rango de páginas")
    print("6. 🗑️ Eliminar páginas específicas del PDF")
    print("7. 🔄 Rotar las páginas del PDF")
    print("8. 📝 Extraer texto del archivo")
    print("9. ❌ Salir del menú")
    print("=" * 45)

def contar_paginas():
    # Permita contar cuantas páginas contiene un archivo
    print("\n--- 📖 Contar Páginas ---")

    # Conocer que documento queremos tratar
    archivo = input("Dime cuál es el nombre del archivo(ej: documento.pdf): ")
    
    # Abrir y leer el documento indicado 
    lector = PyPDF2.PdfReader(archivo)
    
    # (lector.pages) se comporta como una lista para aplicar len()
    total = len(lector.pages)

    print(f"El archivo '{archivo}' tiene {total} página(s).")

def unir_dos_pdfs():

    # Permite unir dos pdfs
    print("\n--- 🔗 Unir PDFs ---")

    archivo1 = input("Nombre del primer PDF: ")
    archivo2 = input("Nombre del segundo PDF: ")
    archivo_salida = input("Nombra el nuevo PDF: ")

    lista_archivos = [archivo1, archivo2]

    # Creamos el nuevo archivo
    escritor = PyPDF2.PdfWriter()

    for nombre in lista_archivos:
        lector = PyPDF2.PdfReader(nombre)

        # Recorrer cada página
        for pagina in lector.pages:
            escritor.add_page(pagina)

    # Guardar el nuevo archivo PDF
    escritor.write(archivo_salida)
    print(f"Listo! Tu nuevo PDF se guardó y se llama '{archivo_salida}'")


def unir_multiples_pdfs():
    #Permite unir más de dos pdfs
    print("\n--- ⛓️ Unir multiples PDFs ---")
    lista_archivos = []
    print("Ingresa los nombres de los PDFs uno a uno. Luego escribe 'listo' cuando termines:")

    while True:
        nombre = input(f"Archivo #{len(lista_archivos) + 1} (o escribe 'listo'):").strip()

        #Rompe el ciclo
        if nombre.lower() == 'listo':
            break

        if nombre != "":
            lista_archivos.append(nombre)

    # Validar que al menos haya 2 archivos
    if len(lista_archivos) < 2:
        print("Error: Debes ingresar al menos 2 nombres de archivo")
        return

    escritor = PyPDF2.PdfWriter()

    for nombre in lista_archivos:
        lector = PyPDF2.PdfReader(nombre)
        for pagina in lector.pages:
            escritor.add_page(pagina)

    archivo_salida = input("Dime el nombre del nuevo archivo: ")
    escritor.write(archivo_salida)
    print(f"Listo! Se unieron con éxito {len(lista_archivos)} archivos en '{archivo_salida}'.")


def extraer_pagina():
    print("\n--- ✂️ Extraer una Página del PDF ---")
    archivo = input("Nombre del PDF original: ")
    lector = PyPDF2.PdfReader(archivo)
    total_paginas = len(lector.pages) 

    print(f"El archivo es '{archivo}', y tiene {total_paginas} página(s)")

    # Preguntar que página queremos extraer
    numero_pagina = int(input("Dime que página quieres extraer: "))

    # Validar que el número solicitado exista
    if numero_pagina >= 1 and numero_pagina <= total_paginas:
        # Restamos una posición al índice de la lista en Python [0] para eliminar el desface
        indice = numero_pagina - 1

        escritor = PyPDF2.PdfWriter()
        # Obtener la página seleccionada
        pagina_seleccionada = lector.pages[indice]

        # Añadimos la página seleccionada al nuevo PDF
        escritor.add_page(pagina_seleccionada)

        # Nombrar el PDF nuevo
        archivo_salida = input("Dime cómo se va a llamar el nuevo archivo: ")
        escritor.write(archivo_salida)

        # Mostrar mensaje de que se generó con éxito
        print(f"Listo! El nuevo archivo se llama: '{archivo_salida}'")
    else:
        # Mostrar mensaje de que no se generó con éxito
        print("Error: El número de página no corresponde a este archivo")


def extraer_rango_palabras():
    print("\n--- 📄 Extraer un Rango de Páginas del PDF ---")
    archivo = input("Dime el nombre del PDF original: ")
    lector = PyPDF2.PdfReader(archivo)
    total_paginas = len(lector.pages) 

    print(f"El archivo es '{archivo}', y tiene {total_paginas} página(s)")

    inicio = int(input("Dime la página inicial para la extracción: "))
    fin = int(input("Dime la página final para la extracción: "))

    if 1 <= inicio <= fin <= total_paginas:
        escritor = PyPDF2.PdfWriter()

        for indice in range(inicio -1, fin):
            escritor.add_page(lector.pages[indice])

        archivo_salida = input("Dime el nombre del nuevo archivo: ")
        escritor.write(archivo_salida)

        print(f"Páginas de la {inicio} a la {fin} guardadas en '{archivo_salida}'")
    else:
        print("Error: El rango de páginas no es válido.")

def eliminar_paginas():
    print("\n--- 🗑️ Eliminar Páginas del PDF ---")
    archivo = input("Dime el nombre del PDF: ")
    lector = PyPDF2.PdfReader(archivo)
    total_paginas = len(lector.pages)

    print(f"El archivo tiene {total_paginas} páginas.")
    entrada = input("Escribe los números de páginas a eliminar, separados por comas(ej. 1, 3, 5): ")
    paginas_a_elimiar = []
    for parte in entrada.split(","):
        parte = parte.strip()
        if parte.isdigit():
            paginas_a_elimiar.append(int(parte))

    escritor = PyPDF2.PdfWriter()
    conservadas = 0

    for numero, pagina in enumerate(lector.pages, start=1):
        if numero not in paginas_a_elimiar:
            escritor.add_page(pagina)
            conservadas += 1

    if conservadas == 0:
        print("Error: No puedes eliminar todas las páginas")
        return

    archivo_salida = input("Dime el nombre del nuevo archivo: ")
    escritor.write(archivo_salida)
    print(f"Listo! Se guardó '{archivo_salida}' con {conservadas} página(s), se eliminaron {len(paginas_a_elimiar)} página(s)")

def rotar_paginas():
    print("\n--- 🔄 Rotar Páginas del PDF ---")
    archivo = input("Dime a qué archivo quieres rotar: ")
    lector = PyPDF2.PdfReader(archivo)

    print("Opciones de rotación: 90, 180, 270 grados.")
    grados = int(input("Dime los grados en los quieres rotar: "))

    if grados == 90 or grados == 180 or grados == 270:
        escritor = PyPDF2.PdfWriter()

        # Recorrer cada página del archivo y rotarlas
        for pagina in lector.pages:
            pagina.rotate(grados)
            escritor.add_page(pagina)

        archivo_salida = input("Dime el nombre del nuevo archivo (rotado): ")
        escritor.write(archivo_salida)
        print(f"Todas las páginas del archivo '{archivo}' fueron rotadas {grados}° y guardadas en '{archivo_salida}'")
    else:
        print("Error: Los grados de rotación solo pueden ser 90, 180 y 270.")

def extrar_texto():
    print("\n--- 📝 Extraer texto del PDF ---")
    archivo = input('Dime el nombre del PDF: ')
    lector = PyPDF2.PdfReader(archivo)
    total_paginas = len(lector.pages)

    print(f'Procesando {total_paginas} paginas...')
    archivo_txt = input("Dime el nombre del nuevo archivo .txt: ")

    texto_completo = ""

    for numero, pagina in enumerate(lector.pages, start=1):
        texto_pagina = pagina.extract_text()
        texto_completo += f'=== PÁGINA {numero} === \n'
        if texto_pagina:
            texto_completo += texto_pagina + "\n\n"
        else:
            texto_completo += "[Esta página no contiene texto o es una imagen]\n\n"

    with open(archivo_txt, "w", encoding="utf-8") as f:
        f.write(texto_completo)

    print(f"Listo! Texto extraido y guardado en '{archivo_txt}'")

def main():

    ejecutando = True

    while ejecutando:
        #Llamar a la funcion mostar_menu
        mostrar_menu()

        opcion = input("Elige una opción (1-9): ").strip()

        if opcion == "1":
            contar_paginas()
        elif opcion == "2":
            unir_dos_pdfs()
        elif opcion == "3":
            unir_multiples_pdfs()
        elif opcion == "4":
            extraer_pagina()
        elif opcion == "5":
            extraer_rango_palabras()
        elif opcion == "6":
            eliminar_paginas()
        elif opcion == "7":
            rotar_paginas()
        elif opcion == "8":
            extrar_texto()
        elif opcion == "9":
            print("Gracias por usar el editor PDF Hybridge")
            ejecutando = False
        else:
            print("Opció no valida, selecciona una del 1 al 9.")

if __name__ == "__main__":
    main()
