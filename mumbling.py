def accum(s):
    
    output = []
    increment = 1

    for letter in s:
        output.append(letter * increment)
        increment += 1

    print(str('-'.join(output).title()))




accum("ZpglnRxqenU")
