
"""
Group: Daniel Houri , 209445071
       Eve Hackmon , 209295914
       Yakov Shtefan , 208060111
       Vladislav Rabinovich , 323602383
       Aaron Hajaj , 311338198
       Git: https://github.com/EveHackmon/Numerical_Analysis.git
"""

import numpy as np
def gaussianElimination(mat):
    N = len(mat)

    singular_flag = forward_substitution(mat)

    if singular_flag != -1:
        if mat[singular_flag][N]:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"

    # if matrix is non-singular: get solution to system using backward substitution
    return backward_substitution(mat)

# function for elementary operation of swapping two rows
def swap_row(mat, i, j):
    N = len(mat)
    for k in range(N + 1):
        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp

def forward_substitution(mat):
    N = len(mat)
    for k in range(N):
        # Partial Pivoting: Find the pivot row with the largest absolute value in the current column
        pivot_row = k
        v_max = mat[pivot_row][k]
        for i in range(k + 1, N):
            if abs(mat[i][k]) > abs(v_max):
                v_max = mat[i][k]
                pivot_row = i

        # if a principal diagonal element is zero,it denotes that matrix is singular,
        # and will lead to a division-by-zero later.
        if not mat[pivot_row][k]:
            return k  # Matrix is singular

        # Swap the current row with the pivot row
        if pivot_row != k:
            swap_row(mat, k, pivot_row)
        # End Partial Pivoting

        for i in range(k + 1, N):
            #  Compute the multiplier
            m = mat[i][k] / mat[k][k]

            # subtract fth multiple of corresponding kth row element
            for j in range(k + 1, N + 1):
                mat[i][j] -= mat[k][j] * m

            # filling lower triangular matrix with zeros
            mat[i][k] = 0
    for i in range(N):
        if not round(mat[i][i], 4):
            return N-1
    return -1

# function to calculate the values of the unknowns
def backward_substitution(mat):
    N = len(mat)
    x = np.zeros(N)  # An array to store solution

    # Start calculating from last equation up to the first
    for i in range(N - 1, -1, -1):

        x[i] = mat[i][N]

        # Initialize j to i+1 since matrix is upper triangular
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]

        x[i] = (x[i] / mat[i][i])

    return x

def linearInterpolation(table_points, point):
    flag = 1
    for i in range(len(table_points) - 1):
        if table_points[i][0] <= point <= table_points[i + 1][0]:
            x1, x2, y1, y2 = table_points[i][0], table_points[i + 1][0], table_points[i][1], table_points[i + 1][1]
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print("\nThe approximation (interpolation) of the point ", point, " is: ", round(result, 4))
            flag = 0
    if flag:
        if point > table_points[len(table_points) - 1][0]:
            x1 = table_points[len(table_points) - 1][0]
            x2 = table_points[len(table_points) - 2][0]
            y1 = table_points[len(table_points) - 1][1]
            y2 = table_points[len(table_points) - 2][1]
            m = (y1 - y2) / (x1 - x2)
            result = y1 + m * (point - x1)
        else:
            x1 = table_points[0][0]
            x2 = table_points[1][0]
            y1 = table_points[0][1]
            y2 = table_points[1][1]
            m = (y1 - y2) / (x1 - x2)
            result = y1 + m * (point - x1)
        print("\nThe approximation (extrapolation) of the point ", point, " is: ", round(result, 4))


def polynomialInterpolation(table_points, x):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points] # Makes the initial matrix
    b = [[point[1]] for point in table_points]
    for i in range(len(matrix)):
        matrix[i].append(b[i][0])

    matrixSol = gaussianElimination(matrix)

    result = sum([matrixSol[i] * (x ** i) for i in range(len(matrixSol))])
    print(f"\nThe Result of P(X={x}) is:", result)
    return result


def lagrange_interpolation(table_points, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    x_data = list(map(lambda point: point[0], table_points))
    y_data = list(map(lambda point: point[1], table_points))
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result


if __name__ == '__main__':
    table_points = [(-3.27, -2), (-1.52, 30.2), (4.2, 2.9093)]
    x = 0.2
    while True:
        choice = input("\nWhat interpolation you want?\n"
                       "1. Linear interpolation.\n"
                       "2. Polynomial interpolation.\n"
                       "3. Lagrange interpolation.\n"
                       "4. None of them, I want to exit.\n")
        if choice == "1":
            linearInterpolation(table_points, x)
        elif choice == "2":
            polynomialInterpolation(table_points, x)
        elif choice == "3":
            print("\nInterpolated value at x =", x, "is y =", round(lagrange_interpolation(table_points, x), 1))
        elif choice == "4":
            break
        else:
            print("\nInvalid input, please try again.")

