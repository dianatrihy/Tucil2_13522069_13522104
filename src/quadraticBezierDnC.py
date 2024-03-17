import matplotlib.pyplot as plt
import numpy as np
from datatypes import Point

# Definisikan kelas quadraticBezierDnC

class quadraticBezierDnC:
    # Inisialisasi atribut dari objek quadraticBezierDnC
    def __init__(self, points, iterations):
        p0, p1, p2 = points
        self.p0 = Point(p0[0], p0[1])
        self.p1 = Point(p1[0], p1[1])
        self.p2 = Point(p2[0], p2[1])
        self.iterations = iterations
        self.elapsed_time = 0.0

    # Fungsi rekursif untuk menghasilkan kurva Bézier kuadratik menggunakan metode Divide and Conquer
    def generate_quadratic_bezier(self, P0, P1, P2, iterations):
        # (Conquer/Solve) jika iterasi sudah mencapai 0, kembalikan titik awal dan titik akhir
        if iterations == 0:
            return [P0, P2]
        
        Q0_x = (P0.x + P1.x) / 2
        Q0_y = (P0.y + P1.y) / 2
        Q0 = Point(Q0_x, Q0_y)
        Q1_x = (P1.x + P2.x) / 2
        Q1_y = (P1.y + P2.y) / 2
        Q1 = Point(Q1_x, Q1_y)
        R0_x = (Q0.x + Q1.x) / 2
        R0_y = (Q0.y + Q1.y) / 2
        R0 = Point(R0_x, R0_y)
        
        # (Devide) Rekursi untuk menemukan kurva di sisi kiri dan kanan
        left_curve = self.generate_quadratic_bezier(P0, Q0, R0, iterations - 1)
        right_curve = self.generate_quadratic_bezier(R0, Q1, P2, iterations - 1)
        
        # (Combine) Gabungkan kurva dari kedua sisi dan hilangkan titik terakhir dari sisi kiri untuk menghindari duplikasi
        return left_curve[:-1] + right_curve

    # Fungsi untuk menghasilkan titik-titik pada kurva Bézier kuadratik menggunakan metode Divide and Conquer
    def quadratic_bezier(self):
        curve_points = self.generate_quadratic_bezier(self.p0, self.p1, self.p2, self.iterations)
        return [[point.x, point.y] for point in curve_points]
    
'''     
def plot_curve(points, iterations):
    start_time = time.time()
    curve = generate_quadratic_bezier(points[0], points[1], points[2], iterations)
    end_time = time.time()

    duration = (end_time-start_time)
    print(duration)
    # Generate x-coordinates for the curve
    x_curve = [point.x for point in curve]
    y_curve = [point.y for point in curve]
    # Plot the curve and points
    plt.plot(x_curve, y_curve, marker='o', color='blue')
    # Extract x and y coordinates from points
    x_points = [point.x for point in points]
    y_points = [point.y for point in points]
    # Plot the points
    plt.plot(x_points, y_points, marker='o', linestyle='dashed', color='red')
    plt.title(f'Quadratic Bézier Curve with {iterations} Iteration Divide and Conquer')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    plt.text(0.5, 0.05, 'Elapsed time: {:.4e} seconds'.format(duration), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

    plt.grid(True)
    plt.show()

# fungsi menerima input point
def input_points():
    points = []
    for i in range(3):
        x = float(input(f"Masukkan koordinat x titik ke-{i+1}: "))
        y = float(input(f"Masukkan koordinat y titik ke-{i+1}: "))
        point = Point(x, y)
        points.append(point)
    return points

points = input_points()
print("Titik yang dimasukkan:")
for i, point in enumerate(points):
    print(f"Titik {i+1}: (x={point.x}, y={point.y})")

iterations = int(input(f"Masukkan iterasi: "))

plot_curve(points, iterations)
'''