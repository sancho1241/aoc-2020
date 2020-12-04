import unittest
import day01.python.sancho1241.solution as solution

class myTestClass(unittest.TestCase):
    def myTest(self):
        data = solution.parse(open("input.txt").lines)
        #print ("hello world")
        #print (data)
        self.assertEqual("1",solution.solve(data))
        
if __name__ == '__main__':
    unittest.main()