"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

from itertools import permutations
# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# Your code here
z = q * 2
perm = list(permutations(z, 2))
l = []
for each in perm:
    add = 0
    sub = 0
    for i in perm:
        add = f(i[0]) + f(i[1])
        for j in perm:
            sub = f(j[0]) - f(j[1])
            if add == sub:
                k = str(i[0]) + '_' + str(i[1]) + '_' + \
                    str(j[0]) + '_' + str(j[1])
                if k not in l:
                    l.append(k)
                    print(
                        f"f({i[0]}) + f({i[1]}) = f({j[0]}) - f({j[1]})       {f(i[0])} + {f(i[1])} = {f(j[0])} - {f(j[1])}")
