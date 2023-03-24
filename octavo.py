# importar las funciones del punto anterior
import séptimo

if __name__ == "__main__":
    a = float(input("ingrese un número: "))
    b = float(input("ingrese un número: "))
    c = float(input("ingrese un número: "))
    d = float(input("ingrese un número: "))
    e = float(input("ingrese un número: "))

    Promedio = séptimo.Prom(a, b, c, d, e)
    print("el promedio es: " + str(Promedio))
    Mediana = séptimo.Med(a, b, c, d, e)
    print("la mediana es: " + str(Mediana))
    PromedioMultiplicativo = séptimo.Mp(a, b, c, d, e)
    print("el promedio multiplicativo es: " + str(PromedioMultiplicativo))
    OrdenAscend = séptimo.OrdAscendente(a, b, c, d, e)
    print("el orden ascendente es: " + str(OrdenAscend))
    OrdenDescend= séptimo.OrdDescendiente(a, b, c, d, e)
    print("el otrden descendiente es: " + str(OrdenDescend))
    Potencia = séptimo.Poten(a, b, c, d, e)
    print("la potencia del mayor número elevado al menor número es: " + str(Potencia))
    RaizCubica = séptimo.RaizCub(a, b, c, d, e)
    print("la raíz cúbica del menor número es: " + str(RaizCubica))