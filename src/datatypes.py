class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QuadraticBezier:
    def __init__(self, points, iterations):
        self.p0 = points[0]
        self.p1 = points[1]
        self.p2 = points[2]
        self.iterations = iterations
        self.elapsed_time = 0.0
        
class MultipointBezierDnC:
    def __init__(self, points, iterations):
        self.points = points # List of Point
        self.iterations = iterations # integer
        self.elapsed_time = 0.0
