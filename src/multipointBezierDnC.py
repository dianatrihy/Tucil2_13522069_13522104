import matplotlib.pyplot as plt
from datatypes import Point

# Definisikan kelas multipointBezierDnC
class multipointBezierDnC:
    # Inisialisasi atribut dari objek multipointBezierDnC
    def __init__(self, points, iterations):
        self.points = points # List of Point
        self.iterations = iterations # integer
        self.elapsed_time = 0.0

    # Fungsi mencari titik tengah dari masukan 2 titik
    def find_center_point(self, point1, point2):
        x = (point1.x + point2.x)/2
        y = (point1.y + point2.y)/2
        center_point = Point(x,y)
        return center_point # Point

    # Fungsi membuat list titik tengah dari list beberapa titik secara terurut
    def list_center_point(self, listpoints):
        new_points = []
        n = len(listpoints)

        for i in range (n-1):
            new_points.append(self.find_center_point(listpoints[i], listpoints[i+1]))

        return new_points # List of Point
    
    def visualization_step(self, new_points):
        x_points = [point.x for point in new_points]
        y_points = [point.y for point in new_points]
        plt.scatter(x_points, y_points, color='orange', s=5.5, zorder=5)
        plt.plot(x_points, y_points, color='gold', linestyle='dashed')

    # Fungsi membuat list titik-titik hasil generate kurava bezier 
    def bezier_multipoint(self, listpoints, iterations):
        n = len(listpoints)

        # (Solve/Conquer) Jika sudah tidak dilakukan lagi iterasi, kembalikan titik awal dan akhir
        if iterations == 0:
            return [listpoints[0], listpoints[n-1]]

        # (pre-Divide) Memasukkan titik awal pada bagian kiri dan titik akhir pada bagian kanan (list titik yang akan digunakan untuk iterasi selanjutnya)
        left_points = []
        left_points.append(listpoints[0])
        right_points = []
        right_points.append(listpoints[n-1])

        # (pre-Divide) Mencari titik tengah dari listpoint serta memasukkan ke bagian kiri dan kanan untuk titik-titik yang diperlukan untuk iterasi selanjutnya
        # Titik yang diperlukan untuk iterasi selanjutnya adalah titik paling awal dan titik paling akhir pada list new_points
        new_points = self.list_center_point(listpoints)
        left_points.append(new_points[0])
        if len(new_points) == 1:
            right_points.insert(0, new_points[0])
        else:
            right_points.insert(0, new_points[len(new_points)-1])
        
        self.visualization_step(new_points)

        # (pre-Divide) Dilakukan secara berulang hingga ditemukan hanya satu titik tengah yang menjadi hasil kurva bezier nantinya
        while len(new_points) > 1:
            new_points = self.list_center_point(new_points)
            self.visualization_step(new_points)
            left_points.append(new_points[0])
            if len(new_points) == 1:
                right_points.insert(0, new_points[0])
            else:
                right_points.insert(0, new_points[len(new_points)-1])

        # (Divide) Melakukan rekursif setiap bagian kiri dan kanan, hingga iterasi habis
        left_curve = self.bezier_multipoint(left_points, iterations-1)
        right_curve = self.bezier_multipoint(right_points, iterations-1)

        # (Combine) Gabungkan kurva dari kedua sisi dan hilangkan titik terakhir dari sisi kiri untuk menghindari duplikasi
        return left_curve[:-1] + right_curve # List of Point
    
    def multipoint_bezier(self):
        curve_points = self.bezier_multipoint(self.points, self.iterations)
        return curve_points # List of Point
