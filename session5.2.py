#Linear Search

instagramUserName = ["mo", "ans", "ro", "sh", "an"]
names = ["mohit", "anshit", "rohit", "shivam", "anish"]
userName = input("ENTER USERNAME TO SEARCH:")


"""
index = 0
#below approach is wrong

if userName == instagramUserName[index]:
    print("NAME IS:", names[index])
    
elif userName == instagramUserName[index+1]:
    print("NAME IS:", names[index+1])

else:
    print("CANNOT FIND USER:")
"""

"""
#while loop
index = 0

while index < len(instagramUserName):
    print("check", userName, "with", instagramUserName[index])

    if userName == instagramUserName[index]:
        print("NAME IS : ", names[index])
        break

    index += 1

"""


Flag = False
for index in range(0, len(instagramUserName)): #index will start ffrom 0 and go till 
    #print("check", userName, "with", instagramUserName[index])

    if userName == instagramUserName[index]:
        print("NAME IS : ", names[index])
        Flag = True
        break


if Flag == False:
    print(userName, "username Not found")
