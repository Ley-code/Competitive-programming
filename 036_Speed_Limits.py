numberofstates =int(input())
dictionary = {}
travelledstates = []
for i in range(numberofstates):
    pairs = list(map(str,input().split()))
    dictionary[pairs[0]] = pairs[1]
numberoftravelledstates= int(input())
for i in range(numberoftravelledstates):
    travelledstates.append(input())
for i in range(numberoftravelledstates):
    print(dictionary.get(travelledstates[i]))

