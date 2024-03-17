import matplotlib.pyplot as plt
import numpy as np
import time
from quadraticBezierBF import quadraticBezierBF
from quadraticBezierDnC import quadraticBezierDnC
from multipointBezierDnC import multipointBezierDnC
from input import getInputQuadratic, getInputMultipoint

# Fungsi untuk menampilkan kurva Bézier kuadratik
def plot_curve(curve_method):
    
    # Memilih metode pembentukan kurva Bézier berdasarkan pilihan pengguna
    start_time = time.time()
    if curve_method == 'Brute Force':
        points, iterations = getInputQuadratic()
        bezier_curve = quadraticBezierBF(points, iterations)  
        curve_points = bezier_curve.quadratic_bezier()
    elif curve_method == 'Divide and Conquer':
        points, iterations = getInputQuadratic()
        bezier_curve = quadraticBezierDnC(points, iterations)  
        curve_points = bezier_curve.quadratic_bezier()
    elif curve_method == 'Divide and Conquer with Multipoint':
        points, iterations = getInputMultipoint()
        bezier_curve = multipointBezierDnC(points, iterations)
        curve_points = bezier_curve.multipoint_bezier()
    else:
        raise ValueError("Jenis kurva tidak valid.")
    
    # Menghitung waktu yang diperlukan untuk pembentukan kurva
    end_time = time.time() 
    elapsed_time = end_time - start_time
    
    # Menampilkan kurva Bézier dan titik kontrolnya
    curve_points = np.array(curve_points)
    plt.plot(curve_points[:, 0], curve_points[:, 1])
    plt.scatter(curve_points[:, 0], curve_points[:, 1], color='blue', s=5, zorder=5)

    # Menampilkan titik awal input
    x_points = [point[0] for point in points]
    y_points = [point[1] for point in points]
    plt.scatter(x_points, y_points, color='red', zorder=5)
    plt.plot(x_points, y_points, color='red', linestyle='dashed')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # Menampilkan judul plot dan waktu yang diperlukan untuk pembentukan kurva
    plt.title(f'Quadratic Bézier Curve with {bezier_curve.iterations} Iteration {curve_method}')
    plt.text(0.5, 0.05, 'Elapsed time: {:.4e} seconds'.format(elapsed_time), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

    # Menampilkan grid
    plt.grid(True)
    plt.show()
