ntolmap = {"0":"o","1":"i","3": "e","4": "a","5": "s","7": "t"," ":" "}
testcase = int(input())
for i in range(testcase):
    numberword = list(map(str,input()))
    oneline = ""
    for number in numberword:
        oneline+= ntolmap.get(number)
    print(oneline)