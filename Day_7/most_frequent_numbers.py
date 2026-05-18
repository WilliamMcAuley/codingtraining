nums = [1,2,2,5,5,5,5,6,8,9]
def most_frequent():
    count = {}
    for x in nums:
        # print(x)
        count[x] = count.get(x, 0) + 1
        print(count)

    max_num = None
    max_count = 0

    for x in count:
        if count[x] > max_count:
            max_count = count[x]
            max_num = x
    return max_num

        # if x > count.get(x):
        #     print(x)
        #     # break
        # return count

print(most_frequent())
# list = []
# for x in most_frequent():
#     if x > most_frequent()
#         get