# Calcular el volumen y el área superficial al ingresar r1, r2 y h
import math
def VolumenFigura(r1:float, r2:float, h:float) -> float:
    VolEsfera = (4/3) * math.pi * (r1**3)
    VolCono = (1/3) * (h) * math.pi * (r2**2)
    return VolEsfera + VolCono  

def AreaFigura(r1:float, r2:float, h:float) -> float:
    ArSupEsfera = 4 * math.pi * (r1**2)
    Hipot = (h**2 + r2**2)**0.5  # formula de la hipotenusa para hallar área superficial
    ArSupCono = (math.pi * r2 * Hipot) + (math.pi * (r2**2))
    return ArSupEsfera + ArSupCono 

if __name__ == "__main__":
    r1 = float(input("ingrese el radio de la esfera: ")) # radio en cm
    r2 = float(input("ingrese el radio del cono: ")) # radio en cm
    h = float(input("ingrese la altura del cono: ")) # altura en cm
    Volumen = VolumenFigura(r1, r2, h)
    print("el volumen de la figura es: " + str(Volumen))
    AreaSuperficial= AreaFigura(r1, r2, h)
    print("el área superficial de la figura es: " + str(AreaSuperficial))
