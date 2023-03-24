# calcular número de personas que se han contagiado de Covid-19
def ContagiadosCovid(D : int, C : float) -> float:
    return C * (2 ** D)
    

if __name__ == "___main__":
    D = int(input("ingrese núumero de días: "))
    C = float(input("ingrese número de contagiados: "))
    TotalContagiados = ContagiadosCovid(D, C)
    print("el número de contagiados será de " + str(TotalContagiados))