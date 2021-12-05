from timeit import default_timer as timer
from datetime import timedelta

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
            #1158
            sliding_list.append(sum(list[i:i+3]))
    return count(sliding_list)


if __name__ == '__main__':
    start = timer()
    mesures = open_input('.\Day1\input.txt')
    print(count(mesures))
    end = timer()
    print(timedelta(seconds=end-start))
    print(count_part_two(mesures))
