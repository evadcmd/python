from collections.abc import Iterator, Iterable

l = []
print(isinstance(l, Iterable), isinstance(l, Iterator))

print(dir(l))

def gen():
    for i in range(10):
        yield i

print(isinstance(gen, Iterable), isinstance(gen, Iterator))
#false false

g = gen()
print(isinstance(g, Iterable), isinstance(g, Iterator))
# true true
