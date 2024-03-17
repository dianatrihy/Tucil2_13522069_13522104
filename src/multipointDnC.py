from datatypes import Point

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
        new_points = list_center_point(new_points)
        left_points.append(new_points[0])
        if len(new_points) == 1:
            right_points.insert(0, new_points[0])
        else:
            right_points.insert(0, new_points[len(new_points)-1])

    left_curve = bezier_multipoint(left_points, iterations-1)
    right_curve = bezier_multipoint(right_points, iterations-1)

    return left_curve[:-1] + right_curve