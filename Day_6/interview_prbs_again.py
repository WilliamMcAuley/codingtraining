#Find all the duplicates
nums = [1,2,3,2,4,3,5]

count = {}

for x in nums:
    count[x] = count.get(x, 0) + 1

for x in count:
    if count[x] > 1:
        print(x)
