class DNASequence(object):
    """ Represents a sequence of DNA """
    def __init__(self, nucleotides):
        """ constructs a DNASequence with the specified nucleotides.
             nucleotides: the nucleotides represented as a string of
                          capital letters consisting of A's, C's, G's, and T's """
        self.seq = nucleotides
 
    def __str__(self):
        """ Returns a string containing the nucleotides in the DNASequence
        >>> seq = DNASequence("TTTGCC")
        >>> print seq
        TTTGCC
        """
        return self.seq

    def get_reverse_complement(self):
        """ Returns the reverse complement DNA sequence represented
            as an object of type DNASequence

            >>> seq = DNASequence("ATGC")
            >>> rev = seq.get_reverse_complement()
            >>> print rev
            GCAT
            >>> print type(rev)
            <class '__main__.DNASequence'>
        """
        def get_complement(nucleotide):
            if nucleotide == 'A':
                nucleotide_complement = 'T'
                return nucleotide_complement
            elif nucleotide == 'T':
                nucleotide_complement = 'A'
                return nucleotide_complement
            elif nucleotide == 'C': 
                nucleotide_complement = 'G'
                return nucleotide_complement
            elif nucleotide == 'G':
                nucleotide_complement = 'C'
                return nucleotide_complement
            else:
                return "error"

        seq = self.seq
        full_complement = ""
        for i in range(len(seq)):
            new_complement = get_complement(seq[i])
            full_complement = new_complement + full_complement

        self.rev = DNASequence(full_complement)
        return self.rev


    def get_proportion_ACGT(self):
        """ Computes the proportion of nucleotides in the DNA sequence
            that are 'A', 'C', 'G', and 'T'
            returns: a dictionary where each key is a nucleotide and the
                corresponding value is the proportion of nucleotides in the
            DNA sequence that are that nucleotide.
            (NOTE: this doctest will not necessarily always pass due to key
                    re-ordering don't worry about matching the order)
        >>> seq = DNASequence("AAGAGCGCTA")
        >>> d = seq.get_proportion_ACGT()
        >>> print (d['A'], d['C'], d['G'], d['T'])
        (0.4, 0.2, 0.3, 0.1)
        """
        seq = self.seq
        length =float(len(seq))
        d = dict()
        for letter in seq:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1

        for key, value in d.items():
            d[key] = value/length

        return d



if __name__ == '__main__':
    import doctest
    doctest.testmod()
