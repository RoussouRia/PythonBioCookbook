
def save_to_file(filename, data):
    """
        Return a long sequence from the given sequence list.
        :param seqs: A list object with multiple sequences as strings.
        :return: A concentrated sequence as a string.

        Examples


        >>> save_to_file("2i2", "454")
        >>> print open("2i2", "r").read()
        True


        """

    with open(filename, "w") as file:
        file.write(data)

    file.close()

import doctest
doctest.testmod()
