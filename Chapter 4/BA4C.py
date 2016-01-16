""" Generate the Theoretical Spectrum of a Cyclic Peptide """


def create_peptide_mass_dict():
    peptideMass = dict()
    peptideMass["G"] = 57
    peptideMass["A"] = 71
    peptideMass["S"] = 87
    peptideMass["P"] = 97
    peptideMass["V"] = 99
    peptideMass["T"] = 101
    peptideMass["C"] = 103
    peptideMass["I"] = 113
    peptideMass["L"] = 113
    peptideMass["N"] = 114
    peptideMass["D"] = 115
    peptideMass["K"] = 128
    peptideMass["Q"] = 128
    peptideMass["E"] = 129
    peptideMass["M"] = 131
    peptideMass["H"] = 137
    peptideMass["F"] = 147
    peptideMass["R"] = 156
    peptideMass["Y"] = 163
    peptideMass["W"] = 186

    return peptideMass


def read_data_from(file_name):
    with open(file_name) as file:
        data = file.readline().strip()

    return data


def write_data_to(fileName, masses):
    with open(fileName, 'w+') as file:
        for i in xrange(len(masses)):
            file.write("%d " % (masses[i]))


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
    write_data_to("out", sorted(spectrum))


if __name__ == "__main__":
    peptide = read_data_from("in")
    generate_spectrum(peptide)
