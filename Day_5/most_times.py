#Find the number that appears most times
nums = [1,2,2,3,3,4]

count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1
    if count[x] > max.count[x]:
        print(max(count[x]))

# for x in nums:
#     if x > max.count[x]:
#         print(x)
#         break