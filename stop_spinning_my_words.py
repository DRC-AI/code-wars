#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.


def spin_words(sentence):
    spinned_words = [word[::-1] if len(word) >= 5 else word for word in sentence.split(' ')]
    return ' '.join(spinned_words)
    

spinned_words = spin_words('Hey fellow warriors')
print(spinned_words)
