""" Construct the Partial Suffix Array of a String """

def read_data(file_name):
    with open(file_name, 'r') as file:
        text = file.readline().rstrip()
        k = int(file.readline().rstrip())

    return text, k

def suffix_array(text):
    suffixes = []
    for i in xrange(len(text)):
        suffixes.append((text[i:], i))

    suffixes.sort()
    return suffixes

if __name__ == "__main__":
    text, k = read_data("in.txt")
    suf_array = suffix_array(text)
    for i in xrange(len(suf_array)):
        if suf_array[i][1]%k == 0:
            print "%d,%d" % (i, suf_array[i][1])
