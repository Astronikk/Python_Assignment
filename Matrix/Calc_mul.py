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
   def __mul__(self, other):
       a = []
       for x in range(0, self.row):
           b = []
           for y in range(0, self.col):
               d = 0
               for z in range(0, self.col):
                   d += self.arr[x][z]*other.arr[z][y]
               b.append(d)
           a.append(b)
       c = matrix(a, self.row, self.col)
       return c

A = matrix([[1, 2, 1], [2, 3, 4], [4, 5, 6]], 3, 3)
B = matrix([[4, 5, 4], [5, 6, 7], [7, 1, 8]], 3, 3)
print(A*B)


# import calc

class TestCalc(unittest.TestCase):
   def test_add(self):
       self.A = matrix([[1, 2, 1], [2, 3, 4], [4, 5, 6]], 3, 3)
       self.B = matrix([[4, 5, 4], [5, 6, 7], [7, 1, 8]], 3, 3)
       result = self.A * self.B
       C = matrix([[21, 18, 26], [51, 32, 61], [83, 56, 99]], 3, 3)
       self.assertEqual(result.__repr__(), C.__repr__())
if __name__ == '__main__':
   unittest.main()
