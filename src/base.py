"""Changing bases."""

digits = {}

for i in range(0, 10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'


def change_to_base(n: int, b: int) -> str:
    """
    Return `n` in base `b`.

    The base `b` must be in the range 2 to 16.

    >>> change_to_base(1, 2)
    '1'
    >>> change_to_base(31, 2)
    '11111'
    >>> change_to_base(31, 8)
    '37'
    >>> change_to_base(31, 16)
    '1F'
    """


    reversed_digits = []

    quotient, remainder = abs(n), abs(n) % b

    while quotient > 0 and remainder > 0:
        reversed_digits.append(digits[remainder])
        quotient = quotient // b
        remainder = quotient % b

    assert 2 <= b <= 16

    if n == 0:
        return '0'
    elif n < 0:
        return '-' + ''.join(reversed_digits[::-1]) # This seems a little cheeky...
    else:
        return ''.join(reversed_digits[::-1])  # FIXME: return n in the right base
