def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # phrase = phrase.lower()

    # titleized = ""
    # for word in phrase.split():
    #     titleized = titleized + word.capitalize() + " "

    # return titleized[:-1]

    return phrase.title()