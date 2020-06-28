def sortChessSubsquares(numbers, queries):
    # if sum of x and y is even, then that square is black, else white
    for query in queries:
        black_squares = []
        white_squares = []
        x = query[0]
        y = query[1]
        w = query[2]
        for i in range(x, x+w):
            for j in range(y, y+w):       
                if (i+j)%2==0:
                    black_squares.append(numbers[i][j])
                else:
                    white_squares.append(numbers[i][j])
        print("Black",black_squares)
        print("White",white_squares)

        black_squares.sort()
        white_squares.sort()
        black_index = 0
        white_index = 0

        for i in range(x, x+w):
            for j in range(y, y+w):       
                if (i+j)%2==0:
                    numbers[i][j] = black_squares[black_index]
                    black_index += 1
                else:
                    numbers[i][j] = white_squares[white_index]
                    white_index += 1
    return numbers

if __name__ == "__main__":
    numbers = [[1,4,3,2], [8,4,7,1], [1,5,2,1]]
    queries = [[0,1,3], [1,0,2]]

    print(sortChessSubsquares(numbers, queries))
            
        
