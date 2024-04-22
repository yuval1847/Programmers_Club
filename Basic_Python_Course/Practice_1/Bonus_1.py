def task1():
    # The function get nothing.
    # The function print all the prime numbers between 1 to 100.
    flag = False
    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0 and i != j:
                flag = True
                break
        if not flag:
            print(i)
        flag = False

def task2(str):
    # The function get a string.
    # The function return the string reversed.
    return str[::-1]

def task3(str):
    # The function get a string.
    # The function return True if the given string is a palindrom, otherwise False.
    return str == task2(str)

def task4(str):
    # The function get a string which represent a sentence.
    # The fucntion return the longest word in the sentence.
    longest_word = ""
    for i in str.split(' '):
        if len(i) > len(longest_word):
            longest_word = i
    return longest_word


task1()
print(task2("Hello, World!"))
print(task3("strrts"))
print(task4("Never gonna give you up"))