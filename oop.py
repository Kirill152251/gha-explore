class Line:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def distance(self):
        return ((self.point1[0] - self.point2[0]) ** 2 + (self.point1[1] - self.point2[1]) ** 2) ** 0.5

    def slope(self):
        # (y2-y1/x2-x1)
        a = (max(self.point1[1], self.point2[1]) - min(self.point1[1], self.point2[1]))
        b = (max(self.point1[0], self.point2[0]) - min(self.point1[0], self.point2[0]))
        slope = a / b
        return slope

    def __str__(self):
        return (f'First point - ({self.point1[0]}, {self.point1[1]}), '
                f'Second point - ({self.point2[0]}, {self.point2[1]})')


p1 = (3, 2)
p2 = (8, 10)
li = Line(p1, p2)
print(str(li))
print(li.distance())
print(li.slope())
