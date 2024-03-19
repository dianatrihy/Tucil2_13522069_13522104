# Menampilkan menu pilihan kepada pengguna
def displayMenu():
    print("\n==================== MENU ====================")
    print("1. Quadratic Bézier Curve (Brute Force)")
    print("2. Quadratic Bézier Curve (Divide and Conquer)")
    print("3. Comparing Algorithm")
    print("4. Multi Bézier Curve (Divide and Conquer)")
    print("")

# Menampilkan perbandingan waktu antara algoritma Brute Force dan Divide and Conquer
def displayComparison(elapsed_time_bf, elapsed_time_dnc):
    print("\n========== Membandingkan Algoritma ===========")
    print("Brute Force")
    print("Elapsed time: {:.4e} seconds\n".format(elapsed_time_bf))
    
    print("Divide and Conquer")
    print("Elapsed time: {:.4e} seconds\n".format(elapsed_time_dnc))

    print("=============================== Analisis ================================")
    if elapsed_time_bf < elapsed_time_dnc:
        print("Pembentukan kurva Bézier lebih cepat dengan Algoritma Brute Force dengan selisih waktu eksekusi: ")
        print(elapsed_time_dnc - elapsed_time_bf)
    elif elapsed_time_bf > elapsed_time_dnc:
        print("Pembentukan kurva Bézier lebih cepat dengan Algoritma Divide and Conquer dengan selisih waktu eksekusi")
        print(elapsed_time_bf - elapsed_time_dnc)
    else:
        print("Waktu pembentukan kurva Bezier sama cepatnya dengan kedua metode.")

    

# Menampilkan jumlah total titik kontrol
def displayTotalPoints(iterations):
    print(f"Total points: {2**iterations+1}\n")

# Menampilkan waktu yang diperlukan untuk pembentukan kurva
def displayElapsedTime(points, iterations, curve_method):
    elapsed_time = calculateElapsedTime(points, iterations, curve_method)
    print("Elapsed time: {:.4e} seconds\n".format(elapsed_time))

# Menghitung waktu yang diperlukan untuk pembentukan kurva
def calculateElapsedTime(points, iterations, curve_method):
    import time
    from quadraticBezierBF import quadraticBezierBF
    from quadraticBezierDnC import quadraticBezierDnC

    start_time = time.time()
    if curve_method == 'Brute Force':
        _ = quadraticBezierBF(points, iterations).quadratic_bezier()
    elif curve_method == 'Divide and Conquer':
        _ = quadraticBezierDnC(points, iterations).quadratic_bezier()
    end_time = time.time()

    elapsed_time = end_time - start_time
    return elapsed_time