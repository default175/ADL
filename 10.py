def is_power_of_two(n):
    if n <= 0:
        return False
    elif n == 1:
        return True
    elif n % 2 == 0:
        return is_power_of_two(n // 2)
    else:
        return False

def main():
    n = int(input())
    for i in range(n + 1):
        print(f"{i} is {'a' if is_power_of_two(i) else 'not a'} power of two")

if __name__ == "__main__":
    main()
