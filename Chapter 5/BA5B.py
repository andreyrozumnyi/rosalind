""" Find the Length of a Longest Path in a Manhattan-like Grid """

def read_data(file_name):
    with open(file_name, 'r+') as file:
        line = file.readline().split()
        n = int(line[0].strip())
        m = int(line[1].strip())
        down_matrix = [[0]*(m+1) for _ in xrange(n)]
        for i in xrange(n):
            line = [int(item.strip()) for item in file.readline().split()]
            for j in xrange(m+1):
                down_matrix[i][j] = line[j]

        file.readline()
        right_matrix = [[0]*(m) for _ in xrange(n+1)]
        for i in xrange(n+1):
            line = [int(item.strip()) for item in file.readline().split()]
            for j in xrange(m):
                right_matrix[i][j] = line[j]

        return n, m, down_matrix, right_matrix

def longest_manh_path(n, m, down, right):
    score = [[0]*(m+1) for _ in xrange(n+1)]
    for i in xrange(1, n+1):
        score[i][0] = score[i - 1][0] + down[i - 1][0]

    for j in xrange(1, m+1):
        score[0][j] = score[0][j - 1] + right[0][j - 1]

    for i in xrange(1, n+1):
        for j in range(1, m+1):
            score[i][j] = max(score[i - 1][j] + down[i - 1][j], score[i][j - 1] + right[i][j - 1])

    print score[n][m]
    return score[n][m]


if __name__ == "__main__":
    n, m, down_matr, right_matr = read_data("in.txt")
    longest_manh_path(n, m, down_matr, right_matr)