# bitwise operator
# &, |, ^

num1 = 10
num2 = 8

print("num1 in binary is : ", bin(num1))
print("num1 in binary is : ", bin(num2))

result1 = num1 & num2 # 1 0 0 0 -> 8
result2 = num1 | num2 # 1 0 1 0 -> 10
result3 = num1 ^ num2 # 0 0 1 0 -> 2

print("result 1 is :", result1)
print("result 2 is :", result2)
print("result 3 is :", result3)

# Shift operators
# >>, << 

num1 = 8
num2 = 3
#      8 >> 3 , 8 / 2 ^ 3
result1 = num1 >> num2
print("result 1 right shift is : ", result1)


number = result1 << num2
print("number :", number)

#      8 << 3 , 8 * 2 ^ 3
result2 = num1 << num2
print("result 1 left shift is : ", result2)

number = -11 # 1 0 1 1
result = number >> 2

print(number, ">> 2 is :", result)

# 13 -> 1 1 0 1
# >> 2
# 13 // 2 power 2
# 0 0 0 0  1 1 0 1 
# _ _ 0 0  0 0  1 1 -> 3

# -11
# 0 0 0 0  1 0 1 1
# 1 1 1 1  0 1 0 0 (1's complement)
#                1
# 1 1 1 1  0 1 0 1 (2's complement)
# >> 2
# _ _ 1 1  1 1 0 1 (right shift)
# 1 1 1 1  1 1 0 1 ( because -)
# now again 2's complemwnt
# 0 0 0 0  0 0 1 1 -> -3


#-13
#0 0 0 0 1 1 0 1
# 1 1 1 1 0 0 1 0 
# 1 1 1 1 0 0 1 1
#>> 2
#_ _ 1 1  1 1 0 0 
# 1 1 1 1 1 1 0 0 
# 0 0 0 0 0 0 1 1 
# 0 0 0 0 0 1 0 0 -> -4 right shift answer 
