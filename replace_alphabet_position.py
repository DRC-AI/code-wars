def alphabet_position(text):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index = range(1,len(alphabet))
    index_number ="" 
    alpha_index = dict(zip(alphabet,index))

    for l in text.lower():index_number = index_number + str(alpha_index.get(l,''))

    print(index_number)
    
alphabet_position("The sunset sets at twelve o' clock.")
