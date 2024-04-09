def summ(arr, n, sum=0, i=0):
    if arr[i]>0 and i<n:
        sum+=arr[i]
        return summ(arr, n, sum, i+1)
    else:
        return sum

arr=[1,2,3,4,7]
n=int(input())
print(summ(arr, n))