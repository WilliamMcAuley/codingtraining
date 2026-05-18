nums = [1,2,2,3,3,4]

count = {}

for x in nums:
    count[x] = count.get(x, 0) + 1
print(count)