
"""
TI-84 Python-style Binomial Calculator - built to be lean
Calculates the probability of exactly X successes in N Bernoulli trials,
given a success probability P.

"""

#Author ZLzam
#Built for Ti-84



##init vars##
N = -1
X = -1 
P = -1
Q = -1
B = "N"
choseN = "N"

##Functions##
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def data_entry():
    print("\nEnter N (Thing):")
    N = float(input())
    print("\nEnter X (Number of Success):")
    X = float(input())
    print("\nEnter P (Chance of Success):")
    P = float(input())
    return N, X, P

def calculations(N, X, P):
        ##Calculation##
    Q = 1-P
    numerator = factorial(N) 
    denominator = factorial(X)*factorial(N-X) 
    temp = numerator / denominator
    result = temp * (P**X) * (Q**(N-X))
    print("\nInputs given:")
    print(f"\nN={N}, X={X}, P={P}, Q={Q}")
    print("\nresult: ")
    print(round(result, 6))
    return result

### MAIN ###
while(True):
    
    if (choseN == "Y"):
        print("\nWould you like to calculate additional X values with the prior inputs? (Y/N):")
        choseNY = input()
        while choseNY == "Y":
            print("\nPlease enter X value: ")
            X = float(input())
            calculations(N, X, P)
            print("\nWould you like to continue with more X values? (Y/N):")
            choseNY = input()

        else:
            break

    ##Data entry##
    N, X, P = data_entry()
    
    print(f"\nFYI: Q = {Q}" )

    calculations(N, X, P)

    print ("\nExit? Y/N: ")
    B = input()
    if(B == "Y"):
        break
    else:
        choseN = "Y"
        continue
