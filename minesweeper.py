# This program is about the minesweeper.
# The function inputs height, length, a height x length field with the location of mines shown,
# and it outputs the field with numbers.
# eg. input: """*...                    output: """*100
#               ....                               2210
#               .*..                               1*10
#               ...."""                            1110"""
# Precondition: The input field contains only '-', '*' and the newline character.
# Time complexity: O(m, n) for m x n field

# find all the position of mines, add 1 to the surrounding positions
def Minesweeper_addingNumbers(height, length, field_string):
    if field_string == '': return ''
    if height == 1 and length == 1: return field_string

    # Convert field into 2-dimensioanl list containing numbers first
    field_list = []
    # Create a list that stores mines position
    mines_position = []
    for i in range(len(field_string.splitlines())):
        r = list(field_string.splitlines()[i])
        for j in range(len(r)):
            if r[j] == '.': r[j] = 0
            if r[j] == '*': mines_position.append([i, j])
        field_list.append(r)

    # Add one to every surrounding positions of each mines
    # Also checking on the boundary case
    for (i, j) in mines_position:
        if i != 0 and field_list[i-1][j] != '*': field_list[i-1][j] += 1
        if j != 0 and field_list[i][j-1] != '*': field_list[i][j-1] += 1
        if i != height - 1 and field_list[i+1][j] != '*': field_list[i+1][j] += 1
        if j != length - 1 and field_list[i][j+1] != '*': field_list[i][j+1] += 1
        if i != 0 and j != 0 and field_list[i-1][j-1] != '*': field_list[i-1][j-1] += 1
        if i != height - 1 and j != length - 1 and field_list[i+1][j+1] != '*': field_list[i+1][j+1] += 1
        if i != 0 and j != length - 1 and field_list[i-1][j+1] != '*': field_list[i-1][j+1] += 1
        if i != height - 1 and j != 0 and field_list[i+1][j-1] != '*': field_list[i+1][j-1] += 1

    # Change the numbers into string to join them
    for i in range(height):
        for j in range(length):
            if type(field_list[i][j]) == int:
                field_list[i][j] = str(field_list[i][j])

    # join all the positions to form a field string
    for i in range(len(field_list)):
        field_list[i] = ''.join(field_list[i])
    return '\n'.join(field_list)


print Minesweeper_addingNumbers(4, 4, '*...\n....\n.*..\n....')
print Minesweeper_addingNumbers(3, 5, '**...\n.....\n.*...')
