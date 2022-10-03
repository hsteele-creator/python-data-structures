def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    upper = to_swap.upper()
    lower = to_swap.lower()
    new_string = ""

    for char in phrase:
        if char == upper or char == lower:
            new_string += char.swapcase() 
        else:
             new_string += char
    return new_string

    # 1. check if swap char is lower caser - if so check if char is equal to
        

    




        # if to_swap.islower():
        #     if char == to_swap:
        #         char.upper()
        #     elif char == to_swap.upper():
        #         char.lower()
        # elif to_swap.isupper():
        #     if char == to_swap:
        #         char.lower()
        #     elif char == to_swap.lower():
        #         char.upper()
        # return phrase
