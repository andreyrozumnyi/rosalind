""" Compute the Probability of a String Emitted by an HMM """

def read_data(file_name):
    with open(file_name, 'r') as file:
        string = file.readline().strip()
        file.readline()
        alphab1 = file.readline().strip().split()
        file.readline()
        alphab2 = file.readline().strip().split()
        file.readline()
        file.readline()
        trans_matr = []
        for i in xrange(len(alphab2)):
            trans_matr.append(file.readline().strip().split()[1:])

        for row in trans_matr:
            for i in xrange(len(row)):
                row[i] = float(row[i])

        file.readline()
        file.readline()
        emis_matr = []
        for i in xrange(len(alphab2)):
            emis_matr.append(file.readline().strip().split()[1:])

        for row in emis_matr:
            for i in xrange(len(row)):
                row[i] = float(row[i])

        return string, alphab1, alphab2, trans_matr, emis_matr

def main(str, em_alphab, tr_alphab, trans_matr, emis_matr):
    tr_al_len = len(tr_alphab)
    str_len = len(str)
    dist_matr = [[0 for _ in xrange(str_len)] for _ in xrange(tr_al_len)]
    for i in xrange(tr_al_len):
        dist_matr[i][0] = 1.0*emis_matr[i][em_alphab.index(str[0])]/tr_al_len



    for i in xrange(1, str_len):
        for j in xrange(tr_al_len):
            for k in xrange(tr_al_len):
                dist_matr[j][i] += dist_matr[k][i-1]*trans_matr[k][j]*emis_matr[j][em_alphab.index(str[i])]

    prob = 0
    for i in xrange(tr_al_len):
        prob += dist_matr[i][-1]

    return prob

if __name__ == "__main__":
    string, alphab1, alphab2, trans_matr, emis_matr = read_data("in.txt")
    print main(string, alphab1, alphab2, trans_matr, emis_matr)