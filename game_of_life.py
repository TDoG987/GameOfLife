import random

def dead_state(width, height):
    state = [[0 for _ in range(width)] for _ in range(height)]

    return state


def random_state(width, height):
    state = dead_state(width, height)

    for i in range(height):
        for j in range(width):
            random_number = random.random()

            if random_number >= 0.5:
                cell_state = 0
            else:
                cell_state = 1

            state[i][j] = cell_state

    return state


def render(state):
    for i in range(len(state[0]) + 2):
        print('-', end='')

    print()

    for row in state:

        print_row = ""
        print_row += '|'

        for char in row:
            if char == 0:
                print_row += ' '
            else:
                print_row += '#'

        print_row += '|'

        print(print_row)

    for i in range(len(state[0]) + 2):
        print('-', end='')

    print()


render(dead_state(5, 5))

render(random_state(5, 5))