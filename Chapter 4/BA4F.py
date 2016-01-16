""" Compute the Score of a Cyclic Peptide Against a Spectrum """


def create_peptide_mass_dict():
    peptide_mass = dict()
    peptide_mass["G"] = 57
    peptide_mass["A"] = 71
    peptide_mass["S"] = 87
    peptide_mass["P"] = 97
    peptide_mass["V"] = 99
    peptide_mass["T"] = 101
    peptide_mass["C"] = 103
    peptide_mass["I"] = 113
    peptide_mass["L"] = 113
    peptide_mass["N"] = 114
    peptide_mass["D"] = 115
    peptide_mass["K"] = 128
    peptide_mass["Q"] = 128
    peptide_mass["E"] = 129
    peptide_mass["M"] = 131
    peptide_mass["H"] = 137
    peptide_mass["F"] = 147
    peptide_mass["R"] = 156
    peptide_mass["Y"] = 163
    peptide_mass["W"] = 186

    return peptide_mass


def read_data_from(fileName):
    with open(fileName) as file:
        peptide = file.readline().strip()
        spectrum = file.readline().strip().split()

    for i in xrange(len(spectrum)):
        spectrum[i] = int(spectrum[i])

    return peptide, spectrum


def circular_string(start, length, string):
    if start >= len(string):
        return

    if start + length <= len(string):
        return string[start: start + length]
    else:
        answer = string[start:]
        answer += string[:(start + length) % (len(string))]
        return answer


def peptide_mass(peptide, masses):
    mass = 0
    for i in xrange(len(peptide)):
        mass += masses[peptide[i]]

    return mass


def generate_spectrum(peptide):
    masses = create_peptide_mass_dict()
    spectrum = [0]
    chank_len = 1
    peptide_len = len(peptide)
    while chank_len < len(peptide):
        start = 0
        while start < peptide_len:
            spectrum.append(peptide_mass(circular_string(start, chank_len, peptide), masses))
            start += 1

        chank_len += 1

    spectrum.append(peptide_mass(peptide, masses))
    return sorted(spectrum)


def score(theoret_spect, exper_spect):
    score = 0
    for item in theoret_spect:
        if item in exper_spect:
            score += 1
            exper_spect.remove(item)

    print score
    return score


if __name__ == "__main__":
    peptide, exp_spect = read_data_from("in")
    theor_spect = generate_spectrum(peptide)
    score(theor_spect, exp_spect)
