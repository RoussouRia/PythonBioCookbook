

def concatenate_two_sequences(seq1, seq2):
    """
    Returns a joined sequence from the two given.

    :param seq1: the first sequence (a string)
    :param seq2: the second sequence  (a string)
    :return: the concatenated sequence (a string)

    Examples:

    >>> concatenate_two_sequences("AA", "CC")
    'AACC'

    >>> concatenate_two_sequences("AGC", "ATC")
    'AGCATC'
    """
    new_seq = seq1 + seq2
    return new_seq



import doctest
doctest.testmod()
