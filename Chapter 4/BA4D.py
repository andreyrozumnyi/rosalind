""" Compute the Number of Peptides of Given Total Mass """


keys = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
def calc_varinats(m):
    ways = [0]*(m + 1)
    index = m
    ways[m] = 1
    while index > 0:
        for key in keys:
            ways[index-key] += ways[index]

        index -= 1
        while ways[index] == 0:
            index -= 1

    print ways[0]

if __name__ == "__main__":
    calc_varinats(1251)

