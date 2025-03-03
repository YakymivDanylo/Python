import random

n = 10
m = 15

matrix = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]

for row in matrix:
    print(row)

num_row = int(input("Enter the number of the row:"))


def findSumFreePlaces(number_row):
    free_places = 0
    for j in range(len(matrix[number_row-1])):
        if matrix[number_row - 1][j] == 0:
            free_places += 1
    return free_places


print("Number of free places in row", num_row, "is:", findSumFreePlaces(num_row))
