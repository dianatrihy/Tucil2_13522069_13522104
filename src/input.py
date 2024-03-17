from datatypes import Point

# Mendapatkan titik koordinat dari pengguna
def getPoints(n):
    points = []
    print("\nMasukkan titik koordinat dipisahkan dengan koma (,)")
    for i in range(n):
        while True:
            point_input = input(f"Masukkan titik kontrol ke-{i+1} (P{i}): ")
            coords = point_input.split(',')
            if len(coords) != 2:
                print("Input tidak valid. Mohon pastikan titik kontrol memiliki dua angka dan dipisahkan dengan satu koma (x,y).")
                continue
            try:
                x, y = map(float, coords)
                point = Point(x,y)
                points.append(point)
                break 
            except ValueError:
                print("Input tidak valid. Mohon pastikan kedua angka adalah bilangan float atau integer.")
    return points

# Mendapatkan jumlah iterasi dari pengguna
def getIteration():
    while True:
        iterations = int(input("\nMasukkan jumlah iterasi: "))
        if iterations > 1:
            return iterations
        elif iterations == 1:
            print("Iterasi 1 akan menghasilkan kurva linear. Mohon masukkan nilai iterasi yang lebih besar dari 1.")
        else:
            print("Jumlah iterasi harus lebih besar dari 1. Mohon masukkan nilai iterasi yang valid.")

# Mendapatkan pilihan menu dari pengguna            
def getChoice():
    while True:
        choice = input("\nPilih menu (1/2/3/4): ")
        try:
            choice = int(choice)
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1, 2, 3, atau 4.")
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat antara 1 hingga 4.")
            
# Mendapatkan input titik dan iterasi untuk kurva quadratic Bézier
def getInputQuadratic():
    points = getPoints(3)
    iterations = getIteration()

    return points, iterations

# Mendapatkan input titik dan iterasi untuk kurva multipoint Bézier
def getInputMultipoint():
    n = int(input("Jumlah titik yang akan dimasukkan: "))
    points = getPoints(n)
    iterations = getIteration()

    return points, iterations
