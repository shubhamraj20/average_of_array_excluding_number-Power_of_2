import math
# chechking_powert_of_two is a helper function which helps to check that number has power of 2.
def chechking_powert_of_two(n):
    return n > 0 and math.log2(n).is_integer()
# main function average_excluding_powers_of_two that takes an array of integers as input, going through each element of the array, and adds it to a running new_arr if it's not a power of two.
def average_after_removing_powerofTwo(arr):
    new_arr = 0
    count = 0
    for num in arr:
        if not chechking_powert_of_two(num):
            new_arr += num
            count += 1
    return int(new_arr / count if count > 0 else 0)
N=int(input())
arr=list(map(int, input().split()))
print(average_after_removing_powerofTwo(arr))

