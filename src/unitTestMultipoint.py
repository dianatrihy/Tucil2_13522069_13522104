import matplotlib.pyplot as plt
import time 
from datatypes import Point
# fungsi membuat list titik kurva bezier kuadratik
def generate_quadratic_bezier(P0, P1, P2, iterations):
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
    
    left_curve = generate_quadratic_bezier(P0, Q0, R0, iterations - 1)
    right_curve = generate_quadratic_bezier(R0, Q1, P2, iterations - 1)
    
    return left_curve[:-1] + right_curve

# fungsi mencari titik tengah dari dua titik
def find_center_point(point1, point2):
    x = (point1.x + point2.x)/2
    y = (point1.y + point2.y)/2
    center_point = Point(x,y)
    return center_point

# fungsi mengumpulkan titik tengah dari sebuah list titik terurut
def list_center_point(listpoints):
    new_points = []
    n = len(listpoints)

    for i in range (n-1):
        new_points.append(find_center_point(listpoints[i], listpoints[i+1]))

    return new_points

# fungsi membuat list titik kurva bezier secara general
def bezier_multipoint(listpoints, iterations):
    if iterations == 0:
        return [listpoints[0], listpoints[len(listpoints)-1]]

    n = len(listpoints)

    left_points = []
    left_points.append(listpoints[0])
    right_points = []
    right_points.append(listpoints[n-1])

    new_points = list_center_point(listpoints)
    left_points.append(new_points[0])
    if len(new_points) == 1:
        right_points.insert(0, new_points[0])
    else:
        right_points.insert(0, new_points[len(new_points)-1])

    while len(new_points) > 1:
        print_list_points(new_points)
        new_points = list_center_point(new_points)
        left_points.append(new_points[0])
        if len(new_points) == 1:
            right_points.insert(0, new_points[0])
        else:
            right_points.insert(0, new_points[len(new_points)-1])

    print("left points:" + str(iterations))
    print_list_points(left_points)
    print("right points:" + str(iterations))
    print_list_points(right_points)

    left_curve = bezier_multipoint(left_points, iterations-1)
    right_curve = bezier_multipoint(right_points, iterations-1)

    return left_curve[:-1] + right_curve

# fungsi membuat visualisasi dalam plot
def plot_curve(points, iterations):
    start_time = time.time()
    # curve = generate_quadratic_bezier(points[0], points[1], points[2], iterations)
    curve = bezier_multipoint(points, iterations)
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
    plt.title(f'Quadratic Bézier Curve (Iterations: {iterations})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

# fungsi menerima input point
def input_points():
    points = []
    for i in range(4):
        x = float(input(f"Masukkan koordinat x titik ke-{i+1}: "))
        y = float(input(f"Masukkan koordinat y titik ke-{i+1}: "))
        point = Point(x, y)
        points.append(point)
    return points

def print_list_points(points):
    for i, point in enumerate(points):
        print(f"Titik {i+1}: (x={point.x}, y={point.y})")

points = input_points()
print("Titik yang dimasukkan:")
for i, point in enumerate(points):
    print(f"Titik {i+1}: (x={point.x}, y={point.y})")

iterations = int(input(f"Masukkan iterasi: "))

plot_curve(points, iterations)
