def find_line_eqn(a, b):
    gradient = (a[1] - b[1]) / (a[0] - b[0])
    y_intercept = a[1] - gradient * a[0]
    return gradient, y_intercept

def line_intersection(line1, line2):
    m1, c1 = find_line_eqn(line1[0], line1[1])
    m2, c2 = find_line_eqn(line2[0], line2[1])

    x_int = (c2 - c1) / (m1 - m2)

    if (x_int < max(min(line1[0][0], line1[1][0]), min(line2[0][0], line2[1][0])) or
        x_int > min(max(line1[0][0], line1[1][0]), max(line2[0][0], line2[1][0]))):
        return False

    return True
