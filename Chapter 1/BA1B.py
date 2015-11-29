"""
Find the most frequent k-mers in a string.
"""

from collections import Counter

def most_freq_kmer(string, k):
    """
    :param string: string for finding most frequent occurences
    :param k: length of kmers
    :return: list of words of length k which are most frequent in the string
    """
    substrs = list()
    start = 0
    length = len(string)
    while start + k <= length:
        sub = string[start:start+k]
        start += 1
        substrs.append(sub)

    if not substrs:
        return []

    stat = Counter(substrs)
    occur_and_kmer = zip(stat.values(), stat.keys())
    occur_and_kmer.sort(reverse=True)
    dif_kmers_num = len(occur_and_kmer)
    most_freq_times = occur_and_kmer[0][0]
    i = 0
    answer = []
    while (i < dif_kmers_num) and (occur_and_kmer[i][0] == most_freq_times):
        answer.append(occur_and_kmer[i][1])
        i += 1

    return answer

def read_data_from(file_name):
    """
    :param file_name: input file
    :return: string: string for proccessing; k: length of substring
    """
    with open(file_name, "r") as file:
        string = file.readline().strip()
        k = int(file.readline().strip())

    return string, k

if __name__ == "__main__":
    string, k = read_data_from("in.txt")
    answer = most_freq_kmer(string, k)
    for elem in answer:
        print elem,