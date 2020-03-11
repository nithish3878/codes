def bruteforce(l):
  maxi=0
  for i in range(len(l)):
      for j in range(i+1,len(l)):
          if((l[i]^l[j])>maxi):
              maxi=l[i]^l[j]
  return maxi
l=list(map(int,input().split()))
print(bruteforce(l))

        
