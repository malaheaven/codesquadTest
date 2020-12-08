cube_slice = [['R', 'R', 'W'],
              ['G','C','W'],
              ['G','B','B']]

for x,y,z in cube_slice:
    print(x,y,z)

def check_inputstr(input_word):
    input_word_list = list()
    for i in range(0, len(input_word)):
        if i != len(input_word)-1 and input_word[i+1] == "'":
            input_word_list.append(input_word[i] + input_word[i+1])
        elif input_word[i] != "'":
            input_word_list.append(input_word[i])
    return input_word_list


def action_cube(action,cube_slice):
    if action == "U":
        value1 = cube_slice[0][0]
        value2 = cube_slice[0][1]
        value3 = cube_slice[0][2]

        cube_slice[0][0] = value2
        cube_slice[0][1] = value3
        cube_slice[0][2] = value1

    elif action == "U'":
        value1 = cube_slice[0][0]
        value2 = cube_slice[0][1]
        value3 = cube_slice[0][2]

        cube_slice[0][0] = value3
        cube_slice[0][1] = value1
        cube_slice[0][2] = value2

    elif action == "R":
        value1 = cube_slice[0][2]
        value2 = cube_slice[1][2]
        value3 = cube_slice[2][2]

        cube_slice[0][2] = value2
        cube_slice[1][2] = value3
        cube_slice[2][2] = value1


    elif action == "R'":
        value1 = cube_slice[0][2]
        value2 = cube_slice[1][2]
        value3 = cube_slice[2][2]

        cube_slice[0][2] = value3
        cube_slice[1][2] = value1
        cube_slice[2][2] = value2

    elif action == "L":
        value1 = cube_slice[0][0]
        value2 = cube_slice[1][0]
        value3 = cube_slice[2][0]

        cube_slice[0][0] = value3
        cube_slice[1][0] = value1
        cube_slice[2][0] = value2

    elif action == "L'":
        value1 = cube_slice[0][0]
        value2 = cube_slice[1][0]
        value3 = cube_slice[2][0]

        cube_slice[0][0] = value2
        cube_slice[1][0] = value3
        cube_slice[2][0] = value1

    elif action == "B":
        value1 = cube_slice[2][0]
        value2 = cube_slice[2][1]
        value3 = cube_slice[2][2]

        cube_slice[2][0] = value3
        cube_slice[2][1] = value1
        cube_slice[2][2] = value2

    elif action == "B'":
        value1 = cube_slice[2][0]
        value2 = cube_slice[2][1]
        value3 = cube_slice[2][2]

        cube_slice[2][0] = value2
        cube_slice[2][1] = value3
        cube_slice[2][2] = value1

    return cube_slice

while True:
    input_word = str(input("CUBE > "))

    input_word_list = check_inputstr(input_word)

    if input_word == "Q":
        print("Bye~")
        break
    else:
        for action in input_word_list:
            print(action)
            if action in ["U","U'","R","R'","L","L'","B","B'"]:
                for x, y, z in action_cube(action,cube_slice):
                    print(x, y, z)
            else:
                print("없는 동작입니다.")









