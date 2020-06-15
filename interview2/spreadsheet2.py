'''
Given a spreadsheet, each cell can have two types of values - 1) a number 2) a formula
How will you evaluate the value of spreadsheet and create a function to pass the final value
'''

class Spreadsheet:
    def __init__(self):
        self.sheet_dict = {}

    def updateSheet(self, cell, value):
        self.sheet_dict[cell] = value
    
    def evaluate(self, val):
        if type(val) is int:
            return val
        else:
            symbols_arr = ['+', '-', '*', '/']
            eval_string = ''
            result = ''

            for char in val:
                if char in symbols_arr:
                    eval_string = eval_string + str(self.sheet_dict[result])
                    eval_string = eval_string + char
                    result = ''
                else:
                    result = result + char
            eval_string = eval_string + str(self.sheet_dict[result])
            return eval(eval_string)

    def print(self):
        print(self.sheet_dict)

    def printValues(self):
        for key, val in self.sheet_dict.items():
            print(key, ": ", self.evaluate(val))

if __name__ == "__main__":
    ss = Spreadsheet()
    ss.updateSheet('A1', 1)
    ss.updateSheet('A2', 2)
    ss.updateSheet('A3', 3)
    ss.updateSheet('A4', 4)
    ss.updateSheet('A5', 5)
    
    ss.updateSheet('B1', 'A1*A1')
    ss.updateSheet('B2', 'A2*A2')
    ss.updateSheet('B3', 'A3*A3')
    ss.updateSheet('B4', 'A4*A4')
    ss.updateSheet('B5', 'A5*A5')

    ss.print()
    ss.printValues()