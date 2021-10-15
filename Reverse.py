def reverse(seq):
    """
    Reverses and outputs the input sequence
    :param seq: input sequence
    :return: reversed input sequence

    >>> reverse("ATG")
    'GTA'
    >>> reverse("ATCTGT")
    'TGTCTA'
    """

    seq_reverse = seq[::-1]
    return seq_reverse

import doctest
doctest.testmod(verbose=True)