def find_longest_word(list1):
    # The function get a list of strings
    # The function return the longest word/words in the list
    longestWordList = [""]
    for i in list1:
        if len(i) == len(longestWordList[0]):
            longestWordList.append(i)
        elif len(i) > len(longestWordList[0]):
            longestWordList = [i]
    return longestWordList

print(find_longest_word(["apple", "banana", "orange", "strawberry", "kiwi", "pineapple"]))