table = ["-","-","-"
        "-","-","-"
        "-","-","-"]

win = None
def game():
    global win
    print("The game started")
    see_table()

    

    for i in range (5):
        print("Turn of X")
        value = "X"
        movement(value)
        winner()
        if win != "X" and 1 < 4:
            for j in range (3):
                print("Turn of O")
                value = "O"
                movement(value)
                winner()

                if win == "O":
                    print("Finish")
                break
        elif win == "X":
            print("Finish")
            break
        else:
            print("Finish")
            



def winner():
    global win 
    horizontal()
    vertical()
    diagonal()



def horizontal():
    global win
    if table[0]==table[1]==table[2] != "-":
        win = table[0]

    elif table[3]==table[4]==table[5] != "-":
        win = table[3]

    elif table[6]==table[7]==table[8] != "-":
        win = table[6]


def vertical():
    global win
    if table[0]==table[3]==table[6] != "-":
        win = table[0]

    elif table[1]==table[4]==table[7] != "-":
        win = table[1]

    elif table[2]==table[5]==table[8] != "-":
        win = table[2]




def diagonal():
    global win
    if table[0]==table[4]==table[8] != "-":
        win = table[0]

    elif table[2]==table[4]==table[6] != "-":
        win = table[2]


def movement(value):
    point = False


    while point == False:
        position = int(input("Choose a position from 1 to 9: "))
        position = -1

        if table[position] == "-":
            point = True

        else:
            print("You cannot choose that position")

    table[position] = value
    see_table()

def see_table():
    print(table[0] + "|" + table[1] + "|" + table[2] + "1|2|3")
    print(table[3] + "|" + table[4] + "|" + table[5] + "4|5|6")
    print(table[6] + "|" + table[7] + "|" + table[8] + "7|8|9")
print()

