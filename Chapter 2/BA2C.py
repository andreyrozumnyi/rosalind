""" Find a Profile-most Probable k-mer in a String """

profile_row = {'A': 0, 'C':1, 'G':2, 'T':3}
def read_profile_matrix(fileName):
    with open(fileName) as f:
        lines = f.readlines()

    for i in xrange(0, len(lines)):
        lines[i] = lines[i].strip()

    data = list(list())
    for i in xrange(0, len(lines)):
        data.append(lines[i].split())

    for i in xrange(0, len(data)):
        for j in xrange(0, len(data[i])):
            data[i][j] = float(data[i][j])

    return data

def pattern_probability(profile, pattern):
    probability = 1
    for i in xrange(0, len(pattern)):
        probability *= profile[profile_row[pattern[i]]][i]

    return probability

def profile_most_probable_kmer(dna, profile, k):
    start = 0
    length = len(dna)
    max_probability = 0
    most_probable = ''
    while start + k <= length:
        substr = dna[start:start+k]
        probability = pattern_probability(profile, substr)
        if probability > max_probability:
            most_probable = substr
            max_probability = probability

        start += 1

    print most_probable

if __name__ == "__main__":
    data = read_profile_matrix("in.txt")
    profile_most_probable_kmer("TGACCTGGATAACAG", data, 6)
