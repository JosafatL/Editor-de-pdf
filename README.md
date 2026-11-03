# 📄 Editor de PDFs 

Aplicación de consola en Python para hacer las tareas más comunes con archivos PDF desde un menú interactivo. Es un proyecto de nivel principiante, creado para practicar funciones, ciclos, condicionales, listas y manejo de archivos con la librería PyPDF2.

## ✨ Funciones

- 📖 **Contar páginas** de un PDF
- 🔗 **Unir dos PDFs** en un solo archivo
- ⛓️ **Unir múltiples PDFs**, indicando los archivos uno a uno
- ✂️ **Extraer una página** a un PDF nuevo
- 📄 **Extraer un rango de páginas** a un PDF nuevo
- 🗑️ **Eliminar páginas específicas** (por ejemplo: `1, 3, 5`)
- 🔄 **Rotar todas las páginas** 90°, 180° o 270°
- 📝 **Extraer el texto** a un archivo `.txt`, separado por página

El archivo original no se modifica: cada operación que genera un resultado lo guarda en un archivo nuevo con el nombre que elijas.

## 🚀 Instalación

Necesitas tener Python 3 instalado. Después, instala la dependencia:

```bash
pip install PyPDF2
```

## ▶️ Uso

Ejecuta el programa desde la carpeta del proyecto:

```bash
python proyecto1.py
```

Elige una opción del 1 al 9 y sigue las instrucciones en pantalla. Si el PDF está en otra carpeta, escribe su ruta en lugar de solo el nombre. Puedes probar el programa con `hola_mundo.pdf`, el archivo de ejemplo incluido.

## 📁 Estructura

```
├── proyecto1.py     # Código del editor
└── hola_mundo.pdf   # PDF de ejemplo
```

## 🛠️ Tecnologías

- Python 3
- [PyPDF2](https://pypi.org/project/PyPDF2/)
