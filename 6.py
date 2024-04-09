def reverse_sequence(n):
    if n == 0:
        return
    else:
        string = input()
        reverse_sequence(n - 1)
        print(string[::-1])


N = int(input())
reverse_sequence(N)
