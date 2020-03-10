#Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the result for the given queries.def bruteforcexor(arr,l,r):


def bruteforcexor(arr,l,r):
    res=0
    for i in range(l,r+1):
        res=res^arr[i]
    print(res)
    
def optimal(arr,l,r):
    if(l==0):
        print(l1[r])
    else:
        print(l1[r]^l1[l-1])
        
arr=list(map(int,input().split()))
for _ in range(int(input("ENTER NO OF QUERIES"))):
    l,r=map(int,input().split())
    l1=[arr[0]]
    for i in range(1,len(arr)):
        l1.append(arr[i]^l1[i-1])
    bruteforcexor(arr,l,r)
    optimal(arr,l,r)



#Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
#Output: [2,7,14,8] 
 




