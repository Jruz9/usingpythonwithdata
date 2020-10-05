# this python files is about specifcation (abstraction,decomposition,assumption,guarantees)

def findRoot(x, power, epsilon):
    """Assume x and epsilon int or float,power an int, epsilion >0 & power >=1
    Return float y such that y^power us within epsilon of x.
    If such a float does not exist, it return None"""

    if x < 0 and power % 2 == 0:
        return None

    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**power - x) >= epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

def testFindRoot():
    epsilon =0.001
    for x in [0.25,-0.25,0,2,-2,8,-8]:
        for power in range(1,4):
            print('Testing x=',str(x),'and power = ',power)
            result =findRoot(x,power,epsilon)
            if result==None:
                print("  NO Root")
            else:
                print("   ",result**power,"~=",x)

