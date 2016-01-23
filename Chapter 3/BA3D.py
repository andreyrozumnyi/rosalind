""" Construct the De Bruijn Graph of a String """
import collections


def prefix(string):
    return string[:len(string)-1]


def suffix(string):
    return string[1:]


def build_de_bruijn(k, string, out_file):
    start = 0
    answer = {}
    while start + k <= len(string):
        window = string[start:start+k]
        pre = prefix(window)
        suf = suffix(window)
        if pre not in answer:
            answer[pre] = (suf,)
        else:
            answer[pre] += (suf,)
        start += 1

    od = collections.OrderedDict(sorted(answer.items()))
    with open(out_file, 'w+') as file:
        for key in od.keys():
            file.write(str(key) + " -> ")
            if len(answer[key]) == 1:
                file.write(answer[key][0] + "\n")
            else:
                answer[key] = sorted(answer[key])
                file.write(answer[key][0])
                del answer[key][0]
                for item in answer[key]:
                    file.write("," + str(item))

                file.write("\n")
