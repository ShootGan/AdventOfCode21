

def load_input(filename: str) -> list:
    # get 2d list from input file by space delimiter
    with open(filename, 'r') as f:
        return [line.split() for line in f]


def count_results(input: list) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(len(input)):
        if input[i][0] == 'forward':
            horizontal += int(input[i][1])
            depth += int(input[i][1]) * aim
        elif input[i][0] == 'down':
            aim += int(input[i][1])
        else:
            aim -= int(input[i][1])
    return horizontal * depth


if __name__ == '__main__':
    input = load_input('.\day2\input.txt')
    print(count_results(input))
