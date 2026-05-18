#Return duplicates like [2,3]
nums = [1,2,3,2,4,3,5]
#need to use a function and add the return function at the end
count = {}
duplicates = []
def count_duplicates():
    for x in nums:
        count[x] = count.get(x, 0) + 1
        if count[x] > 1:
            duplicates.append(x)
    return duplicates
print(count_duplicates())
