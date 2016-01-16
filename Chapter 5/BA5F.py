""" Find a Highest-Scoring Local Alignment of Two Strings """
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

def high_score_align(str1, str2, matr, alphab):
    SIGMA = 5
    cols_num = len(str1)
    rows_num = len(str2)
    dist_matr = np.zeros((rows_num + 1, cols_num + 1))
    for i in xrange(cols_num):
        dist_matr[0][i+1] = dist_matr[0][i] - SIGMA

    for i in xrange(rows_num):
        dist_matr[i+1][0] = dist_matr[i][0] - SIGMA

    for i in xrange(rows_num):
        for j in xrange(cols_num):
            dist_matr[i+1][j+1] = max(0,
                                      dist_matr[i][j+1] - SIGMA,
                                      dist_matr[i+1][j] - SIGMA,
                                      dist_matr[i][j] + matr[alphab.index(str2[i])][alphab.index(str1[j])])

    score = 0
    for k in xrange(rows_num + 1):
        for t in xrange(cols_num + 1):
            if score < dist_matr[k][t]:
                score = dist_matr[k][t]
                i = k - 1
                j = t - 1

    answ1 = []
    answ2 = []

    while i != -1 or j != -1:
        max_el = dist_matr[i+1][j+1] - matr[alphab.index(str2[i])][alphab.index(str1[j])]
        if max_el == dist_matr[i][j]:
            answ1 = [str1[j]] + answ1
            answ2 = [str2[i]] + answ2
            i -= 1
            j -= 1
        else:
            max_el = max(dist_matr[i+1][j], dist_matr[i][j+1])
            if max_el == dist_matr[i+1][j]:
                answ1 = [str1[j]] + answ1
                answ2 = ["-"] + answ2
                j -= 1
            else:
                answ1 = ["-"] + answ1
                answ2 = [str2[i]] + answ2
                i -= 1

        if max_el == 0:
            break

    print int(score)
    print "".join(answ1)
    print "".join(answ2)
    return score, answ1, answ2

if __name__ == "__main__":
    matr, alphab = read_matr("PAM250")
    str1, str2 = read_data("in.txt")
    high_score_align(str1, str2, matr, alphab)
