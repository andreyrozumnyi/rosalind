"""
Find the Reverse Complement of a String
"""

def rev_complement(string):
    """
    :param string: string that need to be reversed and complemented
    :return: reveresed complement of the string
    """
    reversed = []
    length = len(string)
    i = 0
    while i < length:
        if string[i] == "A":
            reversed.append("T")
        elif string[i] == "T":
            reversed.append("A")
        elif string[i] == "C":
            reversed.append("G")
        elif string[i] == "G":
            reversed.append("C")

        i += 1

    return "".join(reversed[::-1])


def read_data_from(file_name):
    with open(file_name, "r") as file:
        string = file.readline().strip()

    return string

if __name__ == "__main__":
    string = read_data_from("in.txt")
    print rev_complement(string)