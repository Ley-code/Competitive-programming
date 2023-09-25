chainmaths = list(map(str,input().split()))
def basicmath(chainmaths):
    result = int(chainmaths[0])
    strings = ""
    for i in range(len(chainmaths)):
        strings+=chainmaths[i]+" "
        if chainmaths[i] == "+":
            result+=(int(chainmaths[i+1]))
        elif chainmaths[i]=="-":
                result-=(int(chainmaths[i+1]))
    print(strings + str(result))
basicmath(chainmaths)