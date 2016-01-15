""" Construct the Burrows-Wheeler Transform of a String """

def read_data(file_name):
    with open(file_name, "r") as file:
        data = file.readline().strip()

    return data

def circular_str(start, length, string):
    if start >= len(string):
        return

    if start + length <= len(string):
        return string[start: start + length]
    else:
        answer = string[start:]
        answer += string[:(start + length) % (len(string))]
        return answer

def bwt(genome):
    length = len(genome)
    table = []
    for i in xrange(length-1, -1, -1):
        table.append(circular_str(i, length, genome))

    table.sort()
    return "".join(table[i][-1] for i in xrange(len(table)))

if __name__ == "__main__":
    data = read_data("in.txt")
    print bwt(data)