# The program is about the 3n + 1 problem.
# Start with an integer n, if n is even, divide by 2, if n is odd, multiply by 3 and plus 1.
# Eventually n will go to 1 (but not proved yet).
# The program aims to find the maximum cycle length over all numbers between i and j, including both endpoints.

# First, we define a function that finds the number of rounds of n to go to 1.
# Pre-Conditions: n is an integer and n > 0
def findRounds(n):
    assert type(n) is int and n > 0
    rounds = 1;
    while n != 1:
        if n % 2 == 0:
            n /= 2
        elif n % 2 == 1:
            n = 3 * n + 1
        rounds += 1
    return rounds

# Observe the number of found between 1 to n, find the pattern of the numbers that take most rounds.

#for i in range(1, 101):
#    print i, 'rounds: ', findRounds(i)

# Define the function that finds the number of round of all numbers between i and j, inclusively, and output the maximum
# Pre-Conditions: j >= i
# Time complexity: O(n)
def findMaxRounds(i, j):
    assert j >= i
    max = 0
    for num in range(i, j+1):
        rounds = findRounds(num)
        if rounds > max: max = rounds
    return max

# print findMaxRounds(1, 10)
# print findMaxRounds(100, 200)
# print findMaxRounds(201, 210)
# print findMaxRounds(900, 1000)

for i in range(2, 101):
    print 'i = ', i, 'MaxRounds = ', findMaxRounds(1, i)
