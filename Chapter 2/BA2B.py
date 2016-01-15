""" Find a Median String """
import itertools

def read_data_from_file(filename):
    with open(filename) as f:
        data = f.readlines()

    for i in xrange(0, len(data)):
        data[i] = data[i].strip()

    return data

def generate_all_substrings(k):
    variants = map(''.join, itertools.product('ACTG', repeat=k))
    answers = dict()
    for item in variants:
        answers[item] = 0

    return sorted(answers)

def hamming_dist(str_one, str_two):
    """ returns number of hamming_dist between two strings """

    len_one = len(str_one)
    len_two = len(str_two)
    if len_one != len_two:
        raise ValueError("Strings have different lengths.")

    mismatches = 0
    for i in xrange(len_one):
        if str_one[i] != str_two[i]:
            mismatches += 1

    return mismatches

def min_distance_in_string(dna, pattern):
    dList = list()
    start = 0
    length = len(dna)
    k = len(pattern)
    while start + k <= length:
        substr = dna[start:start+k]
        dList.append(hamming_dist(substr, pattern))
        start += 1

    return min(dList)

def distance_in_str_set(Dna, pattern):
    distances = list()
    for dna in Dna:
        distances.append(min_distance_in_string(dna, pattern))

    return sum(distances)

def find_median_str(Dna, k):
    allVariants = generate_all_substrings(k)
    answers = dict()
    for kMer in allVariants:
        answers[kMer] = distance_in_str_set(Dna, kMer)

    print min(answers, key=answers.get)

if __name__ == "__main__":
    Dna = read_data_from_file("in.txt")
    find_median_str(Dna, 6)


