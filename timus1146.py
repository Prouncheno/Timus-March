from sys import stdin

n = int(stdin.readline())
matrix = n * [ n * [] ]
max_sum = 0

for i in range(n):
    matrix[i] = map(int, stdin.readline().split())
# matrix = deepcopy(input_matrix)
for start_y in range( n):
    for i in range(n):
        if start_y == 0:
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
        else:
            for j in range(start_y, n):
                matrix[i][j] -= matrix[i][start_y-1]
    
    for y in range(start_y-1, n):
        this_sum = 0
        for x in range(n):
            this_sum += matrix[x][y]
            if this_sum > max_sum:
                max_sum = this_sum
            elif this_sum < 0:
                this_sum = 0

if max_sum <= 0:
    max_sum = matrix[0][0]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > max_sum:
                max_sum = matrix[i][j]

print max_sum
