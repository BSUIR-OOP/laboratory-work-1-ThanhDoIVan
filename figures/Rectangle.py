from Figures import Figures
class Rectangle(Figures):
    def output(self):
        print(f'Rectangle ([{self.x1}, {self.y1}], [{self.x2}, {self.y2}])')
