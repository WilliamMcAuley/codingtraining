nums = [1,2,2,3,4,4,4,5]

count = {}

for x in nums:
    count[x] = count.get(x,0) + 1

most_freq = []
max_num = 0
max_count = 0
for x in count:
    if count[x] > max_count:
        max_count = count[x]
        max_num = x
# print(max_count)
print(max_num)
