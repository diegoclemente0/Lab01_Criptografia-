#!/usr/bin/env python3
import sys

def cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():  # Solo ciframos letras
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            resultado += char  # Dejamos espacios y otros símbolos igual
    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 cesar.py \"texto a cifrar\" desplazamiento")
        sys.exit(1)

    texto = sys.argv[1]
    try:
        desplazamiento = int(sys.argv[2])
    except ValueError:
        print("El desplazamiento debe ser un número entero.")
        sys.exit(1)

    print(cesar(texto, desplazamiento))
