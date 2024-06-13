def square(nums):
    print(" 1. number is:", nums, id(nums))

    for i in range(0, len(nums)):
        nums[i] = nums[i] * nums[i]

    print(" 2. num is :", nums, id(nums))

numbers = [10, 20, 30, 40, 50]
print("A. number is :", numbers,  id(numbers))
square(numbers)
print("B. number is :", numbers, id(numbers))
