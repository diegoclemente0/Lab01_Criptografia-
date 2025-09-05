#!/usr/bin/env python3
import sys

def descifrar_cesar(texto, desplazamiento):
    """Descifra texto con cifrado César"""
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('a')
            resultado += chr((ord(char) - base - desplazamiento) % 26 + base)
        else:
            resultado += char
    return resultado

def main():
    # MENSAJE EXACTO de tu actividad 1 (corregido)
    mensaje_cifrado = "larycxpajorj h bnpdarnjn nw annnb"
    
    # CORRECCIÓN: El mensaje exacto del ejercicio es:
    mensaje_cifrado_correcto = "larycxpajorj h bnpdarnjn nw annnb"
    
    print(f"Mensaje cifrado: {mensaje_cifrado_correcto}")
    print("\nProbando desplazamientos:")
    print("-" * 50)
    
    for d in range(26):
        descifrado = descifrar_cesar(mensaje_cifrado_correcto, d)
        if d == 9:
            print(f"\033[92m{d:2d}: {descifrado}\033[0m")  # Verde
        else:
            print(f"{d:2d}: {descifrado}")
    
    print("\n" + "=" * 50)
    print("MENSAJE ORIGINAL (desplazamiento 9):")
    resultado = descifrar_cesar(mensaje_cifrado_correcto, 9)
    print(f"\033[92m{resultado}\033[0m")
    print("=" * 50)
    
    # Verificación adicional
    print(f"\nVerificación: 'c' + 9 = '{chr(ord('c') + 9)}'")
    print(f"En cifrado: 'c' -> 'l' (debería ser)")

if __name__ == "__main__":
    main()