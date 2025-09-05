#!/usr/bin/env python3
import os
import sys
import time
from scapy.all import IP, ICMP, Raw, send, conf
import random

def send_stealth_ping(data):
    """
    Envía cada carácter del string en paquetes ICMP con 48 bytes de data
    """
    destination = "8.8.8.8"
    
    print(f"Enviando mensaje: '{data}'")
    print(f"Longitud del mensaje: {len(data)} caracteres")
    print(f"Destino: {destination}")
    print("=" * 50)
    
    conf.verb = 0
    
    for i, char in enumerate(data):
        try:
            # Crear payload de 48 bytes: carácter real + datos de relleno
            real_char = char.encode()
            padding = bytes([random.randint(0, 255) for _ in range(47)])  # 47 bytes aleatorios
            payload = real_char + padding  # Total: 48 bytes
            
            # Crear paquete ICMP
            packet = IP(dst=destination)/ICMP(type=8, code=0)/Raw(load=payload)
            
            # Enviar paquete
            send_time = time.time()
            send(packet, verbose=False)
            
            print(f"Paquete {i+1}: Enviado carácter '{char}' en payload de 48 bytes")
            time.sleep(1)  # Pausa para mejor captura
            
        except Exception as e:
            print(f"Error enviando paquete {i+1}: {e}")
    
    print("=" * 50)
    print("Proceso completado - 48 bytes por paquete")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Error: Este script requiere permisos de superusuario (sudo)")
        print("Por favor ejecuta: sudo python3 pingv4.py \"tu mensaje\"")
        sys.exit(1)
    
    if len(sys.argv) != 2:
        print("Uso: sudo python3 pingv4.py \"mensaje a enviar\"")
        sys.exit(1)
    
    message = sys.argv[1]
    send_stealth_ping(message)