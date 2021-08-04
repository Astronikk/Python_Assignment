import unittest
def determinant(matrix):

   num_row = len(matrix)
   for row in matrix:
       if len(row) != num_row:
           print("Not a square matrix.")
           return None
   if num_row == 1:
       return matrix[0][0]
   else:
       sign = -1
       result = 0
       for i in range(num_row):
           m = []
           for j in range(1, num_row):
               n = []
               for k in range(num_row):
                   if k != i:
                       n.append(matrix[j][k])
               m.append(n)
           sign *= -1
           result = result + sign * matrix[0][i] * determinant(m)
   return result

A = [[1, 2, 1], [2, 3, 4], [4, 5, 6]]
print(determinant(A))


# import calc

class TestCalc(unittest.TestCase):
   def test_add(self):
       self.A = determinant([[1, 2, 1], [2, 3, 4], [4, 5, 6]])
       result = self.A
       C = 4
       self.assertEqual(result, C)
if __name__ == '__main__':
   unittest.main()
