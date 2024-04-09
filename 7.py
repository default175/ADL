def fill_spiral(square, n, num, row, col, direction):
    if num > n * n:
        return
    square[row][col] = num

    if direction == "right":
        if col + 1 < n and square[row][col + 1] == 0:
            fill_spiral(square, n, num + 1, row, col + 1, direction)
        else:
            fill_spiral(square, n, num + 1, row + 1, col, "down")
    elif direction == "down":
        if row + 1 < n and square[row + 1][col] == 0:
            fill_spiral(square, n, num + 1, row + 1, col, direction)
        else:
            fill_spiral(square, n, num + 1, row, col - 1, "left")
    elif direction == "left":
        if col - 1 >= 0 and square[row][col - 1] == 0:
            fill_spiral(square, n, num + 1, row, col - 1, direction)
        else:
            fill_spiral(square, n, num + 1, row - 1, col, "up")
    elif direction == "up":
        if row - 1 >= 0 and square[row - 1][col] == 0:
            fill_spiral(square, n, num + 1, row - 1, col, direction)
        else:
            fill_spiral(square, n, num + 1, row, col + 1, "right")

def print_spiral(n):
    square = [[0] * n for _ in range(n)]
    fill_spiral(square, n, 1, 0, 0, "right")

    for row in square:
        print(" ".join(map(str, row)))

N = int(input())
print_spiral(N)
