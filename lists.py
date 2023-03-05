#TODO: make a matrix addition calculator:
import os
matrix = []
column = []
# print("Enter matrix dimentions: ")

def matrixConstructor(rows, columns):
    matrix = []
    column = []
    for i in range(0,rows):
        for j in range(0,columns):
            column.append(0)
        matrix.append(column)
        column = []
    # print(f"final matrix: {matrix}")
    return matrix

def matrixLoader(rows,columns):
    matrix = matrixConstructor(rows, columns)
    for i in range(0, rows):
        for j in range(0, columns):
            element = int(input(f"P(i={i};j={j}) Enter value: "))
            matrix[i][j] = element
            os.system("clear")
    return matrix

def MatrixAddition(rows, columns, matrixA, matrixB):
    matrixSum = matrixConstructor(rows, columns)
    for i in range(0, rows):
        for j in range(0, columns):
            element = matrixA[i][j] + matrixB[i][j]
            matrixSum[i][j] = element
    return matrixSum

columns = int(input("Enter number of columns: "))
rows = int(input("Enter number of rows: "))
# for i in range(0,rows):
#     for j in range(0,columns):
#         column.append(0)
#     matrix.append(column)
#     column = []
# print(f"final matrix: {matrix}")
#
# for i in range(0, rows):
#     for j in range(0, columns):
#         element = int(input(f"P(i={i};j={j}) Enter value: "))
#         matrix[i][j] = element
#         # os.system("clear")
#

matrix = matrixLoader(rows, columns)
matrix2 = matrixLoader(rows, columns)  

matrixSum = MatrixAddition(rows, columns, matrix, matrix2)
print(matrix)
print(matrix2)
print(f"Addition: {matrixSum}")
# printableMatrix = ""
# for i in range(0, rows):
#     printableMatrix += "|"
#     for j in range(0, columns):
#         printableMatrix += f" {str(matrix[i][j])} "
#     printableMatrix += " |\n"
#
# print(printableMatrix)

