

def is_palindrome(seq):
    """
    Takes sequence (string) as input and checks if it is a palindrome.

    >>> is_palindrome("AAAGTTGAAA")
    The sequence is a palindrome

    >>> is_palindrome("ATGGGG")
    The sequence is no palindrome


    :param seq: Sequence as string
    :return: check if sequence is palindromic or not
    """
    seq_rev=seq[::-1]
    if seq==seq_rev:
        print("The sequence is a palindrome")
    else:
        print("The sequence is no palindrome")




import doctest
doctest.testmod(verbose=True)
