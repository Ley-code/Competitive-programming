def wrap(string, max_width):
    each_string = ""
    remaining = len(string) % max_width
    for i in range(max_width,len(string),max_width):
        each_string+= string[i-max_width:i]
        each_string+="\n"
    if remaining:
        for i in range(-(remaining),0):
            each_string+=string[i]
    return each_string