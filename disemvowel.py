Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.



def disemvowel(string_):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    big_vowels = list(map(str.upper, vowels))
        
    for  ele in vowels + big_vowels:
        string_ = string_.replace(ele , "")
        
    return string_

print(disemvowel('I like pankakes!'))
