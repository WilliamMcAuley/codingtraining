#First unique number
#Return the first number that appears only once
nums= (1,2,3,3,4,2,5)

count = {}

for x in nums:
    # print(x)
    count[x] = count.get(x, 0) + 1
    # print(x)
    # print(count)

for x in nums:
    if count[x] == 1:
        print(x)
        break
#List [1,2,3] ordered collection
#Set {1,2,3} unique values only
#Dict {'a',':1'} key -> value mapping
#Tulpe (1,2,3) fixed immutable data
