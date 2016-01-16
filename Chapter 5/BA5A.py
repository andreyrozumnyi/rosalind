""" Find the Minimum Number of Coins Needed to Make Change """
import numpy as np

def read_data(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        line = file.readline().split(',')
        data = [int(i.strip()) for i in line]

    return n, data

def min_coins_num(amount, coins):
    num_list = [0]*(amount+1)
    num_list[0] = 0
    for k in xrange(1, amount+1):
        cur_min = np.inf
        for i in coins:
            if k >= i:
                cur_min = min(cur_min, num_list[k-i])

        num_list[k] = cur_min + 1

    print num_list[-1]
    return num_list[-1]

if __name__ == '__main__':
    n, coins = read_data('in.txt')
    min_coins_num(n, coins)