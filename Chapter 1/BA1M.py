""" Implement NumberToPattern """

NumberToSymbol = {0:'A', 1:'C', 2:'G', 3:'T'}

def NumberToPattern(index, k):
    """ returns pattern in accordance to number """

    if k == 1:
        return NumberToSymbol[index]

    prefixIndex = index / 4
    r = index % 4
    prefixPattern = NumberToPattern(prefixIndex, k - 1)
    return prefixPattern + NumberToSymbol[r]

if __name__ == "__main__":
    print NumberToPattern(5267, 11)
