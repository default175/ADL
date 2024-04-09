def sumpower(n,b,i=0,sum=0):
    if i<=n:
        sum+=b**i
        return sumpower(n,b,i+1,sum)
    else:
        return sum

b=int(input("b"))
n=int(input("n"))
print(sumpower(n,b))