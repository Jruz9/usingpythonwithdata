#this python file is about recursion, one is iterative the other is recursive
def factI(n):
    """Assume n an int > 0
        return n!"""
    result=1
    while n> 1:
        result=result*n
        n-=1
    return result

def factR(n):
    """assumes n an int >0 returns n!"""
    if n==1:
        return n
    else:
        return n*factR(n-1)

    