nums = [1,1,1,2,2,3,4,4,4,5,5]

count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1

min_num = 0
min_count = 1000

for x in count:
    if count[x] < min_count:
        min_count = count[x]
        min_num = x

print(min_num)

