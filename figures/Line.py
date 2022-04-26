from Figures import Figures
class Line(Figures):
    def output(self):
        print(f'Line ([{self.x1}, {self.y1}], [{self.x2}, {self.y2}])')
