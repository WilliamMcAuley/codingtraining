nums = [1,2,2,3,4,4,5]

count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1
print(count)

unique = []
for x in count:
    if count[x] == 1:
        unique.append(x)
print(unique)
# seen =()
# for x in count():
#     if count.get(x,0) count[x]