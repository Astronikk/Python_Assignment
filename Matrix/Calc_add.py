import unittest
class matrix:
   def __init__(self, A, rows, columns):
       self.arr = A
       self.row = rows
       self.col = columns
   def __repr__(self):
       val = ""
       for x in range(0, self.row):
           for y in range(0, self.col):
               val += str(self.arr[x][y]) + "  "
           val += "\n"
       return val
   def __add__(self, other):
       a = []
       for x in range(0, self.row):
           b = []
           for y in range(0, self.col):
               b.append(self.arr[x][y] + other.arr[x][y])
           a.append(b)
       c = matrix(a, self.row, self.col)
       return c

A = matrix([[1, 2, 1], [2, 3, 4], [4, 5, 6]], 3, 3)
B = matrix([[4, 5, 4], [5, 6, 7], [7, 1, 8]], 3, 3)
print(A+B)


class TestCalc(unittest.TestCase):
   def test_add(self):
       self.A = matrix([[1, 2, 1], [2, 3, 4], [4, 5, 6]], 3, 3)
       self.B = matrix([[4, 5, 4], [5, 6, 7], [7, 1, 8]], 3, 3)
       result = self.A + self.B
       C = matrix([[5, 7, 5], [7, 9, 11], [11, 6, 14]], 3, 3)
       self.assertEqual(result.__repr__(), C.__repr__())
if __name__ == '__main__':
   unittest.main()
