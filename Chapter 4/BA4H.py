""" Generate the Convolution of a Spectrum """
import operator


def read_data_from(file_name):
    with open(file_name) as file:
        spectrum = file.readline().strip().split()

    for i in xrange(len(spectrum)):
        spectrum[i] = int(spectrum[i])

    return spectrum


def write_to(fileName, data):
    with open(fileName, "w+") as file:
        for i in xrange(len(data)):
            for j in xrange(data[i][1]):
                file.write("%s " % (str(data[i][0])))


def gen_convolution(spectrum):
    convolution_dict = dict()
    for i in xrange(1, len(spectrum)):
        for j in xrange(i):
            if spectrum[i] == spectrum[j]:
                continue

            diff = abs(spectrum[i] - spectrum[j])
            if diff in convolution_dict:
                convolution_dict[diff] += 1
            else:
                convolution_dict[diff] = 1

    sorted_convolutional_dict = sorted(convolution_dict.items(), key=operator.itemgetter(1))
    write_to("out", sorted_convolutional_dict[::-1])
    return sorted_convolutional_dict[::-1]


if __name__ == "__main__":
    spectrum = read_data_from("in")
    gen_convolution(spectrum)