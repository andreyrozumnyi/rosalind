""" Find a Highest-Scoring Fitting Alignment of Two Strings """


def read_data(file_name):
    with open(file_name, 'r') as file:
        str1 = file.readline().rstrip()
        str2 = file.readline().rstrip()

    return str1, str2


def fitness_align(t, p):
    D = []
    for i in range(len(p)+1):
        D.append([0]*(len(t)+1))

    for i in range(1, len(p)+1):
        for j in range(1, len(t)+1):
            horizon = D[i][j-1] - 1
            vert = D[i-1][j] - 1
            if p[i-1] == t[j-1]:
                diag = D[i-1][j-1] + 1
            else:
                diag = D[i-1][j-1] - 1

            D[i][j] = max(horizon, vert, diag)

    score = max(D[-1])
    for k in xrange(len(D[-1])-1, -1, -1):
        if D[-1][k] == score:
            j = k
            break

    answ1 = []
    answ2 = []
    i = len(D) - 1
    while True:
        if D[i][j] == D[i-1][j-1] + [-1, 1][t[j-1] == p[i-1]]:
            answ1 = [t[j-1]] + answ1
            answ2 = [p[i-1]] + answ2
            i -= 1
            j -= 1
        else:
            max_el = max(D[i][j-1], D[i-1][j])
            if max_el == D[i][j-1]:
                answ1 = [t[j-1]] + answ1
                answ2 = ["-"] + answ2
                j -= 1
            elif max_el == D[i-1][j]:
                answ1 = ["-"] + answ1
                answ2 = [p[i-1]] + answ2
                i -= 1

        if i == 0 or j == 0:
            break

    print score
    print "".join(answ1)
    print "".join(answ2)

if __name__ == "__main__":
    text, pattern = read_data("in.txt")
    fitness_align(text, pattern)

