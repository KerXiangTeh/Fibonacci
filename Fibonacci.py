# O(n^2) or worse
def fibBad(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)


# O(n) time but not space 
def fib(n):
    F = [None] * (n + 1)
    F[0] = 0
    return _fib(n, F)

def _fib(n, F):
    if (F[n] == None):
        if (n == 1 or n == 2):
            F[n] = 1
        else:
            F[n] = _fib(n-1, F) + _fib(n-2, F)
    return F[n]

# O(n) time and space
def fibBottomUp(n):
    F = [None] * (n + 1)
    F[1] = F[2] = 1
    for i in range(3, n + 1):
        F[i] = F[i-1] + F[i-2]
    return F[n]

# bad fib
print(fibBad(11))
# fibBad(111) took too long to calculate

# O(n) time 
print(fib(11))
print(fib(111))

# O(n) time & space
print(fibBottomUp(11))
print(fibBottomUp(111))

# 0 1 2 3 4 5 6 7  8  9  10 11
# 0 1 1 2 3 5 8 13 21 34 55 89
