class Equation:
    def __init__(self, line):
        pos, deltas = line.split(" @ ")
        self.x_0, self.y_0, self.z_0 = (int(p) for p in pos.split(", "))
        self.d_x, self.d_y, self.d_z = (int(d) for d in deltas.split(", "))
        self.m = self.d_y / self.d_x
        self.b =  self.y_0 - self.m * self.x_0

    def intersect(self, eq):
        if self.m == eq.m:
            return None
        m_diff = self.m - eq.m
        b_diff = eq.b - self.b
        x = b_diff / m_diff
        y = self.m * x + self.b
        return (x, y)

    def is_future(self, x, y):
        if self.d_x < 0:
            if (x <= self.x_0): x_res = True
            else: x_res = False
        else:
            if (x >= self.x_0): x_res = True
            else: x_res = False

        if self.d_y < 0:
            if (y <= self.y_0): y_res = True
            else: y_res = False
        else:
            if (y >= self.y_0): y_res = True
            else: y_res = False
        return x_res and y_res

def find_intersections(equations, min_v, max_v):
    counter = 0
    for i in range(len(equations) - 1):
        for j in range(i + 1, len(equations)):
            eq0, eq1 = equations[i], equations[j]
            if eq0.m != eq1.m:
                x, y = eq0.intersect(eq1)
                if (min_v <= x and x <= max_v 
                        and min_v <= y and y <= max_v
                        and eq0.is_future(x, y)
                        and eq1.is_future(x, y)):
                    counter += 1
    return counter


equations = [Equation(line) for line in open("input.txt").read().splitlines()]
silver = find_intersections(equations, 200000000000000, 400000000000000)
print(silver)
#refuse to touch pt2

