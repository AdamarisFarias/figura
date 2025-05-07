class figura_geometrca
    def __init__(self, alto= 0, ancho= 0):
        self._alto = alto
        self._ancho = ancho
    def get_ancho(self):
        return self._ancho
    def get_alto(self):
        return self._alto
    def get_ancho(self,ancho):
        self.ancho = ancho
    def get_alto(self, alto):
        self.alto = alto
def str_(self):
    return f'alto: {self.alto}, ancho: {self.ancho}´
    
