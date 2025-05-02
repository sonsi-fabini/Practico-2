# Practico-2
Este proyecto contiene funciones en Python para filtrar números **pares** e **impares** de una lista.

## 📁 Estructura del proyecto
Practico-2/ ├── main.py └── src/ └── operaciones.py

## 🧠 Funcionalidades
Actualmente incluye las siguientes funciones:
- `filtrar_pares(lista)` → Devuelve los números pares.
- `filtrar_impares(lista)` → Devuelve los números impares.

## 🧪 Cómo probar el proyecto

1. Cloná el repositorio en tu computadora o Google Colab:
```bash
git clone https://github.com/sonsi-fabini/Practico-2.git
cd Practico-2

2.Asegurate de tener Python instalado (o usá Google Colab).

3. Ejecutá el archivo main.py o usá el siguiente ejemplo:
from src.operaciones import filtrar_pares, filtrar_impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filtrar_pares(numeros)
impares = filtrar_impares(numeros)

print("Pares:", pares)      # [2, 4, 6, 8, 10]
print("Impares:", impares)  # [1, 3, 5, 7, 9]

🛠️ Contribuir
Forkeá este repo
Creá una nueva rama (git checkout -b nueva-funcionalidad)
Hacé tus cambios y hacé commit (git commit -am 'Agregar función X')
Hacé push (git push origin nueva-funcionalidad)
Abrí un Pull Request

