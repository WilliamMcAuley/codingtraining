#Return True if duplicate exists
#[1,2,3,4,5] -> False
#[1,2,3,3] -> True

nums = [1,2,3,4,4,5]
seen = set()

def return_tf():
    for x in nums:
        if x in seen:
            return True
        else:
            seen.add(x)
    return False
print(return_tf())







