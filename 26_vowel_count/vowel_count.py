def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = "aeiou"
    vowels_dict = {}.fromkeys(vowels, 0)
    for letter in phrase:
        if letter in vowels:
            vowels_dict[letter] += 1
        elif letter in vowels.upper():
            vowels_dict[letter.lower()] += 1
    return vowels_dict


