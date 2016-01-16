""" Implement GreedySorting to Sort a Permutation by Reversals """

def read_data(file_name):
    with open(file_name, 'r+') as file:
        line = file.readline().strip()

    line = line[1:len(line)-1].split()
    data = []
    for item in line:
        data.append(item)

    return data

def rev_subseq(start, end, str):
    seq = str[:start]
    seq += str[start:end][::-1]
    seq += str[end:]
    for i in xrange(start, end):
        if "+" in seq[i]:
            seq[i] = seq[i].replace("+", "-")
        else:
            seq[i] = seq[i].replace("-", "+")

    return seq

def format_answ(data):
    answ = " ".join(data)
    answ = "(" + answ + ")"
    return answ

def greedy_sort_rev(data):
    answer = []
    for i in xrange(1, len(data)+1):
        for j in xrange(i-1, len(data)):
            if str(i) == data[j][1:]:
                data = rev_subseq(i-1, j+1, data)
                answer.append(format_answ(data))
                if "-" in data[i-1]:
                    data[i-1] = data[i-1].replace("-", "+")
                    answer.append(format_answ(data))

                break

    return answer

def write_to_file(file_name, data):
    with open(file_name, 'w') as file:
        for i in xrange(len(data)):
            file.writelines(data[i]+"\n")

if __name__ == "__main__":
    data = read_data("in.txt")
    answ = greedy_sort_rev(data)
    write_to_file("out.txt", answ)
