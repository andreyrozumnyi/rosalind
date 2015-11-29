""" Implement NumberToPattern """

numb_to_symb = {0:'A', 1:'C', 2:'G', 3:'T'}

def num_to_pattern(index, k):
    """ returns pattern in accordance to number """

    if k == 1:
        return numb_to_symb[index]

    pref_ind = index / 4
    r = index % 4
    pref_pattern = num_to_pattern(pref_ind, k - 1)
    return pref_pattern + numb_to_symb[r]

if __name__ == "__main__":
    print num_to_pattern(5267, 11)
