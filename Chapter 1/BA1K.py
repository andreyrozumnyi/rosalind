""" Generate the Frequency Array of a Strings """

import itertools
from BA1A import occurrences
def get_all_kmers(k):
    """ return list of kmers sorted alphabetically """

    variants = map(''.join, itertools.product('ACTG', repeat=k))
    answer = []
    for item in variants:
        answer.append(item)

    return sorted(answer)

def get_freq_array(k, dna):
    variants = get_all_kmers(k)
    freq_list = []
    vars_len = len(variants)
    for i in xrange(vars_len):
        freq_list.append(occurrences(dna, variants[i]))

    answer = []
    for item in freq_list:
        answer.append(item)

    return answer

def read_data_from(file_name):
    with open(file_name, "r") as file:
        string = file.readline().strip()
        k = int(file.readline().strip())

    return string, k

if __name__ == "__main__":
    dna, k = read_data_from("in.txt")
    answer = get_freq_array(k, dna)
    for elem in answer:
        print elem,
