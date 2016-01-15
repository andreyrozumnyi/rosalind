""" Implement Greedy Motif Search """

def read_data_from(filename):
    with open(filename) as f:
        data = f.readlines()

    for i in xrange(0, len(data)):
        data[i] = data[i].strip()

    return data

profile_row = {'A': 0, 'C':1, 'G':2, 'T':3}
def make_profile(kMers):
    """ return list of dictionaries where each dictionary is column of the profile """

    if len(kMers) == 0:
        print "None!!!"
        return None

    k = len(kMers[0])
    t = len(kMers)
    profile = list(dict())
    for i in xrange(k):
        profile_col = {'A':0, 'C':0, 'G':0, 'T':0}
        for j in xrange(t):
            profile_col[kMers[j][i]] += 1

        for key in profile_col.keys():
            profile_col[key] = 1.0 * profile_col[key] / t

        profile.append(profile_col)

    return profile

def pattern_probability(profile, pattern):
    probability = 1
    for i in xrange(0, len(pattern)):
        probability *= profile[i][pattern[i]]

    return probability

def profile_most_probable_kmer(dna, profile, k):
    start = 0
    length = len(dna)
    max_probability = 0
    most_probable = dna[0:k]
    while start + k <= length:
        substr = dna[start:start+k]
        probability = pattern_probability(profile, substr)
        if probability > max_probability:
            most_probable = substr
            max_probability = probability

        start += 1

    return most_probable

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

def make_consensus(motifes):
    profile = make_profile(motifes)
    consensusList = list()
    for item in profile:
        consensusList.append(max(item, key=item.get))

    return ''.join(consensusList)

def score(motifes):
    consensus = make_consensus(motifes)
    score = 0
    for motif in motifes:
        score += hamming_dist(consensus, motif)

    return score

def greedy_motif_search(Dna, k, t):
    if len(Dna) == 0:
        print "None!!!"
        return None

    bestMotif = list()
    for i in xrange(t):
        bestMotif.append(Dna[i][0:k])

    start = 0
    length = len(Dna[0])
    while start + k <= length:
        motifes = list()
        motifes.append(Dna[0][start:start+k])
        for i in xrange(1, t):
            profile = make_profile(motifes[0:i])
            motifes.append(profile_most_probable_kmer(Dna[i], profile, k))

        if score(motifes) < score(bestMotif):
            bestMotif = motifes[:]

        start += 1

    for element in bestMotif:
        print element

    return bestMotif

if __name__ == "__main__":
    Dna = read_data_from("in.txt")
    greedy_motif_search(Dna, 12, 25)