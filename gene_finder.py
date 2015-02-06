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



def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide

        If the dna only has A, T, G, and C this should really be enough
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    a = 'A'
    t = 'T'
    c = 'C'
    g = 'G'


    if nucleotide == a:
        nucleotide_complement = t
        return nucleotide_complement
    elif nucleotide == t:
        nucleotide_complement = a
        return nucleotide_complement
    elif nucleotide == c:
        nucleotide_complement = g
        return nucleotide_complement
    elif nucleotide == g:
        nucleotide_complement = c
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
    for i in range(0, len(dna)):
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
    length = len(dna)
    i = 0
    a = 0
    b = 3
    end = length


    while i < length:
        if dna[a:b] in stop:
            end = a
            return dna[0:end]
        else:
            i += 1
            a += 3
            b += 3
            
    return dna[0:end]
 


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
    """

    length = len(dna)
    a = 0
    b = 3

    dna_ORFs = []

    while a < length:
        if dna[a:b] == "ATG":
            ORF = rest_of_ORF(dna[a:])
            dna_ORFs.append(ORF)
            a += len(ORF)
            b += len(ORF)
        else:
            a += 3
            b += 3

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

    i = 0

    for i in range(0,3):
        all_ORFs += find_all_ORFs_oneframe(dna[i:])
        i += 1

    return all_ORFs


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    all_ORFs = find_all_ORFs(dna)

    invert_dna = get_reverse_complement(dna)

    all_ORFs += find_all_ORFs(invert_dna)

    return all_ORFs



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """

    ORF_list = find_all_ORFs_both_strands(dna)
    return max(ORF_list, key = len)



def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    random_dna_list =  []

    for i in range(num_trials):
        print i
        random_dna =  shuffle_string(dna)
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

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    length = len(dna)
    a = 0
    b = 3

    amino_acids = ''   

    while b < length+1:
            amino_acids = amino_acids + aa_table[dna[a:b]]
            a += 3
            b += 3

    return amino_acids

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """


    # TODO: implement this
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#the_dna = load_seq
threshold_length = longest_ORF_noncoding("ATGCCCGCTTT", 1500)
print threshold_length
#gene_finder(the_dna, threshold_length)

#print coding_strand_to_AA("ATGCCCGCTTT")
