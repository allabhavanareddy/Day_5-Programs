'''def palin(s):
    l=len(s)
    for i in s:
        if(i!=s[l-1]):
             return 0
        l=l-1
    return 1
s=input('enter the string:')
x=palin(s)
if x==1:
    print('palindrome')
else:
    print('not palindrome')
    
s=input()
i=0
j=len(s)-1
while(i<j):
     if s[i]!=s[j]:
         print('not palindrome')
         break
     i+=1
     j-=1
else:
    print('palindrome')'''
    
 
#using recurssion
def fun(s,i,j):
    if i>j:
        return True
    if s[i]!=s[j]:
        return False
    return fun(s,i+1,j-1)
s=input()
print(fun(s,0,len(s)-1))



    