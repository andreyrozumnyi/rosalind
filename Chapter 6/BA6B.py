""" Compute the Number of Breakpoints in a Permutation """

def read_data(file_name):
    with open(file_name, 'r') as file:
        line = file.readline().strip().split()

    length = len(line)
    line[0] = line[0].replace("(", "")
    line[length-1] = line[length-1].replace(")", "")
    for i in xrange(len(line)):
        line[i] = int(line[i])

    line = [0] + line + [length+1]
    return line

def br_points_num(data):
    num = 0
    length = len(data)
    for i in xrange(length-1):
        if data[i] == data[i+1] - 1:
            continue
        else:
            num += 1

    print num

if __name__ == "__main__":
    data = read_data("in.txt")
    br_points_num(data)