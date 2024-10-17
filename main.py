# main.py

from operaciones import OperacionesMatematicas

if __name__ == '__main__':
    print("Suma 5 + 3 =", OperacionesMatematicas.suma(5, 3))
    print("Resta 10 - 4 =", OperacionesMatematicas.resta(10, 4))
    print("Multiplicación 7 * 6 =", OperacionesMatematicas.multiplicacion(7, 6))
    try:
        print("División 20 / 5 =", OperacionesMatematicas.division(20, 5))
        print("División 10 / 0 =", OperacionesMatematicas.division(10, 0))
    except ValueError as e:
        print(e)
