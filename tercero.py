# Calcular cantidad total de carne de aves en Kg
def CarneAves(N : int, M : int, K : int) -> int:
    CarneGalli = N * 6 # número entero en Kg
    CarneGallo = M * 7  # número entero en Kg
    CarnePolli = K * 1  # número entero en Kg
    return CarneGalli + CarneGallo + CarnePolli

if __name__ == "__main__":
    N = int(input("ingrese cantidad de gallinas: "))
    M = int(input("ingrese cantidad de gallos: "))
    K = int(input("ingrese cantidad de pollitos: "))
    CarneAvesTotal = CarneAves(N, M, K)
    print("la cantidad de carne de aves es: " + str(CarneAvesTotal) + "Kg")
