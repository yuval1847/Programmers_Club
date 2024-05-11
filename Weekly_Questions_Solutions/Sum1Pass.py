def Sum1Pass(lst, s, i=0):
    # The function gets a sorted list of integers(from the smallest to the biggest) and additional integer.
    # The function returns true if there are 2 values in the list which their sum is equals s.
    if len(lst) == 1 or i == len(lst):
        return False
    if s - lst[i] in lst[i+1:]:
        return True
    else:
        return Sum1Pass(lst, s, i + 1)
    
print(Sum1Pass([1, 2, 3, 5], 7))