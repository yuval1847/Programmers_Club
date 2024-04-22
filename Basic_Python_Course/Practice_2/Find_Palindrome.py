def find_palindrome(list1):
    # The function get a list of strings
    # The function return a new list of all the palindromes in the list
    newList = []
    for i in list1:
        if i == i[::-1]:
            newList.append(i)
    return newList

print(find_palindrome(['radar', "apple", "level", "banana", "stats", "noon"]))