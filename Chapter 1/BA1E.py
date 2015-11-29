"""
Find Patterns Forming Clumps in a String

Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome
if there is an interval of Genome of length L in which Pattern appears at least t times.
"""

def occur_numb(string, sub):
    """
    :param string: string for finding number of occurences of pattern
    :param sub: pattern
    :return: how many times pattern occurs inside the string
    """
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count

def get_clumps(k, L, t, data):
    """ return patterns forming clumps in a string """

    start = 0
    answer = set()
    data_len = len(data)
    while start + L <= data_len:
        substr_dict = {}
        window = data[start:start + L]
        sub_start = 0
        wind_len = len(window)
        while sub_start + k <= wind_len:
            sub = window[sub_start:sub_start + k]
            if sub not in substr_dict:
                substr_dict[sub] = 1
            else:
                substr_dict[sub] += 1

            sub_start += 1

        start += 1
        answer_list = [key for key in substr_dict.keys() if substr_dict[key] >= t]
        for item in answer_list:
            answer.add(item)

    for item in answer:
        print item,

    return answer

def read_data_from(file_name):
    with open(file_name, "r") as file:
        string = file.readline().strip()
        k, L, t = file.readline().strip().split()

    return string, int(k), int(L), int(t)

if __name__ == "__main__":
    string, k, L, t = read_data_from("in.txt")
    get_clumps(k, L, t, string)