def dig_pow(n, p):

    pow_n =  sum([ int(i) ** x for x,i in enumerate(str(n), p) ])

    return pow_n / n if pow_n % n == 0 else -1

print(dig_pow(46288, 3))
