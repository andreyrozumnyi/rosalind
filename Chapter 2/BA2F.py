""" Implement RandomizedMotifSearch """

import numpy as np

def read_data(file_name):
    with open(file_name, 'r') as file:
        k, t = (int(element) for element in (file.readline().strip()).split())
        motifs = [motif.strip() for motif in file]

    return k, t, motifs

def rand_motif_search(dna, k, t):
    last_ind = len(dna[0]) - k + 1
    idxs = [np.random.randint(0, last_ind) for _ in xrange(t)]
    best_motifs = [s[start:(start+k)] for s, start in zip(dna, idxs)]

    while True:
        profile = create_profile(best_motifs)
        motifs = create_motifs(profile, dna)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs

def create_profile(motifs):
    profile = dict()
    motif_len = len(motifs[0])
    motifs_num = len(motifs)
    profile['A'] = [1 for _ in xrange(motif_len)]
    profile['C'] = [1 for _ in xrange(motif_len)]
    profile['G'] = [1 for _ in xrange(motif_len)]
    profile['T'] = [1 for _ in xrange(motif_len)]

    for i in xrange(motifs_num):
        for j in xrange(motif_len):
            profile[motifs[i][j]][j] += 1

    return profile

def create_motifs(profile, dna):
    return [get_best_match(profile, s) for s in dna]

def get_best_match(profile, string):
    motif_len = len(profile['A'])
    scores = calc_prob_for_all(profile, string)
    start = scores.index(max(scores))
    return string[start:start + motif_len]

def calc_prob_for_all(profile, string):
    return [calc_prob(profile, string, pos) for pos in xrange(len(string)-len(profile['A']))]

def calc_prob(profile, string, pos):
    result = 1
    for i in xrange(len(profile['A'])):
        result *= profile[string[pos+i]][i]

    return result

def score(motifs):
    consensus = get_consensus(motifs)
    score = 0
    for motif in motifs:
        score += hamming_dist(consensus, motif)

    return score

def get_consensus(motifs):
    length = len(motifs[0])
    profile = dict()
    profile['A'] = [0 for _ in xrange(length)]
    profile['C'] = [0 for _ in xrange(length)]
    profile['G'] = [0 for _ in xrange(length)]
    profile['T'] = [0 for _ in xrange(length)]

    for i in xrange(len(motifs)):
        for j in xrange(length):
            profile[motifs[i][j]][j] += 1

    consensus = []
    for j in xrange(length):
        max_elem = max(profile['A'][j],
                         profile['C'][j],
                         profile['G'][j],
                         profile['T'][j])

        if max_elem == profile['A'][j]:
            consensus.append("A")
        elif max_elem == profile['C'][j]:
            consensus.append("C")
        elif max_elem == profile['G'][j]:
            consensus.append("G")
        else:
            consensus.append("T")

    return "".join(consensus)

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

if __name__ == "__main__":
    ITER_NUM = 10000
    k, t, strings = read_data("in.txt")
    best_motifs = rand_motif_search(strings, k, t)
    for index in xrange(ITER_NUM):
        motifs = rand_motif_search(strings, k, t)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    for motif in motifs:
        print motif
