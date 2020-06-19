def checkStraightLine(coordinates):
    if len(coordinates) == 2:
            return True
        
    # verify if all the other points lie on the same line
    for i in range(2, len(coordinates)):
        y3 = coordinates[i][1]
        y2 = coordinates[i-1][1]
        y1 = coordinates[i-2][1]
        
        x3 = coordinates[i][0]
        x2 = coordinates[i-1][0]
        x1 = coordinates[i-2][0]

        if (y2-y1)*(x3-x2) != (y3-y2)*(x2-x1):
            return False
    return True

if __name__ == "__main__":
    print(checkStraightLine([[1,2],[1,3],[1,4],[1,5],[1,6],[6,7]]))