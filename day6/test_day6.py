import unittest
from day6 import Day6
class MyTestCase(unittest.TestCase):
    def test_day6(self):
        day6 = Day6("input_test")
        lines = day6.lines
        print(f"\n{repr(lines)}")
        self.assertEqual(repr(lines), "['123 328  51 64\\n', ' 45 64  387 23\\n', '  6 98  215 314\\n', '*   +   *   +\\n']")

        operands = day6.operands
        print(f"{repr(operands)}")
        self.assertEqual(repr(operands),
                         "[[123, 328, 51, 64], [45, 64, 387, 23], [6, 98, 215, 314]]")

        operators = day6.operators
        print(f"{repr(operators)}")
        self.assertEqual(repr(operators),
                         "['*', '+', '*', '+']")

        answers = day6.answers
        print(f"{repr(answers)}")
        self.assertEqual(repr(answers),
                         "[33210, 490, 4243455, 401]")

        grand_total = day6.get_grand_total()
        print(f"{repr(grand_total)}")
        self.assertEqual(repr(grand_total),
                         "4277556")

        day6 = Day6("input")
        grand_total = day6.get_grand_total()
        print(f"{repr(grand_total)}")
        self.assertEqual(repr(grand_total),
                         "6295830249262")




if __name__ == '__main__':
    unittest.main()
