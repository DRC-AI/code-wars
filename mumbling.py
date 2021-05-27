#This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    
    output = []
    increment = 1

    for letter in s:
        output.append(letter * increment)
        increment += 1

    print(str('-'.join(output).title()))




accum("ZpglnRxqenU")
