from Figures import Figures
class Rhombus(Figures):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        # super() gives access to the methods of parent class
        super().__init__(x1, y1, x2, y2)
        self.x3 = x3
        self.y3 = y3
    def output(self):
        print(f'Rhombus ([{self.x1}, {self.y1}], [{self.x2}, {self.y2}], [{self.x3}, {self.y3}])')
