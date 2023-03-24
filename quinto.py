# calcular el valor de un préstamo 
def Prestamo(C : float, i : float, n: int) -> float:
    interes = i / 100
    return C * (1 + interes) ** n

if __name__ == "__main__":
    C = float(input("ingrese valor de préstamo en pesos: "))
    i = float(input("ingrese valor de interés en %: "))
    n = int(input("ingrese número de meses: "))
    ValorPrestamo = Prestamo(C, i, n)
    print("el valor del préstamo por " + str(n) + " meses es de: " + str(ValorPrestamo))