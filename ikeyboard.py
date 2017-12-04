from itertools import chain, combinations
import sys

Subproblems = {}
def calculateSubproblem(subalpha):
    i = 1
    sumOfAll = 0
    for a in alphabet[LetterToInd[subalpha[0]]:LetterToInd[subalpha[1]]]:
        sumOfAll += i*LetterToVal[a]
        #print (i,"*",a)
        i += 1
    #print ("calculateSubproblem ", subalpha, sumOfAll)
    Subproblems[subalpha] = sumOfAll
def costOfAlpha(letters):
    #print ("costOfAlpha ", letters)
    if (not letters):
        return 0
    sumOfAll = 0
    prev = alphabet[0]
    for letter in letters:
        subproblem = ''.join([prev,letter])
        if subproblem not in Subproblems:
            calculateSubproblem(subproblem)
        sumOfAll += Subproblems[subproblem]
        prev = letter
    lastProblem = ''.join([letters[-1],alphabet[-1]])
    if lastProblem not in Subproblems:
        i = 1
        sumOfThis = 0
        for a in alphabet[LetterToInd[lastProblem[0]]:LetterToInd[lastProblem[1]]]:
            sumOfThis += i*LetterToVal[a]
        #    print (i,"*",a)
            i += 1
        sumOfThis += i*LetterToVal[lastProblem[1]]
        #print (i,"*",lastProblem[1])
        Subproblems[lastProblem] = sumOfThis

    sumOfAll += Subproblems[lastProblem]

    #print(letters, sumOfAll)
    return sumOfAll
def costOfAll(letters):
    sumOfAll = costOfAlpha(letters)

    #print (letters, sumOfAll)
    return sumOfAll

def findCombination():
    minOfSum = 9223372036854775807
    desiredCombination = []
    if (numOfkeys == 1) or len(alphabet) < 2:
        return desiredCombination

    sb = []
    if numOfkeys >1 and len(alphabet) > 3 :
        sb = combinations(alphabet[1:-1], numOfkeys-1)
    elif len(alphabet)>9:
        candidates = vals[1:]
        candidates.sort(reverse=True)
        candidateLetters = [ValToLetter[a] for a in candidates]
        #print (candidateLetters)
        candidateLetters = ''.join(candidateLetters)
        sb = combinations(candidateLetters, numOfkeys-1)
    elif len(alphabet) == 2 or len(alphabet) == 3:
        sb = alphabet[1:]

    for s in sb:
        s= sorted(s)

        sumOfCost = costOfAll(s)

        if sumOfCost <  minOfSum:
           minOfSum = sumOfCost
           desiredCombination = s

    return desiredCombination

n = int(input())

for iteration in range(0,n):

    numOfkeys,l = input().split(' ')
    keys = input()
    alphabet = input()

    l = int(l)
    numOfkeys = int(numOfkeys)
    LetterToVal = {}
    LetterToInd = {}
    vals = []
    ValToLetter = {}
    letterInd = 0
    for a in alphabet:
        vals.append(int(input()))
        LetterToVal[a] = vals[letterInd]
        LetterToInd[a] = letterInd
        ValToLetter[vals[letterInd]] = a
        letterInd += 1


    desiredCombination = findCombination()
    #desiredCombination = ['E','H','L','N','R','T','W']
    #print (costOfAlpha(['E','H','L','N','R','T','W']))
    print("Keypad #{}:".format(iteration+1))
    k = 0
    lastLetter = alphabet[0]
    copyAlphabet = alphabet[1:]
    for l in desiredCombination:
        splitted = copyAlphabet.split(l)
        letters = lastLetter +  splitted[0]
        copyAlphabet = splitted[1]
        print ("{}: {}".format(keys[k], letters))
        lastLetter = l
        k += 1
    letters = lastLetter + copyAlphabet
    print ("{}: {}".format(keys[k], letters))
