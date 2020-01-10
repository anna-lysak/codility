
def minmax(a):
    firstElem = True

    x = 0
    y = 0
    for i in a:
        if firstElem:
            x = i
            y = i
            firstElem = False
        if x > i:
            x = i
        if y < i:
            y = i

    return x, y


def sum_squares(n):

    if n > 0:
        return sum([i*i for i in range(1,n) if i % 2 != 0])
    else:
        return 0


def pow_list(base, n):
    pow_lst = []
    step = 1 if n > 0 else -1
    if n == 0:
        return [1]

    for i in range(step, n+step, step):
        m = base
        for j in range(step, i, step):
            m = m * base

        pow_lst.append(m if step > 0 else 1 / m)
    return pow_lst


def product_distinct_pairs(a):

    c = [] # result array
    d = [] # indexes
    indexI = 0
    indexJ = 0

    for i in a:
        for j in a:
            if indexJ == indexI or indexI in d or indexJ in d or (i, j) in c or (j, i) in c:
                indexJ += 1
                continue
            if i * j % 2 != 0:
                c.append((i, j))
                d.append(indexI)
                d.append(indexJ)
                break
            indexJ += 1
        indexJ = 0
        indexI += 1

    return c


def distinct_numbers(a):
    res = []
    for i in a:
        if i not in res:
            res.append(i)
    return res


def progression():
    def gen():
        a = 0
        n = 0
        yield n
        while n < 90:
            a = a + 2  # a = 2 a = 4
            n = n + a  # n = 2 n = 6
            yield n

    return [i for i in gen()]


def symbols():
    return [chr(i) for i in range(97, 97+26)]  # symbols from a to z


class IndexOutOfBounds(Exception):
    pass


def replace_by_index(a, i, val):
    if i >= len(a):
        raise IndexOutOfBounds('%s out of bounds' % i)
    a[i] = val
    return a


def factors(n):  # generator that computes factors
    k = 1
    while k*k < n:  # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k*k == n:  # special case if n is perfect square
        yield k


# n-th root: val ** (1/n), example 8 ** (1/3) = 2.0


def alphabet_frequencies(f = 'text.txt'):
    try:
        fp = open(f)
        d = dict()
        for i in fp:
            print(i)
            for j in i:
                if ord(j) in range(97, 97+26):
                    if j in d.keys():
                        d[j] += 1
                    else:
                        d[j] = 1
        fp.close()
        print(d)
    except (FileNotFoundError, IOError) as e:
        print("File not found.", e)


def max_recursive(S, max=0, i=0):
    if S[i] >= max:
        max = S[i]
    if i >= len(S) - 1:
        return max
    else:
        return max_recursive(S, max, i+1)


def unique(A, start=0):
    if start >= len(A) - 1:
        return True

    for i in range(start+1, len(A)):
        if A[start] == A[i]:
            return False

    return unique(A, start+1)


def my_sum():
    a = [[1, 1], [2, 2], [3, 3]]
    print([y for y in [x for x in a]])
    return sum([sum(y) for y in a])


def palindrome(s):
    n = 0
    while n < (len(s) - 1)/2:
        if s[n] == s[len(s)-1 - n]:
            n += 1
            continue
        else:
            return False
    return True


def palindrome_rec(s, n=0):
    if n < (len(s) - 1)/2:
        if s[n] == s[len(s)-1 - n]:
            n += 1
            return palindrome_rec(s, n)
        else:
            return False
    return True


