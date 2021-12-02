
def open_input(filename):
    # get list of numbers from input file
    with open(filename) as f:
        numbers = [int(line.rstrip('\n')) for line in f]
    return numbers


def count(list):
    counter = 0
    for i in range(1, len(list)):
        if list[i] > list[i-1]:
            counter += 1
    return counter


def count_part_two(list):
    sliding_list = []
    for i in range(len(list)):
        if i+2 < len(list):
            sliding_list.append(list[i]+list[i+1]+list[i+2])
    return count(sliding_list)


if __name__ == '__main__':
    mesures = open_input('.\Day1\input.txt')
    print(count(mesures))
    print(count_part_two(mesures))
