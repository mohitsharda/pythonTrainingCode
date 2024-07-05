def add(num1, num2):
    sum = num1 + num2 
    return sum

compute = add

def compute(num1, num2):
    return num1 + num2 * 2

square = compute

result1 = square(num1 = 10, num2 = 2)
print(result1)

result1 = add(num1 = 10, num2 = 2)
print(result1)
