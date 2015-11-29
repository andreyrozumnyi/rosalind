"""
Find All Occurrences of a Pattern in a String
"""

def occurrences(genome, sub):
    """
    :param genome: genome for processing
    :param sub: pattern for which we find indexes of occurnces
    :return: list of indexes
    """
    start = 0
    indexes = []
    while True:
        start = genome.find(sub, start)
        if start > 0:
            indexes.append(start)
        else:
            break

        start += 1

    return indexes

def read_data_from(file_name):
    with open(file_name, "r") as file:
        pattern = file.readline().strip()
        genome = file.readline().strip()

    return genome, pattern

if __name__ == "__main__":
    genome, pattern = read_data_from("in.txt")
    indexes = occurrences(genome, pattern)
    for ind in indexes:
        print ind,