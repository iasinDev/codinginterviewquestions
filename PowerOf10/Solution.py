import math
import timeit

def isPowerOf10(x):
    while x != 0 and x % 10 == 0:
        x //= 10
    return x == 1

def isPowerOf10ByLog(x):
    try:
        return math.log(x,10).is_integer()
    except ValueError:
        return False

def runPower10(array_ok, array_not_ok):
    for x in array_ok:
        assert(isPowerOf10(x))
    for x in array_not_ok:
        assert(not isPowerOf10(x))

def runPower10ByLog(array_ok, array_not_ok):
    for x in array_ok:
        assert(isPowerOf10ByLog(x))
    for x in array_not_ok:
        assert(not isPowerOf10ByLog(x))

array_ok = [1,10,100]
array_not_ok = [-1000,-100,-10,-1,0,105]
start = timeit.default_timer()
runPower10(array_ok, array_not_ok)
stop = timeit.default_timer()
print('Time: ', stop - start) 

start = timeit.default_timer()
runPower10ByLog(array_ok, array_not_ok)
stop = timeit.default_timer()
print('Time: ', stop - start)

