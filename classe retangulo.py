class retangulo():
    def __init__(self,a,b):
        self.altura = a + 3
        self.base = b + 2

    def retornalados(self):
        return self.altura, self.base

    def area(self):
        return self.altura * self.base

    def perimetro(self):
        return self.altura *2 + self.base*2
