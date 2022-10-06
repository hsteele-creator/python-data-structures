def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dict_one = {}
    dict_two = {}
    
    for i in str(num1):
        dict_one[i] = i
    for i in str(num2):
        dict_two[i] = i
    return dict_one == dict_two