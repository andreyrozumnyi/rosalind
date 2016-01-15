""" Implement BetterBWMatching """

def read_data(file_name):
    with open(file_name, "r") as file:
        last_col = file.readline().rstrip()
        patterns = file.readline().rstrip().split()

    return last_col, patterns

def better_BWT_matching(last_col, pattern):
    top = 0
    bottom = len(last_col) - 1
    first_col = ''.join(sorted(last_col))
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in last_col[top:bottom+1]:
                top = first_col.find(symbol) + last_col.count(symbol, 0, top)
                bottom = first_col.find(symbol) + last_col.count(symbol, 0, bottom + 1) - 1
            else:
                return 0
        else:
            return bottom - top + 1


if __name__ == "__main__":
    last_col, patterns = read_data("in.txt")
    for pattern in patterns:
        print better_BWT_matching(last_col, pattern),