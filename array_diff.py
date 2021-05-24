def array_diff(a,b):
    diff = [ i for i in a if i not in b ]
    return diff

print(array_diff([1,2], [2]))

