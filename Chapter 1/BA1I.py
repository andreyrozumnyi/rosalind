"""
Find the Most Frequent Words with Mismatches in a String
"""

import itertools
from BA1G import hamming_dist

def get_all_kmers(k):
    """ generates all possible k-mers from alphabet A,C,T,G """

    variants = map(''.join, itertools.product('ACTG', repeat=k))
    answers = dict()
    for item in variants:
        answers[item] = 0

    return answers

def most_freq_mismatches_words(k, d, string):
    """ returns most frequent k-mers with up to d mismatches inside the string """

    variants = get_all_kmers(k)
    start = 0
    data_len = len(string)
    while start + k < data_len:
        sub = string[start:start + k]
        for item in variants.keys():
            if hamming_dist(item, sub) <= d:
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
    answer = most_freq_mismatches_words(k, d, string)
    for elem in answer:
        print elem,