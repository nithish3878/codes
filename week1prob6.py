from collections import Counter
nums=list(map(int,input().split()))
dict=Counter(nums)
for i in nums:
    if(dict[i]==1):
        print(i)
