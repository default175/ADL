def reverse(n):
    if n == 0:
        return
    else:
        num = int(input())
        reverse(n - 1)
        print(num, end=' ')


N = int(input())
reverse(N)
