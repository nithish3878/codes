#Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).


a,b,c=map(int,input().split())
a,b,c=bin(a)[2:],bin(b)[2:],bin(c)[2:]
k=max(len(a),len(b),len(c))
a=a.zfill(k)
b=b.zfill(k)
c=c.zfill(k)
cnt=0
for i in range(k):
    if(a[i]=='1' and b[i]=='1' and c[i]=='0'):
        cnt+=2
    elif(a[i]=='0' and b[i]=='1' and c[i]=='0'):
        cnt+=1
    elif(a[i]=='1' and b[i]=='0' and c[i]=='0'):
        cnt+=1
    elif(a[i]=='0' and b[i]=='0' and c[i]=='1'):
        cnt+=1
print(cnt)
  
  
#Input: a = 2, b = 6, c = 5
#Output: 3

