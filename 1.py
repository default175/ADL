#1
def sumsquare(n,count=0, i=1):
    if i<=n:
        count+=i*i
        return sumsquare(n, count, i+1 )
    else:
        return count

a=int(input())
print(sumsquare(a))


