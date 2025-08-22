#!/usr/bin/env python3
# Taschenrechner
# Copyright (C) 2025 Anton Schäfer
# Dieses Programm ist freie Software unter GPLv3.
# Eine Kopie der Lizenz befindet sich in der LICENSE-Datei.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Fehler: Division durch 0"
    return a / b

def main():
    print("Willkommen beim Taschenrechner von PyGearTools!")
    while True:
        try:
            a = input("Erste Zahl: ")
            if a.lower() == 'q':
                break
            a = float(a)
            
            op = input("Operator (+, -, *, /, q zum Beenden): ")
            if op.lower() == 'q':
                break
            
            b = float(input("Zweite Zahl: "))
            
            if op == '+':
                print("Ergebnis:", add(a, b))
            elif op == '-':
                print("Ergebnis:", subtract(a, b))
            elif op == '*':
                print("Ergebnis:", multiply(a, b))
            elif op == '/':
                print("Ergebnis:", divide(a, b))
            else:
                print("Ungültiger Operator")
        except ValueError:
            print("Ungültige Eingabe. Bitte Zahlen eingeben.")

if __name__ == "__main__":
    main()