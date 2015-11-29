"""
Compute the Hamming Distance Between Two Strings

The number of mismatches between strings p and q is called the Hamming distance between these strings
"""

def hamming_dist(str_one, str_two):
    """ returns number of mismatches between two strings """

    len_one = len(str_one)
    len_two = len(str_two)
    if len_one != len_two:
        raise ValueError("Strings have different lengths.")

    mismatches = 0
    for i in xrange(len_one):
        if str_one[i] != str_two[i]:
            mismatches += 1

    return mismatches

def read_data_from(file_name):
    with open(file_name, "r") as file:
        str_one = file.readline().strip()
        str_two = file.readline().strip()

    return str_one, str_two

if __name__ == "__main__":
    str_one, str_two = read_data_from("in.txt")
    print hamming_dist(str_one, str_two)