#You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.



def longest_consec(strarr, k):
    string = []
    s = 0
    if not strarr:
        return ''
    while k <= len(strarr):
        long_string = [ strarr[i] for i in range(s,k) ]
        string.append(''.join(long_string))
        k += 1 
        s += 1
    return max(string, key = len) if string else ''

print( longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
