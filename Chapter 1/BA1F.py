"""
Find a Position in a Genome Minimizing the Skew

Define the skew of a DNA string Genome, denoted Skew(Genome),
as the difference between the total number of occurrences of 'G' and 'C' in Genome.
"""

def get_skew(dna):
    """ returns positions where skew of dna is minimal """

    i = 0
    cur_skew = 0
    skews = []
    while i < len(dna):
        if dna[i] == "G":
            cur_skew += 1
        elif dna[i] == "C":
            cur_skew -= 1

        i += 1
        skews.append(cur_skew)

    length = len(skews)
    minimum = min(skews)
    for item in xrange(length):
        if skews[item] == minimum:
            print item + 1,

def read_data_from(file_name):
    with open(file_name, "r") as file:
        string = file.readline().strip()

    return string

if __name__ == "__main__":
    dna = read_data_from("in.txt")
    get_skew(dna)
