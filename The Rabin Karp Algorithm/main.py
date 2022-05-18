alphabet = 256

def search(pattern, text, q):
    M = len(pattern)
    N = len(text)
    p = 0 # hash value for pattern
    t = 0 # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h*alphabet)%q

    # Calculate the hash value of pattern and first window of text
    for i in range(M):
        p = (alphabet*p + ord(pattern[i]))%q
        t = (alphabet*t + ord(text[i]))%q

    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and pattern.
        # If the hash values match then only check for characters on by one
        if p==t:
            # Check for characters one by one
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
            else: j+=1

            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if (i < N-M):
            t = (alphabet*(t-ord(text[i])*h) + ord(text[i+M]))%q

        if t < 0:
            t = t+q

text = "AABAACAADAABAAABAA"
pattern = "AABA"

# q = size of alphabet
q = 101
search(pattern, text, q)