import matplotlib.pyplot as plt
from datatypes import Point

# Definisikan kelas quadraticBezierDnC
class quadraticBezierDnC:
    # Inisialisasi atribut dari objek quadraticBezierDnC
    def __init__(self, points, iterations):
        self.p0 = points[0]
        self.p1 = points[1]
        self.p2 = points[2]
        self.iterations = iterations
        self.elapsed_time = 0.0

    # Fungsi mencari titik tengah dari masukan 2 titik
    def find_center_point(self, point1, point2):
        x = (point1.x + point2.x)/2
        y = (point1.y + point2.y)/2
        center_point = Point(x,y)
        return center_point # Point

    # Fungsi rekursif untuk menghasilkan kurva Bézier kuadratik menggunakan metode Divide and Conquer
    def generate_quadratic_bezier(self, P0, P1, P2, iterations):
        # (Conquer/Solve) jika iterasi sudah mencapai 0, kembalikan titik awal dan titik akhir
        if iterations == 0:
            return [P0, P2]
        
        # Mencari titik tengah dari ketiga titik masukan
        Q0 = self.find_center_point(P0, P1)
        Q1 = self.find_center_point(P1, P2)
        R0 = self.find_center_point(Q0, Q1)

        plt.scatter([Q0.x, R0.x, Q1.x], [Q0.y, R0.y, Q1.y], color='orange', s=5.5, zorder=5)
        plt.plot([Q0.x, R0.x, Q1.x], [Q0.y, R0.y, Q1.y], color='gold', linestyle='dashed')
        
        # (Divide and ) Rekursi untuk menemukan kurva di sisi kiri dan kanan
        left_curve = self.generate_quadratic_bezier(P0, Q0, R0, iterations - 1)
        right_curve = self.generate_quadratic_bezier(R0, Q1, P2, iterations - 1)
        
        # (Combine) Gabungkan kurva dari kedua sisi dan hilangkan titik terakhir dari sisi kiri untuk menghindari duplikasi
        return left_curve[:-1] + right_curve # List of Point

    # Fungsi untuk menghasilkan titik-titik pada kurva Bézier kuadratik menggunakan metode Divide and Conquer
    def quadratic_bezier(self):
        curve_points = self.generate_quadratic_bezier(self.p0, self.p1, self.p2, self.iterations)
        return curve_points # List of Point
    