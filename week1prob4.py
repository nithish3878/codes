def recursiveApproach(n):
    if(n==1):
        return 0
    elif(n%2==0):
        return recursiveApproach(n//2)+1
    else:
        return min(recursiveApproach(n-1),recursiveApproach(n+1))+1
        
        
def optimal(n):
  c=0
  while(n>1):
      if(n==3):
          c+=3
          n=1
      elif(n%2==0):
          n=n//2
          c+=1
      else:
          if(((n-1)//2)%2==0):
              c+=1
              n-=1
          else:
              c+=1
              n+=1
  return c
 
n=int(input())
print(recursiveApproach(n))
print(optimal(n))


