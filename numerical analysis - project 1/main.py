# Eve Hackmon , 209295914
# Daniel Houri , 209445071
# Yakov Shtefan , 208060111
# Vladislav Rabinovich , 323602383
# git : https://github.com/EveHackmon/Numerical-Analysis---Assignment-1.git


# This program accepts two square matrices from the user, prints them and calculates their addition and their multiplication.

def print_matrix(mat): # This function accepts a matrix and prints it in an orderly fashion
    for row in mat:
        print(" ",row, "\n")

def add_matrix(mat1, mat2): # This function accepts two matrices and returns the result of their addition
    if len(mat1) != len(mat2):
        raise ValueError(" mat1 and mat2 must have the same size")
    new_matrix = [] # Create a new list
    for i in range(len(mat1)):
        row = [] # Create an list in each cell in the "new_matrix" list
        for j in range(len(mat1)): # Loop through each element of both matrices
            value = (mat1[i][j] + mat2[i][j]) # Calculates the result of the addition of the two elements in the same position in both matrices
            row.append(value) # Saves the value in the correct order in the row
        new_matrix.append(row) # Saves the row in the correct order in the "New matrix" list
    return new_matrix # Returns the result of the addition of the matrices

def bulid_matrix(row_size, col_size): # This function accepts the size of a matrix, accepts the matrix from the user, and returns the matrix
    matrix = [] # Create a new list
    for i in range(row_size): # The loop runs as the number of rows received
        row = [] # Create an list in each cell in the "matrix" list
        for j in range(col_size): # The loop runs as the number of col received
            value = float(input()) # get a float
            row.append(value) # Saves the value in the correct order in the row
        matrix.append(row) # Saves the row in the correct order in the "matrix" list
    return matrix # Returns the matrix

def mull_matrix(mat1, mat2): # This function accepts two matrices and returns the result of their multiplication (mat1 * mat2)
    if len(mat1) != len(mat2):
        raise ValueError(" mat1 and mat2 must have the same size")
    new_matrix = [] # Create a new list
    value = 0
    for k in range(len(mat1)): # This loop is designed to count the row number in the left matrix that I am multiplying
        row = [] # Create a list in each cell in the "new matrix" list
        for i in range(len(mat1)): # This loop is designed to count the columns in a matrix that is multiplied from the right side
            for j in range(len(mat1)): # This loop is designed to count the columns in the matrix that is multiplied from the left side, and also the number of rows in the matrix that is multiplied from the right side
                value += float(mat1[k][j] * mat2[j][i]) # Calculates the sum of the products of each term in the left matrix row by each term in the right matrix column
            row.append(value)  # Saves the value in the correct order in the row
            value = 0 # Reset value
        new_matrix.append(row) # Saves the row in the correct order in the "new matrix" list
    return new_matrix # Returns the result of the multiplication of the matrices

if __name__ == '__main__':
    mat_size = int(input(" Please enter the matrices size ")) # get from user a square matrix size
    print(" enter the values for each matrix row after row \n matrix 1:")
    mat1 = bulid_matrix(mat_size, mat_size) # In this line I receive values from the user and create a square matrix1
    print(" matrix 2: ")
    mat2 = bulid_matrix(mat_size, mat_size) # In this line I receive values from the user and create a square matrix2
    print(" matrix 1 : ")
    print_matrix(mat1) # Print matrix1
    print(" matrix 2 : ")
    print_matrix(mat2) # Print matrix1
    print(" matrix 1 + matrix 2 = ")
    print_matrix(add_matrix(mat1, mat2)) # Prints the result of the addition of the two matrices
    print(" matrix 1 * matrix 2 = ")
    print_matrix(mull_matrix(mat1, mat2)) # Prints the result of the multiplication of the two matrices










