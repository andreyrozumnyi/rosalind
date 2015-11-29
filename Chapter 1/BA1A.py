def occurrences(string, sub):
    """
    :param string: string for analyzing
    :param sub: pattern for searching
    :return: number of occurences of pattern in a string taking into account ovelapping cases
    """
    number = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            number += 1
        else:
            return number

def read_data_from(file_name):
    with open(file_name, "r") as file:
        string = file.readline().strip()
        pattern = file.readline().strip()

    return string, pattern

if __name__ == "__main__":
    string, pattern = read_data_from("in.txt")
    print occurrences(string, pattern)




