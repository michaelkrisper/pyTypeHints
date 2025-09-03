class Point3D:
    """Represents a point in 3D space."""
    def __init__(self, x: float, y: float, z: float):
        """
        Initializes a Point3D object.

        Args:
            x: The x-coordinate.
            y: The y-coordinate.
            z: The z-coordinate.
        """
        self.X = float(x)
        self.Y = float(y)
        self.Z = float(z)

    def __repr__(self):
        """Returns a string representation of the Point3D object."""
        return '{}({X:.4},{Y:.4},{Z:.4})'.format(self.__class__.__name__, **vars(self))

    def __add__(self, other: 'Point3D'):
        """
        Adds two Point3D objects.

        Args:
            other: The other Point3D object to add.

        Returns:
            A new Point3D object that is the sum of the two points.
        """
        return Point3D(self.X + other.X, self.Y + other.Y, self.Z + other.Z)

    def __truediv__(self, other):
        """
        Divides a Point3D object by a scalar or another Point3D object.

        Args:
            other: The scalar or Point3D object to divide by.

        Returns:
            A new Point3D object that is the result of the division.
        """
        if isinstance(other, float) or isinstance(other, int):
            return Point3D(self.X/other, self.Y/other, self.Z/other)
        if isinstance(other, Point3D):
            return Point3D(self.X / other.X, self.Y / other.Y, self.Z/other.Z)


class Triangle:
    """Represents a triangle in 3D space."""
    def __init__(self, p1: Point3D, p2: Point3D, p3: Point3D):
        """
        Initializes a Triangle object.

        Args:
            p1: The first vertex of the triangle.
            p2: The second vertex of the triangle.
            p3: The third vertex of thetriangle.
        """
        self.P1 = p1
        self.P2 = p2
        self.P3 = p3

    @property
    def center(self):
        """Calculates the center of the triangle."""
        return (self.P1 + self.P2 + self.P3) / 3

    def __repr__(self):
        """Returns a string representation of the Triangle object."""
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