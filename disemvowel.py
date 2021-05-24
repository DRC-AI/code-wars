def disemvowel(string_):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    big_vowels = list(map(str.upper, vowels))
        
    for  ele in vowels + big_vowels:
        string_ = string_.replace(ele , "")
        
    return string_

print(disemvowel('I like pankakes!'))
