""" Construct the Overlap Graph of a Collection of k-mers """
import collections


def read_data_from(file_name):
    with open(file_name) as f:
        data = f.readlines()

    for i in xrange(0, len(data)):
        data[i] = data[i].strip()

    return data


def prefix(string):
    return string[:len(string)-1]


def suffix(string):
    return string[1:]


def overlap(patterns, out_file):
    pat_len = len(patterns)
    pairs = {}
    for i in xrange(pat_len):
        for j in xrange(pat_len):
            if (i != j) and (suffix(patterns[i]) == prefix(patterns[j])):
                pairs[patterns[i]] = patterns[j]

    od = collections.OrderedDict(sorted(pairs.items()))
    with open(out_file, 'w+') as file:
        for key in od.keys():
            file.write(str(key) + " -> " + str(od[key]) + "\n")


if __name__ == "__main__":
    patterns = read_data_from("in")
    overlap(patterns, "out")