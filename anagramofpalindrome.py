"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""
    """
    Iterate throught string
    Store every char as a key with value of char in string
    Get values from dictionary
    If all values //2 = 0 or return True and just 1 value can be //2 != 0
    else False
    """

    maping = {}

    for char in word:
        if char not in maping:
            maping[char] = 0
        maping[char]+= 1

    values = maping.values()  

    count = 0
    for value in values:
        if value//2 != 1:
            count+= 1
        if count > 1:
            return False
    return True             


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
