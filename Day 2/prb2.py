# #Most Frequent Number
# #[1,2,3,3,3,4]
#
# nums = [1,2,3,3,3,4]
# count = dict()
# freqlist = {}
# def mst_freq_num():
#     for x in nums:
#         if x in freqlist:
#             dict(count.add(x,+1))
#         else:
#             freqlist.add(x,+1)
#
# print(mst_freq_num())
#
#




#Return the most frequent number
nums = [1,2,3,3,4]

seen = {}


def freq_num():
    seen = {}
    count = ()
    for x in nums:
        count[x] = count.get(x,0) + 1
print(freq_num())