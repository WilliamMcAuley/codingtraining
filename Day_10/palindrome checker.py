word = "racecar"
word2 = "python"
print("Type word to see if it is a palindrome:")
tryword = input("")

reverse_word = ""


for x in tryword:
    reverse_word = x + reverse_word
    # print(reverse_word)

if reverse_word == tryword:
    print(tryword,"is a palindrome approved word:")
else:
    print(tryword, "is not a palindrome word")



