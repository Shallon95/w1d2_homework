# For the following list of numbers:

numbers = [1, 6, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_nums = []

for num in numbers:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        pass
print(even_nums)



# 2. Print the difference between the largest and smallest value:

largest_num = max(numbers)
smallest_num = min(numbers)
print(largest_num)
print(smallest_num)

diff_in_num = largest_num - smallest_num
print(diff_in_num)


# 3. Print True if the list contains a 2 next to a 2 somewhere.

answer = 0

for num in numbers:
    if num == answer:
        print(True)
    elif num != answer:
        answer = num
    else:
        print(False)




# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

list_total = 0
list_number = 0

for num in numbers:
    list_number = num
    if num == 6:
        pass
    else:
        list_total += num

print(list_total)



# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







