def generate_sequences(n, k, current_sequence=[]):
    if len(current_sequence) == n:
        print(" ".join(map(str, current_sequence)))
    else:
        for i in range(1, k + 1):
            generate_sequences(n, k, current_sequence + [i])


n, k = map(int, input().split())

generate_sequences(n, k)
