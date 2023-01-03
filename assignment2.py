print("""<-----RULES----->
1. BRUSH DOWN
2. BRUSH UP
3. VEHICLE ROTATES RIGHT
4. VEHICLE ROTATES LEFT
5. MOVE UP TO X
6. JUMP 
7. REVERSE DIRECTION
8. VIEW THE MATRIX
0. EXIT
Please enter the commands with a plus sign (+) between them.""")

### INPUT ALMA
commands =input("Please enter the commands:").split("+")
first_input = [commands[0]]
del commands[0]
N = (int(first_input[0])+2)


### MATRIX OLUŞTURMA
matriks = []
for i in range(N):
    line = []
    for j in range(N):
        line.append(" ")
    matriks.append(line)
count = 0
while count < (N):
    matriks[0][count] = "+"
    matriks[N-1][count] = "+"
    matriks[count][0] = "+"
    matriks[count][N-1] = "+"
    count+=1



### ARABA BAŞLANGIÇ KONUMU
directions = ["right","down","left","up"]
direction = directions[0]
position=matriks[1][1]
brush_positions = ["up", "down"] # 0 = UP   1 = DOWN
brush_position = brush_positions[0]
map_size = int(first_input[0])
x=1
y=1

### BRUSH DOWN FONKSİYONU 1
def brush_position1():
    global brush_position
    if brush_position == brush_positions[0]:
        brush_position = brush_positions[1]
        return brush_position
    if brush_position == brush_positions[1]:
        brush_position = brush_positions[1]
        return brush_position


### BRUSH UP FONKSİYONU 2
def brush_position2():
    global brush_position
    if brush_position == brush_positions[0]:
        brush_position = brush_positions[0]
        return brush_position
    if brush_position == brush_positions[1]:
        brush_position = brush_positions[0]
        return brush_position

### DIRECTION RIGHT FONKSİYONU 3
def change_direction_3():
    global direction
    if direction == directions[0]:
        direction = directions[1]
        return direction
    if direction == directions[1]:
        direction = directions[2]
        return direction
    if direction == directions[1]:
        direction = directions[2]
        return direction
    if direction == directions[2]:
        direction = directions[3]
        return direction



### DIRECTION LEFT FONKSİYONU 4
def change_direction_4():
    global direction
    if direction == directions[0]:
        direction = directions[3]
        return direction
    if direction == directions[3]:
        direction = directions[2]
        return direction
    if direction == directions[2]:
        direction = directions[1]
        return direction
    if direction == directions[1]:
        direction = directions[0]
        return direction

### JUMP FONKSİYONU 6
def jump():
    global position
    global x
    global y
    global map_size
    global brush_position
    if direction == directions[0]:
        position = matriks[x][y+3]
        y = y+3
        if y == int(map_size)-2:
            y = 1
        if y == int(map_size)-1:
            y = 2
        if y == int(map_size):
            y = 3
        brush_position = brush_positions[0]
  

    if direction == directions[1]:
        position = matriks[x+3][y]
        x = x+3
        if x == int(map_size) - 2:
            x = 1
        if x == int(map_size) - 1:
            x = 2
        if x == int(map_size):
            x = 3
        brush_position = brush_positions[0]
     

    if direction == directions[2]:
        position = matriks [x][y-3]
        y = y-3
        if y == 3:
            y = int(map_size)
        if y == 2:
            y = int(map_size)-1
        if y == 1:
            y = int(map_size)-2
        brush_position = brush_positions[0]
      

    if direction == directions[3]:
        position = matriks[x-3][y]
        return position
        x = x-3
        if x == 3:
            x = int(map_size)
        if x == 2:
            x = int(map_size) - 1
        if x == 1:
            x = int(map_size) - 2
        brush_position = brush_positions[0]

### REVERSE FONKSİYONU 7
def reverse():
    global direction
    if direction == directions[0]:
        direction = directions[2]
        return direction
    if direction == directions[1]:
        direction = directions[3]
        return direction
    if direction == directions[2]:
        direction = directions[0]
        return direction
    if direction == directions[3]:
        direction = directions[1]
        return direction

### WRONG INPUT
def wrong_input():
    print("Please enter inputs between 0 and 8")
    commands = input("Please enter the commands:").split("+")



### INPUT ALMA
try:
    for c in commands:
        if c == "1": brush_position1()
        elif c == "2": brush_position2()
        elif c == "3": change_direction_3()
        elif c == "4": change_direction_4()
        elif c.startswith("5_"):
            if direction == directions[0]:
                for g in range(int(c[2:])):
                    if brush_position == brush_positions[0]:
                        matriks[x][y] = ""
                    if brush_position == brush_positions[1]:
                        matriks[x][y] = "*"
                    position = matriks[x][y+1]
                    x = (x)
                    y = y+1
                    while y > map_size:
                        y = 1
                    if brush_position == brush_positions[0]:
                        matriks[x][y] = ""
                    if brush_position == brush_positions[1]:
                        matriks[x][y] = "*"


            if direction == directions[1]:
                for g in range(int(c[2:])):
                    if brush_position == brush_positions[0]:
                        matriks[x][y] = ""
                    if brush_position == brush_positions[1]:
                        matriks[x][y] = "*"
                    position = matriks[x+1][y]
                    x = (x+1)
                    y = y
                    while x > map_size:
                        x = 1
                    if brush_position == brush_positions[0]:
                        matriks[x][y] = ""
                    if brush_position == brush_positions[1]:
                        matriks[x][y] = "*"

            if direction == directions[2]:
                for g in range(int(c[2:])):
                    if brush_position == brush_positions[0]:
                        matriks[x][y] = ""
                    if brush_position == brush_positions[1]:
                        matriks[x][y] = "*"
                    position = matriks[x][y-1]
                    x = x
                    y = (y-1)
                    while y < 1:
                        y = int(map_size)
                    if brush_position == brush_positions[0]:
                        matriks[x][y] = ""
                    if brush_position == brush_positions[1]:
                        matriks[x][y] = "*"

            if direction == directions[3]:
                for g in range(int(c[2:])):
                    if brush_position == brush_positions[0]:
                        matriks[x][y] = ""
                    if brush_position == brush_positions[1]:
                        matriks[x][y] = "*"
                    position = matriks[x-1][y]
                    x = (x-1)
                    y = y
                    while x < 1:
                        x = int(map_size)
                    if brush_position == brush_positions[0]:
                        matriks[x][y] = ""
                    if brush_position == brush_positions[1]:
                        matriks[x][y] = "*"
        elif c == "6": jump()
        elif c == "7": reverse()
        elif c == "8":
            for i in range(N):
                count = "".join(matriks[i])
                print(count)
        elif c =="0": break
        else: wrong_input()
except: wrong_input()
