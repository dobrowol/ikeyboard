from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subsets(s):
    return map(set, powerset(s))

def partition(iterable, chain=chain, map=map):
    #s = iterable if hasattr(iterable, '__getslice__') else tuple(iterable)
    n = len(iterable)
    first, middle, last = [0], range(1, n), [n]
   
    return [map( chain(first, div), chain(div, last))
            for i in range(n) for div in combinations(middle, i)]
    
n = input()
k,l = input().split(' ')
keys = input()
alphabet = input()
F = []
l = int(l)
while( l >  0):
    F.append(int(input()))
    l -= 1
from pprint import pprint
alpart = partition("1234")

for a in alpart:
    for b in a:
        print (b)
    