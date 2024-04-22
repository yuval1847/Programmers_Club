# Q-1
def Q_1(list1):
    # The function get a list of integers
    # The function return the largest number in the list
    return max(list1)

print(Q_1([3, 5, 2, 8, 1, 9 ,4]))

# Q-2
def Q_2(list2):
    # The function get a list of integers
    # The function return a new list which contain only the even numbers from the given list
    newList = []
    for i in list2:
        if i % 2 == 0:
            newList.append(i)
    return newList

print(Q_2([1, 4, 5, 7, 8, 10, 13]))

# Q-3
def Q_3(list3):
    # The function get a list of integers
    # The function return True if the list is ordered in increasing order
    for i in range(len(list3)-1):
        if list3[i] > list3[i+1]:
            return False
    return True

print(Q_3([1, 2, 3, 4, 5]))

# Q-4
def Q_4(str):
    # The function get a string
    # The function return the string reversed
    return str[::-1]

print(Q_4("Hello, World!"))

# Q-5
def Q_5(str):
    # The function get a string
    # The funcrion return the amount of vowels in the given string
    count = 0
    for i in str:
        if i in "AEIOU" or i in "aeiou":
            count += 1
    return count

print(Q_5("Hello, how are you?"))