"""
Generate the d-Neighborhood of a String
"""

from BA1K import get_all_kmers
from BA1G import hamming_dist

def gen_d_neighb(d, fileName, data):
    """ returns and write to file_name d-neighborhood of a string """
    
    variants = get_all_kmers(len(data))
    var_len = len(variants)
    answers = []
    for i in xrange(var_len):
        if hamming_dist(data, variants[i]) <= d:
            answers.append(variants[i])

    file = open(fileName, 'w+')
    for item in answers:
        file.writelines(str(item) + "\n")

    return answers

if __name__ == "__main__":
    gen_d_neighb(1, "out.txt", "ACG")
