""" Compute the Probability of an Outcome Given a Hidden Path """

def read_data(file_name):
    with open(file_name, 'r') as file:
        string1 = file.readline().strip()
        file.readline()
        alphab1 = file.readline().strip().split()
        file.readline()
        string2 = file.readline()
        file.readline()
        alphab2 = file.readline().strip().split()
        file.readline()
        file.readline()
        matr = []
        for i in xrange(len(alphab2)):
            matr.append(file.readline().strip().split()[1:])

        for row in matr:
            for i in xrange(len(row)):
                row[i] = float(row[i])

        return string1, string2, alphab1, alphab2, matr

def main(str1, str2, alph1, alph2):
    length = len(str1)
    answer = 1
    for i in xrange(length):
        answer *= matr[alph2.index(str2[i])][alph1.index(str1[i])]

    return answer
if __name__ == "__main__":
    str1, str2, alph1, alph2, matr = read_data("in.txt")
    print main(str1, str2, alph1, alph2)