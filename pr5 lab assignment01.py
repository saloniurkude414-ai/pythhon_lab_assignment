# Lab Assignment 1

# Input integers and store in tuple
nums = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total number of items:", len(nums))

# b) Last item in the tuple
print("Last item:", nums[-1])

# c) Tuple in reverse order
print("Tuple in reverse order:", nums[::-1])

# d) Check for integers 5 and 0
if 5 in nums and 0 in nums:
    print("The tuple contains both 5 and 0")
else:
    print("The tuple does not contain both 5 and 0")

# e) Remove first and last items
if len(nums) > 2:
    new_tuple = nums[1:-1]
else:
    new_tuple = ()
print("Tuple after removing first and last items:", new_tuple)
