#First unique number
#Return the first number that appears only once
nums= [1,2,3,3,4,2,5]
count = {}

for x in nums:
        count[x] = count.get(x+1) + 1

for x in nums:
    if count[x] == 1:
        print(x)
        break



