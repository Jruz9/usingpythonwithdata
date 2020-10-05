#this script will dectect if 2 words are the same backwards.
# I was running on some thrifts, getting ready for the hit, saw some n' and hit, swooshed streets
# to a crowd of r's that sigh to a misfit that aint got no sins except for the art of war that they pretend not
# to be in

def isPalindromes(s):
    """assumes s is a str
    Returns True if letters in s form a palindrome;
    False otherwise.Non-letters and capitalization are ignored."""

    def toChar(s):
        s= s.lower()
        letters=''
        for c in s:
            if c in "abcdefgh":
                letters= letters+c
        return letters

    def isPal(s):
        if len(s) <=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])
    return isPal(toChar(s))


