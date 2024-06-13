"""
another brick in wall
who placed the last brick and how many

Mr. john -> requirement  /  create a wall with 13 bricks
           
                 bricks
jack : 1         1
joe : 2          3

jack : 2        5
joe : 4         9

jack : 3      12
joe : 6       13

joe -> last brick
       1 brick
"""

john = []
joe =[]

def maxBricks(data):
    total = 0

    for i in range(0, len(data)):
        total = sum(data)
    print(total)

numberOfBricks = int(input("Enter the number of bricks: "))
johnFlag = False
joeFlag = False


for index in range(1, numberOfBricks + 1):
    if index <= numberOfBricks:
        john.append(index)
        numberOfBricks -= index
        if index <= numberOfBricks:
            joe.append(index*2)
            numberOfBricks -= (index*2)
     
        else:
            index = numberOfBricks
            joe.append(index)
            numberOfBricks -= index
            joeFlag = True

    else:
        if numberOfBricks != 0:
            index = numberOfBricks
            john.append(index)
            numberOfBricks -= index
            johnFlag = True

print("john bricks: ", john)
print("joe bricks: ", joe)

print("\njohn max brick:")
maxBricks(john)

print("joe max brick:")
maxBricks(joe)

if johnFlag == True:
    print("\nthe last brick is placed by john:")
    print("He placed : ",john[-1],"bricks in the last\n" )


if joeFlag == True:
    print("\nthe last brick is placed by joe:")
    print("He placed : ",joe[-1],"bricks in the last \n" )
