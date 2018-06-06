# A group of students are planning a trip.
# The group agrees in advance to share expenses equally, but it is not practical to share every expense as it occurs.
# Thus individuals in the group pay for particular things, such as meals, hotels, and plane tickets.
# After the trip, each student's expenses are tallied and money is exchanged so that the net cost to each is the same, to within one cent.
# The program outputs the minimum amount of money that must change hands in order to equalize (within one cent) all the students' costs.

# Sample input contain information for several trips.
# Each trip consists of a line containing a positive integer n denoting the number of students on the trip.
# This is followed by n lines input, each containing the amount spent by a student in dollars and cents
# A single line containing 0 follows the information for the last trip

# Constraints: n < 1000, cost by one student < $10,000.00

# Sample Input
# 3
# 10.00
# 20.00
# 30.00
# 4
# 15.00
# 15.01
# 3.00
# 3.01
# 0

# Sample Output
# $10.00
# $11.99

from math import floor

# define a function to get all the amount spent by each student and return a 2-dimenional array storing the information.
def getInput():
    l = []
    no_of_students = None

    print "Enter Here:"
    while no_of_students != 0:
        costs = []
        no_of_students = int(input())
        for _ in range(no_of_students):
            costs.append(float(input()))
        if costs: l.append(costs)
    print '\n'
    return l


# define a function to calculate the minimum amount of money that must change hands for a trip
def MinMoneyToChangeHands(costs):
    s = round(sum(costs), 2)
    average = s / len(costs); average = floor(average * 100) / 100.

    lst = [average] * len(costs)
    index = 0
    # Handle the extra cents that cannot be evenly distributed
    while round(sum(lst), 2) != s:
        lst[index] += 0.01
        index += 1
        if index == len(lst): index = 0

    # calculate the sum of all differences between costs[i] and lst[i], where 0 <= i <= len(costs) - 1
    # then divide it by two
    diff = 0
    costs.sort(reverse=True)
    for i in range(len(costs)):
        diff += abs(costs[i] - lst[i])
    diff /= 2.
    return round(diff, 2)

#finally, define a function that calculates the output of several trips and output them
def MinMoneyToChangeHands_SeveralTrips():
    trips = getInput()
    for costs in trips:
        print '$' + str(MinMoneyToChangeHands(costs))

MinMoneyToChangeHands_SeveralTrips()
