""" Matching Random Motifs """

def rnd_str_probability(x, string):
        probabilities = dict()
        probabilities["G"] = 1.0*x / 2
        probabilities["C"] = 1.0*x / 2
        probabilities["A"] = 1.0*(1 - x) / 2
        probabilities["T"] = 1.0*(1 - x) / 2
        prob = 1
        length = len(string)
        for i in xrange(length):
            prob *= probabilities[string[i]]

        return prob

def main(N, x, string):
    print "%.3f" % (1 - (1 - rnd_str_probability(x, string))**N)

if __name__ == "__main__":
    main(97329, 0.459759, "GAATAATG")