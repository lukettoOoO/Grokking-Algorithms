"""
def countdown(i):
    print(i)
    countdown(i - 1)

countdown(3)
"""

def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)

countdown(3)

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
    
print(fact(3))