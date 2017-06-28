import unittest
from DateIterator import DateIterator
from datetime import timedelta

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


if __name__ == '__main__':
    unittest.main()
