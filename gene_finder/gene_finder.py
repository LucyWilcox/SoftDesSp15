# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Lucy Wilcox

"""

# you may find it useful to import these variables (although you are not required to use them)
#from amino_acids import aa, codons, aa_table
import random
from load import load_seq
from amino_acids import aa_table
dna = load_seq("./data/X73525.fa")


def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T') # I just decided to test everything that should be a nucleotide
    'A'
    >>> get_complement('G')
    'C'
    """
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



def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
        This seems like sufficent testing...
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    full_complement = ""
    for i in range(len(dna)):
        new_complement = get_complement(dna[i])
        full_complement = new_complement + full_complement

    return full_complement


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    >>> rest_of_ORF("ATGGGTAGCCCC")   #tests off frame stop to make sure it does not stop and makes sure it returns the whole thing if no stop
    'ATGGGTAGCCCC'
    """
    stop = ("TAG", "TAA", "TGA")
    a = 0
    end_of_ORF = len(dna)

    while a < len(dna):
        if dna[a:a+3] in stop:
            end_of_ORF = a
            return dna[0:end_of_ORF]
        else:
            a += 3

    return dna[0:end_of_ORF]
 


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    >>> find_all_ORFs_oneframe("CCGATGGGGAGATTTTAAGC") #makes sure it works if it doesn't start with ATG
    ['ATGGGGAGATTT']
    >>> find_all_ORFs_oneframe('ATGCCCATGTAG') #tests to makes sure nested ORFs are not listed
    ['ATGCCCATG']
    """
    a = 0
    dna_ORFs = []

    while a < len(dna):
        if dna[a:a+3] == "ATG":
            ORF = rest_of_ORF(dna[a:])
            dna_ORFs.append(ORF)
            a += len(ORF)
        else:
            a += 3

    return dna_ORFs



def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    >>> find_all_ORFs("ATGCATGAAATGAGGTAAAAGTAG") # actually tests to make sure nested sequences are not printed
    ['ATGCATGAAATGAGG', 'ATGAAA']
    """
    all_ORFs = []

    for i in range(3):
        all_ORFs += find_all_ORFs_oneframe(dna[i:])

    return all_ORFs


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

        this should be a good enough test, it tests both the dna and inverse and tests to check multiple reading frames
        it also makes sure nested ORFs are not counted
        
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    invert_dna = get_reverse_complement(dna)
    all_ORFs =  find_all_ORFs(dna) + find_all_ORFs(invert_dna)
    return all_ORFs


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string

        Tried to test a string with no start but doctest was unhappy with that.

    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    
    """
    ORF_list = find_all_ORFs_both_strands(dna)
    if len(ORF_list) > 1:
        return max(ORF_list, key = len)



def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF

        This is random, there is not a good way to test it.
        """
    random_dna_list =  []

    for i in range(num_trials):
        random_dna =  shuffle_string(dna)
        if random_dna != None:
            random_dna_list.append(longest_ORF(random_dna))

    longest = max(random_dna_list, key = len)
    return len(longest)
    


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        This is good, because it's heavily specified already.

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    length = len(dna)
    a = 0
    amino_acids = ''   

    while a < length - 2:
            amino_acids = amino_acids + aa_table[dna[a:a + 3]]
            a += 3

    return amino_acids

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
        >>> gene_finder("ATGCGAATGTAGCATCAAA", 10) 
        ['MLHSH']
        >>> gene_finder("ATGCGAATGTAGCATCAAA", 30)
        []
    """
    ORFs = find_all_ORFs_both_strands(dna)
    sig_AAs = []

    for entry in ORFs:
        if len(entry) > threshold:
            AA = coding_strand_to_AA(entry)
            sig_AAs.append(AA)

    return sig_AAs




if __name__ == "__main__":
    import doctest
    doctest.testmod()

    threshold_length = longest_ORF_noncoding(dna, 1500)
    print gene_finder(dna, threshold_length)
