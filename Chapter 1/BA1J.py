"""
Find Frequent Words with Mismatches and Reverse Complements
"""

from BA1C import rev_complement
from BA1G import hamming_dist
from BA1I import get_all_kmers

def main(k, d, data):
    variants = get_all_kmers(k)
    start = 0
    data_len = len(data)
    while start + k <= data_len:
        sub = data[start:start + k]
        for item in variants.keys():
            if hamming_dist(item, sub) <= d:
                variants[item] += 1

            if hamming_dist(rev_complement(item), sub) <= d:
                variants[item] += 1

        start += 1

    values = variants.values()
    maximum = max(values)
    answer = []
    for key in variants.keys():
        if variants[key] == maximum:
            answer.append(key)

    return answer

def read_data_from(file_name):
    with open(file_name, "r") as file:
        string = file.readline().strip()
        k, d = file.readline().strip().split()

    return string, int(k), int(d)

if __name__ == "__main__":
    string, k, d = read_data_from("in.txt")
    answer = main(k, d, string)
    for elem in answer:
        print elem,