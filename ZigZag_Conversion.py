def convert( s, numRows):
    if numRows==1:
        return s
    rows = {row:"" for row in range(1,numRows+1)}
    row = 1
    up = True
    for letter in s:
        rows[row] += letter
        if row==1 or (row < numRows) and up:
            row+=1
            up=True
        else:
            row-=1
            up=False
    converted = ""
    for row in range(1,numRows+1):
        converted+=rows[row]
    return converted
