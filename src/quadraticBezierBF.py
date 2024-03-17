import matplotlib.pyplot as plt
import numpy as np
from datatypes import Point

# Definisikan kelas quadraticBezierBF
class quadraticBezierBF:
    # Inisialisasi atribut dari objek quadraticBezierBF
    def __init__(self, points, iterations):
        self.p0 = points[0]
        self.p1 = points[1]
        self.p2 = points[2]
        self.iterations = iterations
        self.elapsed_time = 0.0

    # Fungsi untuk menghasilkan titik-titik pada kurva Bézier kuadratik menggunakan metode Brute Force
    def quadratic_bezier(self):
        points = []
        for t in np.linspace(0, 1, 2 ** self.iterations + 1):
            x = (1 - t) ** 2 * self.p0.x + 2 * (1 - t) * t * self.p1.x + t ** 2 * self.p2.x
            y = (1 - t) ** 2 * self.p0.y + 2 * (1 - t) * t * self.p1.y + t ** 2 * self.p2.y
            point = Point(x, y)
            points.append(point)  
            
        return points
