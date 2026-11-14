class RacingSeries:
    
    def __init__(self,name):
        self.name = name
        self.drivers=[]
        self.points={}
        

    def add_race_result(self,finishing_order):
        for indice, driver in enumerate(finishing_order):
            posicao = indice +1
            if driver not in self.drivers:
                self.drivers.append(driver)
                self.points[driver]=0

        
        
            self.points[driver] += self.get_points(posicao)

    def get_points(self, position):
        return 0

    def get_standings(self):
        lista_ordenada = sorted(self.points.items(), key=lambda item: item[1], reverse=True)
        return lista_ordenada
            
            
        
class FormulaSeries(RacingSeries):
    super().__init__(name)

    def get_points(self, position):
        if position == 1:
            return 25
        elif position == 2:
            return 18
        elif position == 3:
            return 15
        elif position == 4:
            return 12
        elif position == 5:
            return 10
        elif position == 6:
            return 8
        elif position == 7:
            return 6
        elif position == 8:
            return 4
        elif position == 9:
            return 2
        elif position ==10
            return 1
        else:
            return 0
        
        








f1 = RacingSeries("F1")
f1 = FormulaSeries("LEAGUE 1") 
f1.add_race_result(["Lando Norris", "Max Verstappen", "Charles Leclerc", "Carlos Sainz", "Oscar Piastri"])








    


