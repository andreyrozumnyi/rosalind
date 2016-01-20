""" Reconstruct a String from its Genome Path """


def read_data_from(file_name):
    with open(file_name) as f:
        data = f.readlines()
    for i in xrange(0, len(data)):
        data[i] = data[i].strip()
    return data


def special_cocatination(kmers):
    answer = kmers[0]
    k = len(answer)
    for i in xrange(1, len(kmers)):
        answer += kmers[i][k - 1]

    print answer

if __name__ == "__main__":
    data = read_data_from("in")
    special_cocatination(data)
