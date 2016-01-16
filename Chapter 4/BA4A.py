""" Translate an RNA String into an Amino Acid String """

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

def read_data_from(file_name):
    with open(file_name, 'r') as file:
        rna = file.readline().strip()

    return rna

def write_to_file(fileName, peptide):
    with open(fileName, 'w+') as file:
        file.write(peptide)

def rna_to_peptide(rna):
    peptide = ''
    lookup_dict = create_lookup()

    for start in xrange(0, len(rna) - 2, 3):
        if lookup_dict[rna[start: start + 3]] == "*":
            break

        peptide += lookup_dict[rna[start: start + 3]]

    write_to_file("out", peptide)
    return peptide

if __name__ == "__main__":
    rna = read_data_from("in")
    rna_to_peptide(rna)
