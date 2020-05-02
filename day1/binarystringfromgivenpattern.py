string = "1??0?101"
output = []

def getOutput(string):
    if "?" in string:
        s1 = string.replace("?", "0", 1)
        s2 = string.replace("?", "1", 1)
        getOutput(s1)
        getOutput(s2)
    else:
        output.append(string)

getOutput(string)
print(output)
