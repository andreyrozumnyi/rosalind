""" Implement CycleToChromosome """

def read_data(file_name):
    with open(file_name, "r") as file:
        line = file.readline().strip().split()
        line[0] = line[0].replace("(", "")
        line[len(line)-1] = line[len(line)-1].replace(")","")

    for i in xrange(len(line)):
        line[i] = int(line[i])

    return line

def cycle_to_chrom(nodes):
    length = len(nodes)
    chrom = [0]*(length/2)
    for j in xrange(length/2):
        if nodes[2*j] < nodes[2*j+1]:
            chrom[j] = nodes[2*j+1]/2
        else:
            chrom[j] = -nodes[2*j]/2

    return chrom

def form_answ(chrom):
    for i in xrange(len(chrom)):
        if chrom[i] > 0:
            chrom[i] = "+" + str(chrom[i])
        else:
            chrom[i] = str(chrom[i])

    answ = "(" + " ".join(chrom) + ")"
    print answ

if __name__ == "__main__":
    nodes = read_data("in.txt")
    form_answ(cycle_to_chrom(nodes))


