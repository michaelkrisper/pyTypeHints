class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self.X = float(x)
        self.Y = float(y)
        self.Z = float(z)

    def __repr__(self):
        return '{}({X:.4},{Y:.4},{Z:.4})'.format(self.__class__.__name__, **vars(self))

    def __add__(self, other: 'Point3D'):
        return Point3D(self.X + other.X, self.Y + other.Y, self.Z + other.Z)

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Point3D(self.X/other, self.Y/other, self.Z/other)
        if isinstance(other, Point3D):
            return Point3D(self.X / other.X, self.Y / other.Y, self.Z/other.Z)


class Triangle:
    def __init__(self, p1: Point3D, p2: Point3D, p3: Point3D):
        self.P1 = p1
        self.P2 = p2
        self.P3 = p3

    @property
    def center(self):
        return (self.P1 + self.P2 + self.P3) / 3

    def __repr__(self):
        return '{}({P1},{P2},{P3})'.format(self.__class__.__name__, **vars(self))

if __name__ == '__main__':
    p1 = Point3D(3, 4, 5)
    print(p1)

    p2 = Point3D(2, 4, 5)
    print(p2)

    print(p1+p2)

    p3 = Point3D(1,2,-11)
    t = Triangle(p1, p2, p3)
    print(t)
    print(t.center)