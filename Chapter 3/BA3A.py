""" Generate the k-mer Composition of a String """


def read_data_from(file_name):
    with open(file_name) as file:
        k = int(file.readline().rstrip())
        text = file.readline().rstrip()

    return k, text


def gen_composition(k, string):
    start = 0
    str_len = len(string)
    compositions = []
    while start + k <= str_len:
        sub = string[start:start+k]
        compositions.append(sub)
        start += 1

    compositions.sort()
    composition_len = len(compositions)
    for i in xrange(composition_len):
        print compositions[i]

if __name__ == "__main__":
    k, text = read_data_from("in")
    gen_composition(k, text)