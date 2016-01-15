""" Implement DistanceBetweenPatternAndStrings """
import itertools

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

def min_dist_in_str(dna, pattern):
    d_list = list()
    start = 0
    length = len(dna)
    k = len(pattern)
    while start + k <= length:
        substr = dna[start:start+k]
        d_list.append(hamming_dist(substr, pattern))
        start += 1

    return min(d_list)

def dist_in_str_set(Dna, pattern):
    distances = list()
    for dna in Dna:
        distances.append(min_dist_in_str(dna, pattern))

    return sum(distances)

def find_median_string(Dna, k):
    all_variants = generate_all_substrings(k)
    answers = dict()
    for kmer in all_variants:
        answers[kmer] = dist_in_str_set(Dna, kmer)

    print min(answers, key=answers.get)

if __name__ == "__main__":
    Dna = "TCACTTTCGCTAAGCTATGCTGGTGCGGACATGTAAATTCTAATATACCTTCAGGGTGTATGCATTTAATTAAGGTCCCTTTGGCCTGATACATGGTAACCA CGGATTACCAGATGGACTGTTGTCCCGGTGAGCTTCATGGGATTACCAACAGCTGACTGTACACCGCGGTACATCGCATCGGTCAATCAAAATACTACCACA AAGACCATCCGCCTGCTCCAATGAATTGACACCTCAGTGCTTCCAGATAGCATGACGCCATTGAGACATGGTTCCCGAGCCATAACCATTACCAGACCTGCG GGCGGATGTCTGAAGCGTATGAGAAAGTCGTTTAGTGCAGTCTCAGCGAATTTACTATAGATTGGTCAAACTAGGTCTACCTTTCGAGTGGGACCTCAGAGG CGGCCGCCTTGGCTATCGAATCAGACCGGTACACGGTCATCACGCTTCCACATAACGGTAGCATAGCACTTATGGAAGCGCTGCTCCCCTCTTTGTGAGTAT CGATCAAAAGGTTGCCACAGGGGAGCCTGGGACTCGTTTAGGTGCCGGTTGGCTGGAGCCGGGATCGCTCAGTGAGGAAGTCACTAGAACTCCGCCCCGGAG CCGATGTTGGCAACTGCTCGACACACGCATAGATCGCTGAATCCGAAAATTTAGGCGATTAGATAGCTCGGACGATATAGCGCAATCAGGGCGGGGAATGTG TCGTCTCTGTGTCTGCATAAAGAACCCCACCATCCGAGCCGGGTGTTTCAGTTATATAATGTGTCGCGTTTGTTCATGGCCGCATGGTTCACTGAGGACTGG ACCTCCGAGCGCAACTCGTTTTGCACGAACCGTGTCCCGTGAACTTTTTTTATGGCGTTTAGTGCCCGTTATTAGGCTTAAAGAGGGTATAAAAAACCTTGC".split()
    print dist_in_str_set(Dna, "GACTTTA")

