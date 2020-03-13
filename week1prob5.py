#Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

l=[]
n=int(input())
print('[',end='')
for i in range(n):
    print(bin(i)[2:].count('1'),end=',')
print(bin(i+1)[2:].count('1'),end=']')

#Input: 2
#Output: [0,1,1]

    
