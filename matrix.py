class Matrix(object):
        def __init__(self, matrix_str):
                self.matrix = self.make_matrix(matrix_str.replace('\n', ' \n ').split(' '))
        def row(self, index):
                return self.matrix[index-1]
                
        def column(self, index):
                return [row[index-1] for row in self.matrix]




        def make_matrix(self, matrix_str):
                matrix = []
                if '\n' in matrix_str:
                        row_length = matrix_str.index('\n')
                else:
                        row_length = len(matrix_str)
                
                matrix_str = [x for x in matrix_str if x != '\n']
                for i in range(0, len(matrix_str), row_length):
                        matrix.append(matrix_str[i:i+row_length])
                matrix = [[int(num) for num in item if num] for item in matrix]
                return matrix