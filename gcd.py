import sys

silent_gcd = False

# List of 2 tuple values (quotient, remainder) to
# be used for back substitution
a_values = []

'''
Finds the greatest common denominator of 2 integers a & b
'''
def gcd(a: int, b: int, silent=False):

    # Makes sure a >= b
    if b > a:
        a, b = b, a

    # Quotient q equal to integer division of a and b
    q = a // b

    # Remainder r equal to the difference of a and the quotient times b
    r = a % b

    if not silent:
        print('%d = %d * %d + %d' % (a, q, b, r))

    # If there's no more remainders we've found the gcd
    if r == 0:
        return b

    a_values.append((q, r))

    return gcd(b, r, silent)


def bezout(lst):
    raise NotImplementedError()


# Usage: python gcd.py 321 47 [-s]
if __name__ == '__main__':

    arg_len = len(sys.argv)

    if arg_len < 3 or arg_len > 4:
        print('Invalid arguments, expecting an integer A and an integer B')
        exit(0)

    if arg_len == 4:
        if sys.argv[3] == '-s':
            silent_gcd = True
        else:
            print('Invalid flag %s' % sys.argv[3])
            exit(0)

        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print('GCD of %d & %d is %d' % (x, y, gcd(x, y, silent_gcd)))

        bezout(a_values)


