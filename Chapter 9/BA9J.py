""" Reconstruct a String from its Burrows-Wheeler Transform """

def read_data(file_name):
    with open(file_name, "r") as file:
        data = file.readline().strip()

    return data

def decompression(bwt):
    last = bwt
    first = sorted(bwt)
    length = len(bwt)
    first_ind = []
    last_ind = []
    dict_for_ind_1 = {}
    dict_for_ind_2 = {}
    for i in xrange(length):
        #indexing first column
        if first[i] in dict_for_ind_1:
            dict_for_ind_1[first[i]] += 1
        else:
            dict_for_ind_1[first[i]] = 1

        first_ind.append((first[i], dict_for_ind_1[first[i]]))
        #indexing last column
        if last[i] in dict_for_ind_2:
            dict_for_ind_2[last[i]] += 1
        else:
            dict_for_ind_2[last[i]] = 1

        last_ind.append((last[i],dict_for_ind_2[last[i]]))

    answer = [first[0]]
    index = 0
    for i in xrange(length-1):
        answer.append(last[index])
        index = first_ind.index((answer[-1], last_ind[index][1]))

    return "".join(answer[::-1])

if __name__ == "__main__":
    data = read_data("in.txt")
    print decompression(data)