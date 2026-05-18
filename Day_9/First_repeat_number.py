nums = [1,2,3,4,4,4,5]

count = {}

for x in nums:
    count[x] = count.get(x, 0) + 1

seen = []
for x in count:
    if count[x] > 1:
        print("first repeat",x)
        break
    else:
        print("not a repeat",x,count[x])
    #

