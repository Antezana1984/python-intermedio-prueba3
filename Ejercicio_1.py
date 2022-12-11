
'''
                  Matías Moreno Barrios
┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿   Cristian Antezana Pizarro
'''

import math

class Cuadrado:
    
    # Constructor
    def __init__(self, largo):
        self.largo = largo
        self.lados = 4

    # Metodos    

    def cantidad_lados(self):
        return str(self.lados)

    def devuelve_largo(self):
        return str(self.largo)

    def calcula_area(self):
        return str(self.largo * self.largo)
    
    def calcula_perimetro(self):
        return str(self.largo * 4)
    
    def imprimir(self):
        print("CUADRADO")
        print("Cantidad de lados: " + self.cantidad_lados())
        print("El largo del lado es: " + self.devuelve_largo())
        print("El área es : " + self.calcula_area())
        print("El perímetro es: " + self.calcula_perimetro())

class Rectangulo:
    
    # Constructor
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        self.lados = 4

    # Metodos    

    def cantidad_lados(self):
        return str(self.lados)

    def devuelve_largo(self):
        return str(self.largo)

    def devuelve_ancho(self):
        return str(self.ancho)

    def calcula_area(self):
        return str(self.largo * self.ancho)
    
    def calcula_perimetro(self):
        return str((self.largo + self.ancho) * 2)
    
    def imprimir(self):
        print("RECTANGULO")
        print("Cantidad de lados: " + self.cantidad_lados())
        print("El largo es : " + self.devuelve_largo())
        print("El ancho es : " + self.devuelve_ancho())
        print("El área es : " + self.calcula_area())
        print("El perímetro es: " + self.calcula_perimetro())

class Triangulo:
    
    # Constructor
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.lados = 3

    # Metodos    

    def cantidad_lados(self):
        return str(self.lados)

    def devuelve_lado_a(self):
        return str(self.a)

    def devuelve_lado_b(self):
        return str(self.b)

    def devuelve_lado_c(self):
        return str(self.c)

    def calcula_perimetro(self):
        return str(self.a + self.b + self.c)

    def calcula_area(self):
        # Emplea fórmula para calcular área en función de
        # los lados.
        auxiliar = ( self.a + self.b + self.c ) / 2
        area = math.sqrt( auxiliar * ( auxiliar - self.a ) * ( auxiliar - self.b ) * ( auxiliar - self.c ) )
        return str(round(area, 3))
    
    def calcula_perimetro(self):
        return str(self.a + self.b + self.c)
    
    def imprimir(self):
        print("TRIÁNGULO")
        print("Cantidad de lados: " + self.cantidad_lados())
        print("El lado 'a' es : " + self.devuelve_lado_a())
        print("El lado 'b' es : " + self.devuelve_lado_b())
        print("El lado 'c' es : " + self.devuelve_lado_c())        
        print("El área es : " + self.calcula_area())
        print("El perímetro es: " + self.calcula_perimetro())

class Circulo:
    
    # Constructor
    def __init__(self, radio):
        self.radio = radio
        self.lados = 0

    # Metodos    

    def cantidad_lados(self):
        return str(self.lados)

    def devuelve_radio(self):
        return str(self.radio)

    def calcula_area(self):
        area = ( self.radio ** 2 ) * math.pi
        return str(round(area, 3))
    
    def calcula_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return str(round(perimetro, 3))
    
    def imprimir(self):
        print("CIRCULO")
        print("Cantidad de lados: " + self.cantidad_lados())
        print("El radio  es: " + self.devuelve_radio())
        print("El área es : " + self.calcula_area())
        print("El perímetro es: " + self.calcula_perimetro())

def main(): 
    cuadrado = Cuadrado(5)
    cuadrado.imprimir()

    rectangulo = Rectangulo(5, 10)
    rectangulo.imprimir()

    triangulo = Triangulo(5, 6, 7)
    triangulo.imprimir()

    circulo = Circulo(10)
    circulo.imprimir()



if __name__ == '__main__':
    main()
