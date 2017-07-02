import unittest
import os
from DateIterator import DateIterator
from datetime import timedelta
from WordGetter import WordGetter

class Test_TestRedditSemantic(unittest.TestCase):
    def test_A(self):
        self.fail("Not implemented")

    def test_dateiterator(self):
        di = DateIterator()

        self.assertIsNone(di.startDateTime)

        di.SetStartDateTime(2017, 1, 1, 12)
        di.SetEndDateTime(2017, 1, 5, 12)

        self.assertIs(di.previousDateTime, di.startDateTime)

        next = di.previousDateTime + timedelta(days = 1)
        self.assertEqual(di.nextDateTime, next)

        di.IncreaseOneDay()

        prev, new = di.GetCurrentStartEndDateTime()
        self.assertEqual(prev, next)
        self.assertEqual(new, next + timedelta(days = 1))

        di.IncreaseOneDay()

        prev, new = di.GetCurrentStartEndDateTime()
        self.assertEqual(prev, next + timedelta(days = 1))
        self.assertEqual(new, next + timedelta(days = 2))

    def testWordGetterReadLines(self):
        wg = WordGetter()
        path = os.getcwd()
        testFile = path + "\\testfile.txt"
        outputTestFile = path + "\\testOutput.txt"
        wg.ReadEachLine(testFile, self.testReturnLine)

        wg.ReadEachLine(testFile)
        wg.WriteOutWordsAndCounts(outputTestFile)

    def testReturnLine(self, line):
        """helper test method for testWordGetterReadLines"""
        if str(line).startswith("1"):
            self.assertEqual(line, "1 one two three four five six\n")
        elif str(line).startswith("2"):
            self.assertEqual(line, "2 seven eight nine ten\n")
        elif str(line).startswith("3"):
            self.assertEqual(line, "3 eleven twelve thirteen\n")
        else:
            self.assertFalse("Bad file data")





if __name__ == '__main__':
    unittest.main()
