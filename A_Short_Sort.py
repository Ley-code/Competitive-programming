testcase = int(input())
words = []
def listtowrd(listword):
    strword = ""
    for i in listword:
        strword+= i
    return strword
def swaps(word):
    listword = []
    for i in range(len(word)):
        listword.append(word[i])
    for i in range(3):
        if word == "abc":
            return "YES"
        else:
            if i!=2:
                temp = listword[i]
                listword[i] = listword[i+1]
                listword[i+1] = temp
                if listtowrd(listword) == "abc":
                    return "YES"
                else:
                    temp = listword[i]
                    listword[i] = listword[i+1]
                    listword[i+1] = temp
            else:
                temp = listword[i]
                listword[i] = listword[0]
                listword[0] = temp
                if listtowrd(listword) == "abc":
                    return "YES"
            
    return "NO"




for i in range(testcase):
    print(swaps(input()))
