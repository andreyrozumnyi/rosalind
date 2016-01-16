""" Align Two Strings Using Affine Gap Penalties """
import numpy as np


def read_matr(file_name):
    with open(file_name, 'r') as file:
        alphab = file.readline().rstrip().split()
        matr = []
        for _ in xrange(len(alphab)):
            line = file.readline().rstrip().split()
            matr.append([int(line[i]) for i in xrange(1, len(line))])

    return matr, alphab


def read_data(file_name):
    with open(file_name, 'r') as file:
        str1 = file.readline().rstrip()
        str2 = file.readline().rstrip()

    return str1, str2


def affine_gap_align(str1, str2, matr, alphab):
    SIGMA = 11
    EPS = 1
    len_one = len(str1)
    len_two = len(str2)
    low_matr = np.zeros((len_one + 1, len_two + 1))
    mid_matr = np.zeros((len_one + 1, len_two + 1))
    up_matr = np.zeros((len_one + 1, len_two + 1))
    trans_low = []
    trans_mid = []
    trans_up = []
    for i in range(len_one+1):
        trans_low.append([0]*(len_two+1))
        trans_mid.append([0]*(len_two+1))
        trans_up.append([0]*(len_two+1))

    for i in xrange(1, len_one+1):
        for j in xrange(1, len_two+1):
            low_matr[i][j] = max(low_matr[i-1][j] - EPS, mid_matr[i-1][j] - SIGMA)
            if low_matr[i][j] == low_matr[i-1][j] - EPS:
                trans_low[i][j] = ('l', i-1, j)
            else:
                trans_low[i][j] = ('m', i-1, j)

            up_matr[i][j] = max(up_matr[i][j-1] - EPS, mid_matr[i][j-1] - SIGMA)
            if up_matr[i][j] == up_matr[i][j-1] - EPS:
                trans_up[i][j] = ('u', i, j-1)
            else:
                trans_up[i][j] = ('m', i, j-1)

            mid_matr[i][j] = max(low_matr[i][j],
                                 mid_matr[i-1][j-1] + matr[alphab.index(str1[i-1])][alphab.index(str2[j-1])],
                                 up_matr[i][j])
            if mid_matr[i][j] == low_matr[i][j]:
                trans_mid[i][j] = ('l', i, j)
            elif mid_matr[i][j] == up_matr[i][j]:
                trans_mid[i][j] = ('u', i, j)
            else:
                trans_mid[i][j] = ('m', i-1, j-1)

    answ1 = []
    answ2 = []
    came_from = trans_mid[len_one][len_two]
    cur_matr = 'm'
    while came_from != 0:
        if cur_matr == 'm':
            if came_from[0] == 'm':
                answ1 = [str1[came_from[1]]] + answ1
                answ2 = [str2[came_from[2]]] + answ2
                came_from = trans_mid[came_from[1]][came_from[2]]
            elif came_from[0] == 'l':
                answ1 = [str1[came_from[1]-1]] + answ1
                answ2 = ["-"] + answ2
                came_from = trans_low[came_from[1]][came_from[2]]
                cur_matr = 'l'
            else:
                #???
                answ1 = ["-"] + answ1
                answ2 = [str2[came_from[2]-1]] + answ2
                came_from = trans_up[came_from[1]][came_from[2]]
                cur_matr = 'u'

        elif cur_matr == 'l':
            if came_from[0] == 'l':
                answ1 = [str1[came_from[1]-1]] + answ1
                answ2 = ["-"] + answ2
                came_from = trans_low[came_from[1]][came_from[2]]
            else:
                came_from = trans_mid[came_from[1]][came_from[2]]
                cur_matr = 'm'

        elif cur_matr == 'u':
            if came_from[0] == 'u':
                answ1 = ["-"] + answ1
                answ2 = [str2[came_from[2]-1]] + answ2
                came_from = trans_up[came_from[1]][came_from[2]]
            else:
                came_from = trans_mid[came_from[1]][came_from[2]]
                cur_matr = 'm'
        else:
            print "There is no path"
            break

    print int(mid_matr[-1][-1])
    print "".join(answ1)
    print "".join(answ2)


if __name__ == "__main__":
    matr, alphab = read_matr("BLOSUM62")
    str1, str2 = read_data("in.txt")
    affine_gap_align(str1, str2, matr, alphab)
