""" Implement Motif Enumeration """
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

def motif_enumeration(data, k, d):
    Patterns = set(generate_all_substrings(k))
    PatternsCopy = Patterns.copy()
    for dna in data:
       currentSet = set()
       start = 0
       length = len(dna)
       while start + k <= length:
           substr = dna[start: start + k]
           for item in PatternsCopy:
               if hamming_dist(substr, item) <= d:
                   currentSet.add(item)

           start += 1

       Patterns = Patterns & currentSet

    for item in Patterns:
        print item

if __name__ == "__main__":
    data = read_data_from_file("in.txt")
    motif_enumeration(data, 5, 1)
