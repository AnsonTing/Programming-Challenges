# This program displays numbers in large LCD screen.
# The input contains size and numbers, where numbers are to be displayed and size is the size of the display.
# The numbers are constructed using | and - characters.
# eg. input s = 2, n = 12345
#     output = """      --  --        --
#                    |    |   | |  | |
#                    |    |   | |  | |
#                       --  --   --   --
#                    | |      |    |    |
#                    | |      |    |    |
#                       --  --        -- """

def generate_LED_numbers(size):
    space = ' ' * (size + 2)                # '    '
    left = '|' + ' ' * (size + 1)           # '|   '
    right = ' ' * (size + 1) + '|'          # '   |'
    both = '|' + ' ' * size + '|'           # '|  |'
    middle = ' ' + '-' * size + ' '         # ' -- '

    numbers_list = []
    f = lambda a, b, c, d, e: '\n'.join([a] + [b] * size + [c] + [d] * size + [e])
    numbers_list.append(f(middle, both, space, both, middle))
    numbers_list.append(f(space, right, space, right, space))
    numbers_list.append(f(middle, right, middle, left, middle))
    numbers_list.append(f(middle, right, middle, right, middle))
    numbers_list.append(f(space, both, middle, right, space))
    numbers_list.append(f(middle, left, middle, right, middle))
    numbers_list.append(f(middle, left, middle, both, middle))
    numbers_list.append(f(middle, right, space, right, space))
    numbers_list.append(f(middle, both, middle, both, middle))
    numbers_list.append(f(middle, both, middle, right, middle))

    return numbers_list

# function for joining the numbers
# Pre-condition: all numbers have the same number of lines, len(l) > 0
def join_lines(l):
    assert len(l) > 0
    l = [num.splitlines() for num in l]
    joined_numbers = []
    for i in range(len(l[0])):
        joined_numbers.append(''.join([num[i] for num in l]))
    return '\n'.join(joined_numbers)


def LCD_print(size, number):
    if size <= 0: return None
    numbers_list = generate_LED_numbers(size)
    l = []
    for n in str(number):
        l.append(numbers_list[int(n)])
    return join_lines(l)

print LCD_print(2, 12345)
print LCD_print(3, 67890)
