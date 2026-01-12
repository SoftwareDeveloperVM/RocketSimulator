# calculus
def derivative(function, x, limit):
    dydx = (function(x + limit) - function(x)) / limit
    return dydx


def integral(start, stop, function, step):
    sumvalue = 0
    val = start + ((stop - start) / step)
    count = 0
    while True:
        sumvalue += function(val)
        val += ((stop - start) / step)
        count += 1
        if count >= (step):
            break
    return (sumvalue * (stop - start) / step)


# useful formulas
def distance_formula(x2, x1, y2, y1):
    return (((x2**2)-(x1**2))+((y2**2)-(y1**2)))**0.5


# vectors
def vector(direction, magnitude):
    return [direction, magnitude]


def unit_vector(vector):
    return vector / abs(vector)


def vector_length(vx, vy):
    return ((vx ** 2) + (vy ** 2)) ** 0.5


# linear algebra
def matrix(rows, columns, characters=0):
    matrix = []
    for element in range(rows):
        row = []
        for element in range(columns):
            row.append(characters)
        matrix.append(row)
    print(matrix)
