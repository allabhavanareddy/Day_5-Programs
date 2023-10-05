n=int(input())
def fun(n):
    if(n==0 or n==1):
       return 1
    else:
        return n*fun(n-1)
   
r=fun(n)
print(r)