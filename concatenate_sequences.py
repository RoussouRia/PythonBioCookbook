def concatenate_sequences(seqs):
    """
    Return a long sequence from the given sequence list.
    :param seqs: A list object with multiple sequences as strings.
    :return: A concentrated sequence as a string.

    Examples

    >>> concatenate_sequences(['AA', 'U', 'CC', 'G'])
    'AAUCCG'

    >>> concatenate_sequences(['aucg', 'AUCG'])
    'aucgAUCG'
    """
    all_seqs = ''
    for seq in seqs:
        all_seqs += seq
    return all_seqs

import doctest
doctest.testmod()

