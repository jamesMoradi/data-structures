class Matrix :
    def __init__(self) :
        self.matrix = []
    
    def create (self) :
        rows_num = int(input("please enter number of rows : "))
        cols_num = int(input("please enter number of columns : "))  
        for i in range(1, rows_num+1) :
            row = []
            for j in range(1, cols_num+1) :
                val = int(input(f"please enter value for column {i} and row {j} : "))
                row.append(val)
            self.matrix.append(row)

        return self.matrix

    def print_matrix(self, matrix) :
        for i in range (len(matrix)) :
            print(self.matrix[i])
