def sum_of_arr(arr, n, i=0, sum=0):
    if i < n:
        sum += arr[i]
        return sum_of_arr(arr, n, i+1, sum)
    else:
        return sum

arr = [1, 2, 3, 4, 5]
n = int(input())
print(sum_of_arr(arr, n))
