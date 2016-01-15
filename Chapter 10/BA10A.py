""" Probability of a Hidden Path Problem """

def read_data(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
        file.readline()
        alphab = file.readline().strip().split()
        file.readline()
        file.readline()
        matr = []
        for i in xrange(len(alphab)):
            matr.append(file.readline().strip().split()[1:])

        for row in matr:
            for i in xrange(len(row)):
                row[i] = float(row[i])

        return string, alphab, matr

def main(str, alph, matr):
    answ = 0.5

    for i in xrange(len(str)-1):
        k = alph.index(str[i])
        j = alph.index(str[i+1])
        answ *= matr[k][j]

    return answ

if __name__ == "__main__":
    str, alph, matr = read_data("in.txt")
    print main(str, alph, matr)