nums = [2,2,1,1,2,0,4]
seen = {}

for x in nums:
    seen[x] = seen.get(x, 0) + 1
    # print(seen)

for x in nums:
    if seen[x] == 1:
        print(x)
        break

