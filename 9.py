def generate_permutations(s, permutation=''):
    if len(s) == 0:
        print(permutation)
    else:
        for i in range(len(s)):
            generate_permutations(s[:i] + s[i+1:], permutation + s[i])

s = input()
generate_permutations(s)
