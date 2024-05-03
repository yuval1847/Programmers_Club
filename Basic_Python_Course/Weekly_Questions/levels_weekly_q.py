def HowManyOptions(n):
    # The function get a number of levels.
    # The function return the amount of possibilities to reach the n levels by
    # get up only 1 or 2 levels in a time.
    if n < 0:
        return 0
    if 0 <= n <= 1:
        return 1
    return HowManyOptions(n-2) + HowManyOptions(n-1)

n = int(input("Enter amount of levels: "))
print(f"There are {HowManyOptions(n)} options to get up on {n} levels.")