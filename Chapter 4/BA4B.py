""" Find Substrings of a Genome Encoding a Given Amino Acid String """


def create_lookup():
    codons = dict()
    # AXX
    codons['AUG'] = 'M'
    codons['AUA'] = 'I'
    codons['AUC'] = 'I'
    codons['AUU'] = 'I'
    codons['AGG'] = 'R'
    codons['AGA'] = 'R'
    codons['AGC'] = 'S'
    codons['AGU'] = 'S'
    codons['ACG'] = 'T'
    codons['ACA'] = 'T'
    codons['ACC'] = 'T'
    codons['ACU'] = 'T'
    codons['AAG'] = 'K'
    codons['AAA'] = 'K'
    codons['AAC'] = 'N'
    codons['AAU'] = 'N'
    #CXX
    codons['CAU'] = 'H'
    codons['CAC'] = 'H'
    codons['CAA'] = 'Q'
    codons['CAG'] = 'Q'
    codons['CCU'] = 'P'
    codons['CCC'] = 'P'
    codons['CCA'] = 'P'
    codons['CCG'] = 'P'
    codons['CGU'] = 'R'
    codons['CGC'] = 'R'
    codons['CGA'] = 'R'
    codons['CGG'] = 'R'
    codons['CUU'] = 'L'
    codons['CUC'] = 'L'
    codons['CUA'] = 'L'
    codons['CUG'] = 'L'
    #GXX
    codons['GAU'] = 'D'
    codons['GAC'] = 'D'
    codons['GAA'] = 'E'
    codons['GAG'] = 'E'
    codons['GCU'] = 'A'
    codons['GCC'] = 'A'
    codons['GCA'] = 'A'
    codons['GCG'] = 'A'
    codons['GGU'] = 'G'
    codons['GGC'] = 'G'
    codons['GGA'] = 'G'
    codons['GGG'] = 'G'
    codons['GUU'] = 'V'
    codons['GUC'] = 'V'
    codons['GUA'] = 'V'
    codons['GUG'] = 'V'
    #UXX
    codons['UAU'] = 'Y'
    codons['UAC'] = 'Y'
    codons['UAA'] = '*'
    codons['UAG'] = '*'
    codons['UCU'] = 'S'
    codons['UCC'] = 'S'
    codons['UCA'] = 'S'
    codons['UCG'] = 'S'
    codons['UGU'] = 'C'
    codons['UGC'] = 'C'
    codons['UGA'] = '*'
    codons['UGG'] = 'W'
    codons['UUU'] = 'F'
    codons['UUC'] = 'F'
    codons['UUA'] = 'L'
    codons['UUG'] = 'L'

    return codons


def reaad_data(file_name):
    with open(file_name, 'r') as file:
        dna = file.readline().strip()
        peptide = file.readline().strip()

    return dna, peptide


def write_to(file_name, data):
    with open(file_name, 'w+') as file:
        length = len(data)
        for i in xrange(length):
            file.write("%s \n" % data[i])


def reverse_complement(dna):
    lookup_dict = {"A":"T", "C":"G", "G":"C", "T":"A"}
    reverse_compl = ""
    length = len(dna)
    for index in xrange(length):
        reverse_compl += lookup_dict[dna[index]]

    return reverse_compl[::-1]


def rna_to_peptide(rna):
    peptide = ''
    lookup_dict = create_lookup()

    for start in xrange(0, len(rna) - 2, 3):
        if lookup_dict[rna[start: start + 3]] == "*":
            break

        peptide += lookup_dict[rna[start: start + 3]]

    return peptide


def dna_to_rna(dna):
    return dna.replace("T", "U")


def rna_to_dna(rna):
    return rna.replace("U", "T")


def substrs_in_genome(dna, peptide):
    substrs = []
    rna = dna_to_rna(dna)
    complement_rna = dna_to_rna(reverse_complement(dna))
    sub_len = len(peptide)*3
    start = 0
    dna_len = len(dna)
    while start + sub_len <= dna_len:
        sub_one = rna[start: start + sub_len]
        sub_two = complement_rna[start: start + sub_len]
        if peptide == rna_to_peptide(sub_one):
            substrs.append(rna_to_dna(sub_one))

        if peptide == rna_to_peptide(sub_two):
            substrs.append(reverse_complement(rna_to_dna(sub_two)))

        start += 1

    write_to("out", substrs)


if __name__ == "__main__":
    dna, peptide = reaad_data("in")
    substrs_in_genome(dna, peptide)


