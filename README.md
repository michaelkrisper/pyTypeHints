# 3D Point and Triangle Geometry

This script defines two classes, `Point3D` and `Triangle`, for performing simple 3D geometry operations.

## Features

*   **Point3D**: Represents a point in 3D space with X, Y, and Z coordinates.
    *   Supports addition of two points.
    *   Supports division by a scalar or another point.
*   **Triangle**: Represents a triangle defined by three `Point3D` vertices.
    *   Can calculate its geometric center.

## How to Run

To run the script, simply execute it from your terminal:

```bash
python main.py
```

## Example Output

Running the script will produce the following output:

```
Point3D(3.0,4.0,5.0)
Point3D(2.0,4.0,5.0)
Point3D(5.0,8.0,10.0)
Triangle(Point3D(3.0,4.0,5.0),Point3D(2.0,4.0,5.0),Point3D(1.0,2.0,-11.0))
Point3D(2.0,3.333,-0.3333)
```
