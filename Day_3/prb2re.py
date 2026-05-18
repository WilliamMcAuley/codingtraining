# #Most Frequent Number
nums = [1,2,3,3,3,4]
def most_freq_num():
    count = {}
    for x in nums:
        count[x] = count.get(x,0) + 1
    return count



# print(most_freq_num())
count = most_freq_num()

max_num = None
max_count = 0

for x in count:
    if count[x] > max_count:
        max_count = count[x]
        max_num = x
print(max_num)