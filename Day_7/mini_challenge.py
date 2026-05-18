nums = [3,3,3,2,2,1]
#return the number that appears the most
def appears_the_most():
    count = {}
    for x in nums:
        count[x] = count.get(x, 0) + 1

    max_num = 0
    max_count = 0

    for x in count:
        if count[x] > max_count:
            max_count = count[x]
            max_num = x
        return (max_count,max_num)
print(appears_the_most())
