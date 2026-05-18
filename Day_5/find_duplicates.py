nums = [1,2,2,3,4,4,5]

count = {}
dup = {}
for x in nums:
    count[x] = count.get(x, 0) + 1
    # print(count[x])
    if count[x] > 1:
        print(x)
        # print(count)

# for x in nums:
#     if count[x] =>
#     print()