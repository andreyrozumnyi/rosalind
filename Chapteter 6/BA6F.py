""" Implement ChromosomeToCycle """

def read_data(file_name):
    with open(file_name, 'r+') as file:
        line = file.readline().strip()

    line = line[1:len(line)-1].split()
    data = []
    for item in line:
        data.append(item)

    return data

def chrom_to_cycle(chromosoms):
    length = len(chromosoms)
    nodes = [0]*(2*length)
    for j in xrange(length):
        i = int(chromosoms[j])
        if i > 0:
            nodes[2*j] = 2*i-1
            nodes[2*j+1] = 2*i
        else:
            nodes[2*j] = -2*i
            nodes[2*j+1] = -2*i-1

    return nodes

def form_answ(data):
    answ = ' '.join(str(x) for x in data)
    answ = "(" + answ + ")"
    return answ

if __name__ == "__main__":
    data = read_data("in.txt")
    print form_answ(chrom_to_cycle(data))