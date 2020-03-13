#Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.from collections import Counter

nums=list(map(int,input().split()))
dict=Counter(nums)
for i in nums:
    if(dict[i]==1):
        print(i)
   
#Input: [2,2,3,2]
#Output: 3

