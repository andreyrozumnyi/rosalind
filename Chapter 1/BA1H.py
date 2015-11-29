"""
Find All Approximate Occurrences of a Pattern in a String
"""

from BA1G import hamming_dist

def hamming_dist_approx(pattern, string, d):
    """ returns all approximate occurances (up to d mismatches) of pattern inside the string """

    start = 0
    pat_len = len(pattern)
    str_len = len(string)
    answer = []
    while start + pat_len < str_len:
        sub = string[start:start+pat_len]
        if (hamming_dist(pattern, sub) <= d):
            answer.append(start)

        start += 1

    return answer

def read_data_from(file_name):
    with open(file_name, "r") as file:
        pattern = file.readline().strip()
        string = file.readline().strip()
        d = int(file.readline().strip())

    return pattern, string, d

if __name__ == "__main__":
    pattern, string, d = read_data_from("in.txt")
    answer = hamming_dist_approx(pattern, string, d)
    for elem in answer:
        print elem,