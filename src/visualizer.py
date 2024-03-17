import matplotlib.pyplot as plt
import numpy as np
import time
from quadraticBezierBF import quadraticBezierBF
from quadraticBezierDnC import quadraticBezierDnC
from input import getInputQuadratic 

# Fungsi untuk menampilkan kurva Bézier kuadratik
def plot_curve(curve_method):
    points, iterations = getInputQuadratic()
    
    # Memilih metode pembentukan kurva Bézier berdasarkan pilihan pengguna
    start_time = time.time()
    if curve_method == 'Brute Force':
        bezier_curve = quadraticBezierBF(points, iterations)  
        curve_points = bezier_curve.quadratic_bezier()
    elif curve_method == 'Divide and Conquer':
        bezier_curve = quadraticBezierDnC(points, iterations)  
        curve_points = bezier_curve.quadratic_bezier()
    else:
        raise ValueError("Jenis kurva tidak valid.")
    
    # Menghitung waktu yang diperlukan untuk pembentukan kurva
    end_time = time.time() 
    elapsed_time = end_time - start_time
    
    # Menampilkan kurva Bézier dan titik kontrolnya
    curve_points = np.array(curve_points)
    plt.plot(curve_points[:, 0], curve_points[:, 1])
    plt.scatter(curve_points[:, 0], curve_points[:, 1], color='blue', s=5, zorder=5)  
    plt.scatter([bezier_curve.p0.x, bezier_curve.p1.x, bezier_curve.p2.x], [bezier_curve.p0.y, bezier_curve.p1.y, bezier_curve.p2.y], color='red', zorder=5)
    plt.plot([bezier_curve.p0.x, bezier_curve.p1.x, bezier_curve.p2.x], [bezier_curve.p0.y, bezier_curve.p1.y, bezier_curve.p2.y], color='red', linestyle='dashed')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # Menampilkan judul plot dan waktu yang diperlukan untuk pembentukan kurva
    plt.title(f'Quadratic Bézier Curve with {bezier_curve.iterations} Iteration {curve_method}')
    plt.text(0.5, 0.05, 'Elapsed time: {:.4e} seconds'.format(elapsed_time), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

    # Menampilkan grid
    plt.grid(True)
    plt.show()
