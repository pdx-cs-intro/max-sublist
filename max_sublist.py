# Find the maximum-scoring sublist of a given list.
# Bart Massey 2021

def slice_score(slice):
    """Compute the score of a given list by
    summing its elements.
    """
    score = 0
    for v in slice:
        score += v
    return score

def max_sublist(source):
    """Return the maximum-scoring slice of source.

    >>> max_sublist([6, -5, 7, -5, 2])
    [6, -5, 7]
    """
    nsource = len(source)
    max_score = 0
    max_slice = []
    for n in range(1, nsource):
        for i in range(nsource):
            if i + n > nsource:
                break
            slice = source[i:i+n]
            score = slice_score(slice)
            if score > max_score:
                max_score = score
                max_slice = slice
    return max_slice

if __name__ == "__main__":
    import doctest, random

    doctest.testmod()

    # Make a random list of n values.
    def random_source(n):
        result = []
        for _ in range(n):
            result.append(random.randrange(-100, 101))
        return result

    # Check the identity that reversing the list just gives
    # the maximum slice backward. Also check that the score
    # is always ≥ 0, since the empty slice is minimal.
    for _ in range(100):
        source = random_source(100)
        slice_forward = max_sublist(source)
        slice_reverse = max_sublist(list(reversed(source)))
        assert slice_forward == list(reversed(slice_reverse))
        assert slice_score(slice_forward) >= 0
