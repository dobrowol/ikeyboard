from itertools import chain, combinations
import sys

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subsets(s):
    return map(set, powerset(s))

def partition(iterable, chain=chain, map=map):
    s = iterable if hasattr(iterable, '__getitem__') else tuple(iterable)
    n = len(s)
    first, middle, last = [0], range(1, n), [n]
    getitem = s.__getitem__
    return [map(getitem, chain(first, div), chain(div, last))
            for i in range(n) for div in combinations(middle, i)]
    
n = int(input())
for iteration in range(0,n):
    
    numOfkeys,l = input().split(' ')
    keys = input()
    alphabet = input()
    
    l = int(l)
    numOfkeys = int(numOfkeys)
    F = {}
    for a in alphabet:
        F[a] = int(input())
    
    from pprint import pprint
    minOfSum = 9223372036854775807
    desiredCombination = []
    sb = combinations(alphabet[1:], numOfkeys-1)
    for s in sb:
        sumOfCost = F[alphabet[0]]
        i = 1
        lastLetter = alphabet[0]
        copyAlpha = alphabet[1:]
        for letter in copyAlpha:
            if letter in s:
                i = 1
                sumOfCost += F[letter]
            else:
                i += 1
                sumOfCost += i*F[letter]
        #print ("combination: ", s, "; sumOfCost: ", sumOfCost)
        
        if sumOfCost <  minOfSum:
           minOfSum = sumOfCost
           desiredCombination = s
    "Keypad #{} :".format(iteration)
    print("Keypad #{}:".format(iteration))  
    k = 0
    lastLetter = alphabet[0]
    copyAlphabet = alphabet[1:]
    for l in desiredCombination:
        splitted, copyAlphabet = copyAlphabet.split(l)
        letters = lastLetter +  splitted
        print ("{}: {}".format(keys[k], letters))    
        lastLetter = l
        k += 1
    letters = lastLetter + copyAlphabet 
    print ("{}: {}".format(keys[k], letters))
    
