import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
from quadraticBezierBF import quadraticBezierBF
from quadraticBezierDncVis import quadraticBezierDnCVis
from multipointBezierDnC import multipointBezierDnC
from input import getInputQuadratic, getInputMultipoint

# Fungsi untuk menampilkan kurva Bézier kuadratik
def plot_curve(curve_method):
    
    # Memilih metode pembentukan kurva Bézier berdasarkan pilihan pengguna
    if curve_method == 'Brute Force':
        points, iterations = getInputQuadratic()
        bezier_curve = quadraticBezierBF(points, iterations)  
        curve_points = bezier_curve.quadratic_bezier()
        
        # Menyiapkan plot untuk animasi
        fig, ax = plt.subplots()
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title(f'Quadratic Bézier Curve with {bezier_curve.iterations} Iteration {curve_method}')
        
        # Inisialisasi plot untuk animasi
        curve_lines = []
        for i in range(len(curve_points) - 1):
            curve_line, = ax.plot([], [], color='royalblue')
            curve_lines.append(curve_line)
        
        # Menampilkan titik awal input
        x_points = [point.x for point in points]
        y_points = [point.y for point in points]
        ax.scatter(x_points, y_points, color='darkred', zorder=5)
        ax.plot(x_points, y_points, color='red', linestyle='dashed')
        
        # Fungsi inisialisasi untuk animasi
        def init():
            for line in curve_lines:
                line.set_data([], [])
            return curve_lines
        
        # Fungsi update untuk animasi
        def update(frame):
            for i in range(len(curve_lines)):
                if frame > i:
                    x_data = [curve_points[i].x, curve_points[i+1].x]
                    y_data = [curve_points[i].y, curve_points[i+1].y]
                    curve_lines[i].set_data(x_data, y_data)
            return curve_lines

        # Menampilkan animasi
        ani = FuncAnimation(fig, update, frames=len(curve_points), init_func=init, blit=True, repeat=False)
        
        # Menampilkan grid
        ax.grid(True)
        plt.show()
    
    # Untuk metode selain 'Brute Force', tampilkan plot tanpa animasi
    else:
        if curve_method == 'Divide and Conquer':
            points, iterations = getInputQuadratic()
            start_time = time.time()
            bezier_curve = quadraticBezierDnCVis(points, iterations)  
            curve_points = bezier_curve.quadratic_bezier()
        elif curve_method == 'Divide and Conquer with Multipoint':
            points, iterations = getInputMultipoint()
            start_time = time.time()
            bezier_curve = multipointBezierDnC(points, iterations)
            curve_points = bezier_curve.multipoint_bezier()
        else:
            raise ValueError("Jenis kurva tidak valid.")
        
        # Menghitung waktu yang diperlukan untuk pembentukan kurva
        end_time = time.time() 
        elapsed_time = end_time - start_time

        # Menampilkan titik awal input
        x_points = [point.x for point in points]
        y_points = [point.y for point in points]
        plt.scatter(x_points, y_points, color='darkred', zorder=5)
        plt.plot(x_points, y_points, color='red', linestyle='dashed')
        
        # Menampilkan kurva Bézier dan titik kontrolnya
        x_curve = [point.x for point in curve_points]
        y_curve = [point.y for point in curve_points]
        plt.plot(x_curve, y_curve, color='royalblue')
        plt.scatter(x_curve, y_curve, color='blue', s=8, zorder=5)

        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        
        # Menampilkan judul plot dan waktu yang diperlukan untuk pembentukan kurva
        if curve_method == 'Divide and Conquer with Multipoint':
            plt.title(f'Bézier Curve with {bezier_curve.iterations} Iteration {curve_method}')
        else:
            plt.title(f'Quadratic Bézier Curve with {bezier_curve.iterations} Iteration {curve_method}')
        plt.text(0.5, 0.05, 'Elapsed time: {:.4e} seconds'.format(elapsed_time), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

        # Menampilkan grid
        plt.grid(True)
        plt.show()