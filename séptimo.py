# calcular diferentes operaciones
def Prom(a : float, b : float, c : float, d : float, e : float) -> float:
    s = a + b + c + d + e
    return s / 5

def OrdAscendente(a : float, b : float, c : float, d : float, e : float) -> float:
    if a < b and a < c and a < d and a < e :
        primero = a
    elif b < a and b < c and b < d and b < e :
        primero = b
    elif c < b and c < a and c < d and c < e :
        primero = c
    elif d < b and d < c and d < a and d < e :
        primero = d
    else :
        primero = e

    if (a > b and a < c and a < d and a < e) or (a > c and a < b and a < d and a < e) or (a > d and a < b and a < c and a < e) or (a > e and a < b and a < c and a < d):
        segundo = a
    elif (b > a and b < c and b < d and b < e) or (b > c and b < a and b < d and b < e) or (b > d and b < a and b < c and b < e) or (b > e and b < a and b < c and b < d):
        segundo = b
    elif (c > a and c < b and c < d and c < e) or (c > b and c < a and c < d and c < e) or (c > d and c < a and c < b and c < e) or (c > e and c < a and c < b and c < d):
        segundo = c
    elif (d > a and d < b and d < c and d < e) or (d > b and d < a and d < c and d < e) or (d > c and d < a and d < b and d < e) or (d > e and d < a and d < b and d < c):
        segundo = d
    elif (e > a and e < b and e < c and e < d) or (e > b and e < a and c < c and e < d) or (e > c and e < a and e < b and e < d) or (e > d and e < a and e < b and e < c):
        segundo = e


    if (a < e and a > b and a > c and a > d) or (a < d and a > b and a > c and a > e) or (a < c and a > b and a > d and a < e) or (a < b and a > c and a > d and a > e):
        cuarto = a
    elif (b < e and b > a and b > c and b > d) or (b < d and b > a and b > c and b > e) or (b < c and b > a and b > d and b < e) or (b < a and b > c and b > d and b > e):
        cuarto = b
    elif (c < e and c > a and c > b and c > d) or (c < d and c > a and c > b and c > e) or (c < b and c > a and d > d and c < e) or (c < a and c > b and c > d and c > e):
        cuarto = c
    elif (d < e and d > a and d > b and d > c) or (d < c and d > a and d > b and d > e) or (d < b and d > a and d > c and d < e) or (d < a and d > b and d > c and d > d):
        cuarto = d
    elif(e < a and e > b and e > c and e > d) or (e < b and e > a and e > c and e > d) or (e < c and e > a and e > b and e < d) or (e < d and e > a and e > b and e > c):
        cuarto = e

    if (a > b and a > c and a > d and a > e):
        quinto = a
    elif (b > a and b > c and b > d and b < e):
        quinto = b
    elif (c > a and c > b and c > d and c > e):
        quinto = c
    elif (d > a and d > b and d > c and d > e):
        quinto = d
    elif (e > a and e > b and e > c and e > d):
        quinto = e

    if (a > segundo and a < cuarto):
        tercero = a
    elif (b > segundo and b < cuarto):
        tercero = b
    elif (c > segundo and c < cuarto):
        tercero = c
    elif (d > segundo and d < cuarto):
        tercero = d
    elif (e > primero and e > segundo and e < cuarto and e < quinto):
        tercero = e
    return primero, segundo, tercero, cuarto, quinto

def OrdDescendiente(a : float, b : float, c : float, d : float, e : float) -> float:
    if a < b and a < c and a < d and a < e :
        primero = a
    elif b < a and b < c and b < d and b < e :
        primero = b
    elif c < b and c < a and c < d and c < e :
        primero = c
    elif d < b and d < c and d < a and d < e :
        primero = d
    else :
        primero = e

    if (a > b and a < c and a < d and a < e) or (a > c and a < b and a < d and a < e) or (a > d and a < b and a < c and a < e) or (a > e and a < b and a < c and a < d):
        segundo = a
    elif (b > a and b < c and b < d and b < e) or (b > c and b < a and b < d and b < e) or (b > d and b < a and b < c and b < e) or (b > e and b < a and b < c and b < d):
        segundo = b
    elif (c > a and c < b and c < d and c < e) or (c > b and c < a and c < d and c < e) or (c > d and c < a and c < b and c < e) or (c > e and c < a and c < b and c < d):
        segundo = c
    elif (d > a and d < b and d < c and d < e) or (d > b and d < a and d < c and d < e) or (d > c and d < a and d < b and d < e) or (d > e and d < a and d < b and d < c):
        segundo = d
    elif (e > a and e < b and e < c and e < d) or (e > b and e < a and c < c and e < d) or (e > c and e < a and e < b and e < d) or (e > d and e < a and e < b and e < c):
        segundo = e


    if (a < e and a > b and a > c and a > d) or (a < d and a > b and a > c and a > e) or (a < c and a > b and a > d and a < e) or (a < b and a > c and a > d and a > e):
        cuarto = a
    elif (b < e and b > a and b > c and b > d) or (b < d and b > a and b > c and b > e) or (b < c and b > a and b > d and b < e) or (b < a and b > c and b > d and b > e):
        cuarto = b
    elif (c < e and c > a and c > b and c > d) or (c < d and c > a and c > b and c > e) or (c < b and c > a and d > d and c < e) or (c < a and c > b and c > d and c > e):
        cuarto = c
    elif (d < e and d > a and d > b and d > c) or (d < c and d > a and d > b and d > e) or (d < b and d > a and d > c and d < e) or (d < a and d > b and d > c and d > d):
        cuarto = d
    elif(e < a and e > b and e > c and e > d) or (e < b and e > a and e > c and e > d) or (e < c and e > a and e > b and e < d) or (e < d and e > a and e > b and e > c):
        cuarto = e

    if (a > b and a > c and a > d and a > e):
        quinto = a
    elif (b > a and b > c and b > d and b < e):
        quinto = b
    elif (c > a and c > b and c > d and c > e):
        quinto = c
    elif (d > a and d > b and d > c and d > e):
        quinto = d
    elif (e > a and e > b and e > c and e > d):
        quinto = e

    if (a > segundo and a < cuarto):
        tercero = a
    elif (b > segundo and b < cuarto):
        tercero = b
    elif (c > segundo and c < cuarto):
        tercero = c
    elif (d > segundo and d < cuarto):
        tercero = d
    elif (e > primero and e > segundo and e < cuarto and e < quinto):
        tercero = e
    return quinto, cuarto, tercero, segundo, primero

def Med(a : float, b : float, c : float, d : float, e : float) -> float:
    if a < b and a < c and a < d and a < e :
        primero = a
    elif b < a and b < c and b < d and b < e :
        primero = b
    elif c < b and c < a and c < d and c < e :
        primero = c
    elif d < b and d < c and d < a and d < e :
        primero = d
    else :
        primero = e

    if (a > b and a < c and a < d and a < e) or (a > c and a < b and a < d and a < e) or (a > d and a < b and a < c and a < e) or (a > e and a < b and a < c and a < d):
        segundo = a
    elif (b > a and b < c and b < d and b < e) or (b > c and b < a and b < d and b < e) or (b > d and b < a and b < c and b < e) or (b > e and b < a and b < c and b < d):
        segundo = b
    elif (c > a and c < b and c < d and c < e) or (c > b and c < a and c < d and c < e) or (c > d and c < a and c < b and c < e) or (c > e and c < a and c < b and c < d):
        segundo = c
    elif (d > a and d < b and d < c and d < e) or (d > b and d < a and d < c and d < e) or (d > c and d < a and d < b and d < e) or (d > e and d < a and d < b and d < c):
        segundo = d
    elif (e > a and e < b and e < c and e < d) or (e > b and e < a and c < c and e < d) or (e > c and e < a and e < b and e < d) or (e > d and e < a and e < b and e < c):
        segundo = e


    if (a < e and a > b and a > c and a > d) or (a < d and a > b and a > c and a > e) or (a < c and a > b and a > d and a < e) or (a < b and a > c and a > d and a > e):
        cuarto = a
    elif (b < e and b > a and b > c and b > d) or (b < d and b > a and b > c and b > e) or (b < c and b > a and b > d and b < e) or (b < a and b > c and b > d and b > e):
        cuarto = b
    elif (c < e and c > a and c > b and c > d) or (c < d and c > a and c > b and c > e) or (c < b and c > a and d > d and c < e) or (c < a and c > b and c > d and c > e):
        cuarto = c
    elif (d < e and d > a and d > b and d > c) or (d < c and d > a and d > b and d > e) or (d < b and d > a and d > c and d < e) or (d < a and d > b and d > c and d > d):
        cuarto = d
    elif(e < a and e > b and e > c and e > d) or (e < b and e > a and e > c and e > d) or (e < c and e > a and e > b and e < d) or (e < d and e > a and e > b and e > c):
        cuarto = e

    if (a > b and a > c and a > d and a > e):
        quinto = a
    elif (b > a and b > c and b > d and b < e):
        quinto = b
    elif (c > a and c > b and c > d and c > e):
        quinto = c
    elif (d > a and d > b and d > c and d > e):
        quinto = d
    elif (e > a and e > b and e > c and e > d):
        quinto = e

    if (a > segundo and a < cuarto):
        tercero = a
    elif (b > segundo and b < cuarto):
        tercero = b
    elif (c > segundo and c < cuarto):
        tercero = c
    elif (d > segundo and d < cuarto):
        tercero = d
    elif (e > primero and e > segundo and e < cuarto and e < quinto):
        tercero = e
    return tercero

def Poten(a : float, b : float, c : float, d : float, e : float) -> float:
    if a < b and a < c and a < d and a < e :
        primero = a
    elif b < a and b < c and b < d and b < e :
        primero = b
    elif c < b and c < a and c < d and c < e :
        primero = c
    elif d < b and d < c and d < a and d < e :
        primero = d
    else :
        primero = e

    if (a > b and a < c and a < d and a < e) or (a > c and a < b and a < d and a < e) or (a > d and a < b and a < c and a < e) or (a > e and a < b and a < c and a < d):
        segundo = a
    elif (b > a and b < c and b < d and b < e) or (b > c and b < a and b < d and b < e) or (b > d and b < a and b < c and b < e) or (b > e and b < a and b < c and b < d):
        segundo = b
    elif (c > a and c < b and c < d and c < e) or (c > b and c < a and c < d and c < e) or (c > d and c < a and c < b and c < e) or (c > e and c < a and c < b and c < d):
        segundo = c
    elif (d > a and d < b and d < c and d < e) or (d > b and d < a and d < c and d < e) or (d > c and d < a and d < b and d < e) or (d > e and d < a and d < b and d < c):
        segundo = d
    elif (e > a and e < b and e < c and e < d) or (e > b and e < a and c < c and e < d) or (e > c and e < a and e < b and e < d) or (e > d and e < a and e < b and e < c):
        segundo = e


    if (a < e and a > b and a > c and a > d) or (a < d and a > b and a > c and a > e) or (a < c and a > b and a > d and a < e) or (a < b and a > c and a > d and a > e):
        cuarto = a
    elif (b < e and b > a and b > c and b > d) or (b < d and b > a and b > c and b > e) or (b < c and b > a and b > d and b < e) or (b < a and b > c and b > d and b > e):
        cuarto = b
    elif (c < e and c > a and c > b and c > d) or (c < d and c > a and c > b and c > e) or (c < b and c > a and d > d and c < e) or (c < a and c > b and c > d and c > e):
        cuarto = c
    elif (d < e and d > a and d > b and d > c) or (d < c and d > a and d > b and d > e) or (d < b and d > a and d > c and d < e) or (d < a and d > b and d > c and d > d):
        cuarto = d
    elif(e < a and e > b and e > c and e > d) or (e < b and e > a and e > c and e > d) or (e < c and e > a and e > b and e < d) or (e < d and e > a and e > b and e > c):
        cuarto = e

    if (a > b and a > c and a > d and a > e):
        quinto = a
    elif (b > a and b > c and b > d and b < e):
        quinto = b
    elif (c > a and c > b and c > d and c > e):
        quinto = c
    elif (d > a and d > b and d > c and d > e):
        quinto = d
    elif (e > a and e > b and e > c and e > d):
        quinto = e

    if (a > segundo and a < cuarto):
        tercero = a
    elif (b > segundo and b < cuarto):
        tercero = b
    elif (c > segundo and c < cuarto):
        tercero = c
    elif (d > segundo and d < cuarto):
        tercero = d
    elif (e > primero and e > segundo and e < cuarto and e < quinto):
        tercero = e
    return quinto**primero

def Mp(a : float, b : float, c : float, d : float, e : float) -> float:
    return (a*b*c*d*e) ** (0.2)

def RaizCub(a : float, b : float, c : float, d : float, e : float) -> float:
    if a < b and a < c and a < d and a < e :
        primero = a
    elif b < a and b < c and b < d and b < e :
        primero = b
    elif c < b and c < a and c < d and c < e :
        primero = c
    elif d < b and d < c and d < a and d < e :
        primero = d
    else :
        primero = e

    if (a > b and a < c and a < d and a < e) or (a > c and a < b and a < d and a < e) or (a > d and a < b and a < c and a < e) or (a > e and a < b and a < c and a < d):
        segundo = a
    elif (b > a and b < c and b < d and b < e) or (b > c and b < a and b < d and b < e) or (b > d and b < a and b < c and b < e) or (b > e and b < a and b < c and b < d):
        segundo = b
    elif (c > a and c < b and c < d and c < e) or (c > b and c < a and c < d and c < e) or (c > d and c < a and c < b and c < e) or (c > e and c < a and c < b and c < d):
        segundo = c
    elif (d > a and d < b and d < c and d < e) or (d > b and d < a and d < c and d < e) or (d > c and d < a and d < b and d < e) or (d > e and d < a and d < b and d < c):
        segundo = d
    elif (e > a and e < b and e < c and e < d) or (e > b and e < a and c < c and e < d) or (e > c and e < a and e < b and e < d) or (e > d and e < a and e < b and e < c):
        segundo = e


    if (a < e and a > b and a > c and a > d) or (a < d and a > b and a > c and a > e) or (a < c and a > b and a > d and a < e) or (a < b and a > c and a > d and a > e):
        cuarto = a
    elif (b < e and b > a and b > c and b > d) or (b < d and b > a and b > c and b > e) or (b < c and b > a and b > d and b < e) or (b < a and b > c and b > d and b > e):
        cuarto = b
    elif (c < e and c > a and c > b and c > d) or (c < d and c > a and c > b and c > e) or (c < b and c > a and d > d and c < e) or (c < a and c > b and c > d and c > e):
        cuarto = c
    elif (d < e and d > a and d > b and d > c) or (d < c and d > a and d > b and d > e) or (d < b and d > a and d > c and d < e) or (d < a and d > b and d > c and d > d):
        cuarto = d
    elif(e < a and e > b and e > c and e > d) or (e < b and e > a and e > c and e > d) or (e < c and e > a and e > b and e < d) or (e < d and e > a and e > b and e > c):
        cuarto = e

    if (a > b and a > c and a > d and a > e):
        quinto = a
    elif (b > a and b > c and b > d and b < e):
        quinto = b
    elif (c > a and c > b and c > d and c > e):
        quinto = c
    elif (d > a and d > b and d > c and d > e):
        quinto = d
    elif (e > a and e > b and e > c and e > d):
        quinto = e

    if (a > segundo and a < cuarto):
        tercero = a
    elif (b > segundo and b < cuarto):
        tercero = b
    elif (c > segundo and c < cuarto):
        tercero = c
    elif (d > segundo and d < cuarto):
        tercero = d
    elif (e > primero and e > segundo and e < cuarto and e < quinto):
        tercero = e
    return primero**(1/3)

if __name__ == "__main__":
    a = float (input("Ingrese un numero: "))
    b = float (input("Ingrese un numero: "))
    c = float (input("Ingrese un numero: "))
    d = float (input("Ingrese un numero: "))
    e = float (input("Ingrese un numero: "))
    Promedio = Prom(a, b, c, d, e)
    print("el promedio es: " + str(Promedio))
    Mediana = Med(a, b, c, d, e)
    print("la mediana es: " + str(Mediana))
    PromedioMultiplicativo = Mp(a, b, c, d, e)
    print("el promedio multiplicativo es: " + str(PromedioMultiplicativo))
    OrdenAscend = OrdAscendente(a, b, c, d, e)
    print("el orden ascendente es: " + str(OrdenAscend))
    OrdenDescend= OrdDescendiente(a, b, c, d, e)
    print("el otrden descendiente es: " + str(OrdenDescend))
    Potencia = Poten(a, b, c, d, e)
    print("la potencia del mayor número elevado al menor número es: " + str(Potencia))
    RaizCubica = RaizCub(a, b, c, d, e)
    print("la raíz cúbica del menor número es: " + str(RaizCubica))