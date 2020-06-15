'''
Given a spreadsheet, each cell can have two types of values - 1) a number 2) a formula
How will you evaluate the value of spreadsheet and create a function to pass the final value
'''

class Spreadsheet:
    def __init__(self, rows, cols):
        self.arr = [[0 for i in range(cols)] for j in range(rows)]
        self.rows = rows
        self.cols = cols
        self.dict_arr = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, 'AA': 27, 'AB': 28, 'AC': 29}

    def updateSheet(self, row, col, value):
        self.arr[row][col] = value
    
    def evaluate(self, val):
        symbols_arr = ['+', '-', '*', '/']
        num_arr = ['1','2','3','4','5','6','7','8','9']
        str_res = ''
        num_res = ''

        for char in val:
            if char not in num_arr:
                str_res = str_res + char
            else:
                num_res = num_res + char
        row = self.dict_arr[str_res] - 1
        col = int(num_res) - 1
        return self.arr[col][row]

    def print(self):
        for row in self.arr:
            print(row)

    def printValues(self):
        for row in self.arr:
            for r in row:
                if type(r) is int:
                    print(r, end=" ")
                else:
                    val = self.evaluate(r)
                    print(val, end=" ")
            print()

if __name__ == "__main__":
    ss = Spreadsheet(5,2)
    ss.updateSheet(0,0,1)
    ss.updateSheet(1,0,2)
    ss.updateSheet(2,0,3)
    ss.updateSheet(3,0,4)
    ss.updateSheet(4,0,5)

    ss.updateSheet(0,1,'A1')
    ss.updateSheet(1,1,'A2')
    ss.updateSheet(2,1,'A3')
    ss.updateSheet(3,1,'A4')
    ss.updateSheet(4,1,'A5')
    
    ss.print()
    ss.printValues()