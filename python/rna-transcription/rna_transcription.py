def to_rna(dna_strand):
    for nucleotide in dna_strand:
        if nucleotide == 'G':
            dna_strand = dna_strand.replace('G', 'C')
        elif nucleotide == 'C':
            dna_strand = dna_strand.replace('C', 'G')
        elif nucleotide == 'A':
            dna_strand = dna_strand.replace('A', 'U')
        elif nucleotide == 'T':
            dna_strand = dna_strand.replace('T', 'A')
    return dna_strand
