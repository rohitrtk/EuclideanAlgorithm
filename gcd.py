import sys


def gcd(a: int, b: int):

    # Checks if a >= b, if not, fix
    if b > a:
        t = a
        a = b
        b = t

    # Quotient q equal to integer division of a and b
    q = a // b

    # Remainder r equal to the difference of a and the quotient times b
    r = a - (q * b)

    print('%d = %d * %d + %d' % (a, q, b, r))

    # If there's no more remainders we've found the gcd
    if r == 0:
        return b

    return gcd(b, r)


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Invalid arguments, expecting an integer A and an integer B')
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print('GCD of %d & %d is %d' % (x, y, gcd(x, y)))



