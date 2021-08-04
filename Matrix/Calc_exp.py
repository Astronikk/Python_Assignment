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

  def exponent(self, n):
          a = self.arr
          for xc in range(0, n - 1):
              c = []
              for x in range(0, self.row):
                  d = []
                  for y in range(0, len(a)):
                      e = 0
                      for z in range(0, self.col):
                          e += self.arr[x][z] * a[z][y]
                      d.append(e)
                  c.append(d)
              a = c
          f = matrix(a, self.row, self.row)
          return f

A = matrix([[1, 2, 1],
           [2, 3, 4],
           [4, 5, 6]], 3, 3)
B = matrix([[4, 5, 4],
           [5, 6, 7],
           [7, 1, 8]], 3, 3)
print(A.exponent(3))
print(B.exponent(3))


# import calc

class TestCalc(unittest.TestCase):
   def test_add(self):
       self.A = matrix([[1, 2, 1], [2, 3, 4], [4, 5, 6]], 3, 3)
       result = self.A.exponent(3)
       C = matrix([[95, 132, 151], [242, 337, 384], [384, 535, 610]], 3, 3)
       self.assertEqual(result.__repr__(), C.__repr__())
if __name__ == '__main__':
   unittest.main()

