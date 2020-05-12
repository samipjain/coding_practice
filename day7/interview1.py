def findMax1(managers):
    output = -999
    for m in range(len(managers)-1):
        if managers[m] > output:
            output = managers[m]
    return output
    # return max(managers)

def findMax2(managers, children):
    for m in range(len(managers)):
        max_children = 0
        if (children[m] != []):
            max_children = max(children[m])
        managers[m] = max_children + managers[m]
    return max(managers)

if __name__ == "__main__":
    managers = [20, 15, 19]
    children = [
        [5,9],
        [],
        [8]
    ]
    print("Find Max only from list of managers (initial quesstion): ", findMax1(managers))
    print("Find Max (using arrays): ", findMax2(managers, children))
