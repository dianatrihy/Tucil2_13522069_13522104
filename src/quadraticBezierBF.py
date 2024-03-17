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

''' 
    def plot_curve(self):
        start_time = time.time()
        curve_points = self.quadratic_bezier()
        curve_points = np.array(curve_points)
        plt.plot(curve_points[:, 0], curve_points[:, 1])
        plt.scatter(curve_points[:, 0], curve_points[:, 1], color='blue', s=5, zorder=5)  
        plt.scatter([self.p0[0], self.p1[0], self.p2[0]], [self.p0[1], self.p1[1], self.p2[1]], color='red', zorder=5)
        plt.plot([self.p0[0], self.p1[0], self.p2[0]], [self.p0[1], self.p1[1], self.p2[1]], color='red', linestyle='dashed')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title(f'Quadratic Bézier Curve with {self.iterations} Iteration Brute Force')
        end_time = time.time() 
        elapsed_time = end_time - start_time
        plt.text(0.5, 0.05, 'Elapsed time: {:.4e} seconds'.format(self.elapsed_time), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

        plt.grid(True)
        plt.show()

    def main():
    p0_input = input("Masukkan titik kontrol pertama (dipisahkan dengan koma): ")
    p1_input = input("Masukkan titik kontrol antara (dipisahkan dengan koma): ")
    p2_input = input("Masukkan titik kontrol terakhir (dipisahkan dengan koma): ")
    iterations = int(input("Masukkan jumlah iterasi: "))
    
    # Parse input coordinates
    p0 = list(map(float, p0_input.split(',')))
    p1 = list(map(float, p1_input.split(',')))
    p2 = list(map(float, p2_input.split(',')))
    
    # Plot and calculate the elapsed time of Brute Force
    start_time = time.time()
    bezier_curve = quadraticBezierBF(p0, p1, p2, iterations)
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    bezier_curve.elapsed_time = elapsed_time
    print("Elapsed time: {:.4e} seconds".format(elapsed_time))
    print(elapsed_time)
    
    bezier_curve.plot_curve()    

if __name__ == "__main__":
    main()
'''