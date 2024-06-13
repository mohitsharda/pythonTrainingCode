# Nested loops

# for i in range(0, 3): #0, 1, 2
#     print("i is :", i)

#     for j in range(0, 5): #0, 1, 2, 3, 4
#         print(j, end=" - ")
    
#     print()

blackSquar = "\u25A1"
whiteSquare  = "\u25A0"
king = "\u2654"
queen = "\u2655"
knight = "\u2658"
whiteBishop = "\u2657"
blackBishop = "\u265D"
elephant = "\u2656"
whitePawn = "\u2659"



for i in range(0, 8):
    # print(i%2, end=" ")  #if we divide by 2 anything we will get 0 or 1

    for j in range(0, 8):
        if i == 0 and j == 3 :
            print(king, end=" ")
        elif i == 0 and j == 4:
            print(queen, end=" ")
        elif i == 0 and j == 1:
            print(knight, end=" ")
        elif i == 0 and j == 6:
            print(knight, end=" ")
        elif i == 0 and j == 0:
            print(elephant, end=" ")
        elif i == 0 and j == 7:
            print(elephant, end=" ")
        elif i == 0 and j == 2:
            print(whiteBishop, end=" ")
        elif i == 0 and j == 5:
            print(whiteBishop, end=" ")
        elif i == 1 and j in (0,1,2,3,4,5,6,7):
            print(whitePawn, end=" ")
        else:
            if i % 2 == 0:  
                if j%2 == 0:
                    print(whiteSquare, end=" ") #j%2 -> white square
                else:
                    print(blackSquar, end=" ")
                    
            else:
                if (j+1)%2 == 0:
                    print(whiteSquare, end=" ") #(j+1)%2 -> black square
                else:
                    print(blackSquar, end=" ")
        
    print()


# HW :  place king and queen on their right position 
# place knights 