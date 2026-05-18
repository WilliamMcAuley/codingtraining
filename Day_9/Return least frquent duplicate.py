nums = [1,1,1,2,2,3,3,3,4,4,4,4,5,5,5,5]

# print(1)
count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1
    # print(x)

min_num = float('inf')
discard = {}
# print(count)

for x in count:
    if count[x] < min_num:
        min_num = count[x]
        least_freq = x
        # print(min_num)
        #print("min_num",min_num)
    else:
        discard = x
print(least_freq,min_num)


