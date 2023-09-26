def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap = to_swap.upper()
    phrase_list = list(phrase)
    for index in range(len(phrase_list)):
        if phrase_list[index] == to_swap:
            phrase_list[index] = phrase_list[index].lower()
        elif phrase_list[index] == to_swap.lower():
            phrase_list[index] = phrase_list[index].upper()
    return "".join(phrase_list)
