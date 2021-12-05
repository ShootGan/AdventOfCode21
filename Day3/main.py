
def get_data(filename):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    return len(data[0]) , [int(i, 2) for i in data]
     
def count_power_consumption(data):
    gamma = 0
    epsilon = 0 
    list_len = len(data)
    
    for i in range(1,number_bit_length+1):
        shift = number_bit_length - i
        ones = sum([((x & (1 << shift)) >> shift) for x in data])
        zeros = list_len - ones
        bit = 1 if ones > zeros else 0
        gamma = (gamma << 1) | bit
        epsilon = (epsilon << 1) | (1 - bit)
    return gamma * epsilon


def count_oxygen(data):
    shift = number_bit_length - 1
    while shift >= 0 and len(data) > 1:
        ones = sum([((x & (1 << shift)) >> shift) for x in data])
        zeros = len(data) - ones
        if ones >= zeros:
            data = [ x for x in data if ((x & (1 << shift)) >> shift) == 1]
        else:
            data = [ x for x in data if ((x & (1 << shift)) >> shift) == 0]
        shift -= 1
    return data[0]


def count_co2(data):
    shift = number_bit_length - 1
    while shift >= 0 and len(data) > 1:
        ones = sum([((x & (1 << shift)) >> shift) for x in data])
        zeros = len(data) - ones
        if ones >= zeros:
            data = [ x for x in data if ((x & (1 << shift)) >> shift) == 0]
        else:
            data = [ x for x in data if ((x & (1 << shift)) >> shift) == 1]
        shift -= 1
    return data[0]


def count_life_support(data):
    return count_oxygen(data) * count_co2(data)


if __name__ == '__main__':
    number_bit_length, data = get_data('.\day3\input.txt')
    print(count_power_consumption(data))
    print(count_life_support(data))

