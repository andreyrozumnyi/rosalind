""" Compute Limb Lengths in a Tree """
import sys

def read_data(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        j = int(file.readline().strip())
        D = []
        lines = file.readlines()
        for line in lines:
            line = line.strip().split()
            D.append([int(elem) for elem in line])

        return D, j

def limb_length(D, j):
    limb_len = sys.maxint
    for i in xrange(len(D)):
        for k in xrange(len(D[i])):
            if (i != j) and (j != k) and (i != k):
                temp = (D[i][j] + D[j][k] - D[i][k])/2
                limb_len = min(limb_len, temp)

    return limb_len

if __name__ == "__main__":
    D, j = read_data("in.txt")
    print limb_length(D, j)
