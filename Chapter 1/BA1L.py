""" Implement PatternToNumber """

symb_to_numb = {'A':0, 'C':1, 'G':2, 'T':3}

def pattern_to_number(pattern):
    """ return number in accordance to pattern """

    if not pattern:
        return 0

    return 4 * pattern_to_number(pattern[:-1]) + symb_to_numb[pattern[-1]]

if __name__ == "__main__":
    print pattern_to_number("ATGTCAAGGGGTGACGAAAGGTAGGTTG")
