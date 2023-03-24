# calcular las vueltas o lo que quedo debiendo
def Cuenta(P : int, M : int, H : int, B : float) -> float:
    ValorPanes = P * 300  # valor en pesos
    ValorLeche = M * 3300  # valor en pesos
    ValorHuevos = H * 350  # valor en pesos
    BilletePago = B
    return BilletePago - (ValorPanes + ValorLeche + ValorHuevos)

if __name__ == "__main__":
    P = int(input("ingrese cantidad de panes: "))
    M = int(input("ingrese cantidad de bolsas de leche: "))
    H = int(input("ingrese cantidad de huevos: "))
    B = float(input("ingrese un valor en pesos: "))
    CuentaTotal = Cuenta(P, M, H, B)
    print("las vueltas o lo que quedo debiendo son: " + str(CuentaTotal) + " pesos")
