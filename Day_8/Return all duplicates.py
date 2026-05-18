nums = [1,2,2,3,4,4,5]

count = {}

for x in nums:
    count[x] = count.get(x, 0) + 1
print(count)
dup = []
for x in count:
    if count[x] > 1:
        dup.append(x)
print(dup)


