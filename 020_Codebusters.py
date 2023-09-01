def swapper(letter1,letter2):
    swapped = ''
    swapped+=letter2
    swapped+=letter1
    return swapped

testcase = int(input())
words = []
answer = []
for i in range(testcase):
    words.append(input())
for i in range(len(words)):
    final = ""
    if len(words[i])%2 == 0:   
        for j in range(0,len(words[i]),2):
            final+=swapper(words[i][j],words[i][j+1])
    else:
        for j in range(0,len(words[i])-1,2):
            final+=swapper(words[i][j],words[i][j+1])
        final+=words[i][-1]
    print(final)   

