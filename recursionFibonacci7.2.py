def fibonacci(nums):
    if nums == 0:
        return 0
    
    elif nums == 1:
        return 1
    
    else: 
        return fibonacci(nums - 1) + fibonacci(nums - 2)

number = 3
result =  fibonacci(number)
print("fibonacci series is :", result)
