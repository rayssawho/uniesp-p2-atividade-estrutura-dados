class Aviao:
    def __init__(self, modelo, companhia, numeroVoo):
        self.modelo = modelo
        self.companhia = companhia
        self.numeroVoo = numeroVoo
    
    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
        self.modelo = modelo
        
    def getCompanhia(self):
        return self.companhia
    
    def setCompanhia(self, companhia):
        self.companhia = companhia
    
    def getNumeroVoo(self):
        return self.numeroVoo
    
    def setNumeroVoo(self, numeroVoo):
        self.numeroVoo = numeroVoo
