import unittest
from main import Point3D, Triangle

class TestPoint3D(unittest.TestCase):
    def test_init(self):
        """Test that the Point3D constructor initializes coordinates correctly."""
        p = Point3D(1, 2, 3)
        self.assertIsInstance(p.X, float)
        self.assertIsInstance(p.Y, float)
        self.assertIsInstance(p.Z, float)
        self.assertEqual(p.X, 1.0)
        self.assertEqual(p.Y, 2.0)
        self.assertEqual(p.Z, 3.0)

    def test_repr(self):
        """Test the string representation of a Point3D object."""
        p = Point3D(1.23456, 2.34567, 3.45678)
        self.assertEqual(repr(p), 'Point3D(1.2346,2.3457,3.4568)')

    def test_add(self):
        """Test the addition of two Point3D objects."""
        p1 = Point3D(1, 2, 3)
        p2 = Point3D(4, 5, 6)
        p3 = p1 + p2
        self.assertEqual(p3.X, 5.0)
        self.assertEqual(p3.Y, 7.0)
        self.assertEqual(p3.Z, 9.0)

    def test_truediv_scalar(self):
        """Test the division of a Point3D object by a scalar."""
        p1 = Point3D(2, 4, 6)
        p2 = p1 / 2
        self.assertEqual(p2.X, 1.0)
        self.assertEqual(p2.Y, 2.0)
        self.assertEqual(p2.Z, 3.0)

        with self.assertRaises(ZeroDivisionError):
            p1 / 0

    def test_truediv_point(self):
        """Test the division of a Point3D object by another Point3D object."""
        p1 = Point3D(2, 8, 18)
        p2 = Point3D(2, 4, 3)
        p3 = p1 / p2
        self.assertEqual(p3.X, 1.0)
        self.assertEqual(p3.Y, 2.0)
        self.assertEqual(p3.Z, 6.0)

        p4 = Point3D(1, 0, 1)
        with self.assertRaises(ZeroDivisionError):
            p1 / p4

class TestTriangle(unittest.TestCase):
    def test_init(self):
        """Test that the Triangle constructor initializes vertices correctly."""
        p1 = Point3D(1, 2, 3)
        p2 = Point3D(4, 5, 6)
        p3 = Point3D(7, 8, 9)
        t = Triangle(p1, p2, p3)
        self.assertIs(t.P1, p1)
        self.assertIs(t.P2, p2)
        self.assertIs(t.P3, p3)

    def test_repr(self):
        """Test the string representation of a Triangle object."""
        p1 = Point3D(1, 2, 3)
        p2 = Point3D(4, 5, 6)
        p3 = Point3D(7, 8, 9)
        t = Triangle(p1, p2, p3)
        expected_repr = (
            "Triangle(Point3D(1.0000,2.0000,3.0000),"
            "Point3D(4.0000,5.0000,6.0000),"
            "Point3D(7.0000,8.0000,9.0000))"
        )
        self.assertEqual(repr(t), expected_repr)

    def test_center(self):
        """Test the calculation of the triangle's geometric center."""
        p1 = Point3D(0, 0, 0)
        p2 = Point3D(3, 6, 9)
        p3 = Point3D(0, 0, 0)
        t = Triangle(p1, p2, p3)
        center = t.center
        self.assertEqual(center.X, 1.0)
        self.assertEqual(center.Y, 2.0)
        self.assertEqual(center.Z, 3.0)

if __name__ == '__main__':
    unittest.main()
