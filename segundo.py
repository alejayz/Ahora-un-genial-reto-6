# Calcular el área y perímetro
import math
def AreaFigura(a:float, b:float, r:float) -> float:
    ARectangulo = a * b
    ACirculos = (math.pi * (r)**2) * 2  # el área se duplica dado que son dos círculos
    return ARectangulo + ACirculos

def PerimetroFigura(a:float, b:float, r:float) -> float:
    PeRectangulo = (2 * a) + (2 * b)
    Diametro = 2 * r  # se duplica el radio para hallar diámetro y con éste el perímetro
    PeCirculos = (math.pi * Diametro) * 2  # el perímetro se duplica dado que son dos círculos
    return PeRectangulo + PeCirculos 

if __name__ == "__main__":
    a = float(input("ingrese ancho del rectángulo: "))
    b = float(input("ingrese largo del rectángulo: "))
    r = float(input("ingrese el radio del círculo: ")) 
    Area = AreaFigura(a, b, r)
    print("el área de la figura es: " + str(Area))
    Perimetro = PerimetroFigura(a, b, r)
    print("el perímertro de la figura es: " + str(Perimetro))
