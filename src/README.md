# Práctico 2 – Números pares e impares

Este es un proyecto en Python donde se trabajan listas de números. La idea es tener funciones que separen los **pares** y los **impares** de una lista.
Todo el código está en el archivo `src/operaciones.py`.

## ¿Qué hace el código?

Hay dos funciones principales:
- `filtrar_pares(lista)` → devuelve los números pares de la lista
- `filtrar_impares(lista)` → devuelve los impares

## ¿Cómo lo pruebo?
Podés correr el archivo `main.py`, que ya tiene un ejemplo listo.  
También podés probarlo vos así:

```python
from src.operaciones import filtrar_pares, filtrar_impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Pares:", filtrar_pares(numeros))
print("Impares:", filtrar_impares(numeros))


