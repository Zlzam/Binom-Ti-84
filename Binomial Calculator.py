"""
TI-84 Python-style Binomial Calculator - built to be lean
Calculates the probability of exactly X successes in N Bernoulli trials,
given a success probability P.
Author: ZLzam
Built for Ti-84
"""

##init vars##
N = -1
X = -1 
P = -1
Q = -1
choice = "N"

##Functions##
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def data_entry():
    print("\nEnter N (Number of trials):")
    N = float(input())
    print("Enter X (Number of Success):")
    X = float(input())
    print("Enter P (Chance of Success):")
    P = float(input())
    return N, X, P

def calculations(N, X, P):
    Q = 1 - P
    numerator = factorial(N)
    denominator = factorial(X) * factorial(N - X)
    temp = numerator / denominator
    result = temp * (P ** X) * (Q ** (N - X))
    print("\nInputs given:")
    print("\nN=%.2f, X=%.2f, P=%.2f, Q=%.2f" % (N, X, P, Q))
    print("\nResult: ")
    print(round(result, 6))
    return result

### MAIN ###
while True:

    if choice == "Y":
        print("\nCurrent N=%.2f, P=%.2f" % (N, P))
        print("\nWould you like to calculate additional X values with the prior inputs? \n(1)Yes, 2(No):")
        userChoice = int(input())
        while userChoice == 1:
            print("\nPlease enter X value: ")
            X = float(input())
            calculations(N, X, P)
            print("\nWould you like to continue with more X values? \n(1)Yes, 2(No):")
            userChoice = int(input())

    ## Data entry ##
    N, X, P = data_entry()
    calculations(N, X, P)

    print("\nExit? \n(1)Yes, 2(No): ")
    B = int(input())
    if B == 1:
        break
    else:
        choice = "Y"
