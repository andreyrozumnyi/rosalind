""" Find All Occurrences of a Collection of Patterns in a String """

from collections import defaultdict

def read_data(file_name):
    with open(file_name, 'r') as file:
        text = file.readline().rstrip()
        patterns = []
        try:
            while True:
                patterns.append(next(file).rstrip())
        except StopIteration:
            return text, patterns

def find_all_occur(text, patterns):
    oc_pos = defaultdict(list)
    pat_len = len(patterns[0])
    text_len = len(text)
    start = 0
    while start + pat_len <= text_len:
        oc_pos[text[start:start+pat_len]].append(start)
        start += 1

    positions = []
    for pattern in patterns:
        positions += oc_pos[pattern]

    return sorted(positions)

if __name__ == "__main__":
    text, patterns = read_data("in.txt")
    posittions = find_all_occur(text, patterns)
    for pos in posittions:
        print pos,