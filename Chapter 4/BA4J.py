""" Generate the Theoretical Spectrum of a Linear Peptide """


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


def read_data_from(file_name):
    with open(file_name) as file:
        data = file.readline().strip()

    return data


def write_data_to(file_name, masses):
    with open(file_name, 'w+') as file:
        for i in xrange(len(masses)):
            file.write("%d " % (masses[i]))


def get_peptide_mass(peptide, masses):
    mass = 0
    for i in xrange(len(peptide)):
        mass += masses[peptide[i]]

    return mass


def gen_spectrum(peptide):
    masses = create_peptide_mass_dict()
    spectrum = [0]
    chank_len = 1
    peptide_len = len(peptide)
    while chank_len < len(peptide):
        start = 0
        while start + chank_len <= peptide_len:
            spectrum.append(get_peptide_mass(peptide[start:start+chank_len], masses))
            start += 1
        chank_len += 1

    spectrum.append(get_peptide_mass(peptide, masses))
    write_data_to("out", sorted(spectrum))


if __name__ == "__main__":
    peptide = read_data_from("in")
    gen_spectrum(peptide)
