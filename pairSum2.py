'''
Given a list find a pair of numbers that add up to 8

'''

ans = 8

listSum = [1, 2, 4, 6]
sortedList = sorted(listSum)
lengthList = len(sortedList)


def calc(sortedList):
    counter = 0
    start = 0
    stop = lengthList - 1
    sumPair = sortedList[start] + sortedList[stop]
    while (sumPair != ans) and (counter <= len(sortedList)):
        sumPair = sortedList[start] + sortedList[stop]
        if sumPair > ans:
            # del sortedList[-1]
            stop = stop - 1
        elif sumPair < ans:
            # del sortedList[0]
            start = start + 1
        counter = counter + 1

    if (sumPair == ans) and (start != stop):
        print("The answer is " + str(sortedList[start]) + " and " + str(sortedList[stop]))
    else:
        print("No answer")


calc(sortedList)
