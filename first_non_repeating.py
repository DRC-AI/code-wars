#Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

#For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

#As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.


def first_non_repeating_letter(string):

    if not string:
        return ''
    for i in string.lower():
        if string[string.index(i)].lower() not in string[:string.index(i)].lower() + string[string.index(i)+1:].lower():
            return i
    return ''

letter = first_non_repeating_letter( '' )

print(letter)
