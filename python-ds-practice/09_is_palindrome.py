def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    spaceless_phrase_list = [item for item in phrase if item != " "]
    spaceless_phrase_list.reverse()

    spaceless_original = [item for item in phrase if item != " "]

    return "".join(spaceless_phrase_list) == "".join(spaceless_original).upper()

# use replace and slice