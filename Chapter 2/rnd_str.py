""" Introduction to Random Strings """

import numpy

def read_data_from(file_name):
    with open(file_name) as f:
        data = f.readlines()

    for i in xrange(0, len(data)):
        string = data[i]
        answer = string.split()

    length = len(answer)
    for i in xrange(length):
        answer[i] = float(answer[i])

    return answer

def rnd_strings(string, xList):
    probabilities = dict()
    output = list()
    length = len(string)
    for x in xList:
        prob = 1
        probabilities["G"] = 1.0*x / 2
        probabilities["C"] = 1.0*x / 2
        probabilities["A"] = 1.0*(1 - x) / 2
        probabilities["T"] = 1.0*(1 - x) / 2
        for i in xrange(length):
            prob *= probabilities[string[i]]

        output.append(numpy.log10(prob))

    for item in output:
        print "%.3f" % (item),

if __name__ == "__main__":
    data = read_data_from("in.txt")
    rnd_strings("ACAAGATTGACCCCTCCATAGTGAGTGAATTAATGTAAGTCCCAATGATACGCAATAATAATCTGTGCGGGGAGATTCTCTATGTCTGTTGAGACTTC", data)
