def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # TODO: swapcase
    to_swap = to_swap.upper()
    phrase_list = list(phrase)

    return "".join([letter.swapcase() if letter.upper() == to_swap else letter
                    for letter in phrase_list])

    # for index in range(len(phrase_list)):
    #     if phrase_list[index].upper() == to_swap:
    #         phrase_list[index] = phrase_list[index].swapcase()

    # return "".join(phrase_list)
