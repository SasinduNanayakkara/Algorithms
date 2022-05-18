from sqlite3 import apilevel


alphabet = 256

def getNextState(pattern, M, state, x):
    if state < M and x == ord(pattern[state]):
        return state + 1

    i = 0

    # Start matching from the last possible value and stop if you find a match
    for s in range(state, 0, -1):
        if ord(pattern[s - 1]) == x:
            while(i < s - 1):
                if pattern[i] != pattern[state -s + 1 + i]:
                    break
                i += 1

                if i == s - 1:
                    return s
    return 0

def computeTF(pattern, M):
    # Create TF table
    global alphabet

    TF = [[0 for i in range(alphabet)]\
        for _ in range(M)]

    for state in range(M + 1):
        for x in range(alphabet):
            z = getNextState(pattern, M, state, x)
            TF[state][x] = z
    
    return TF


def search(pattern, text):

    global alphabet
    M = len(pattern)
    N = len(text)
    TF = computeTF(pattern, M)

    state = 0
    for i in range(N):
        state = TF[state][ord(text[i])]
        if state == M:
            print("Pattern found at index " + str(i - M + 1))


text = "AABAACAADAABAAABAA"
pattern = "AABA"
search(pattern, text)