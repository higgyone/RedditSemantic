from datetime import datetime
from datetime import timedelta


class DateIterator(object):
    """Class to get the next date in the sequence"""

    def __init__(self):
        self.startDateTime = None
        self.endDateTime = None
        self.nextDateTime = None
        self.previousDateTime = None

    def SetStartDateTime(self, year, month, day, hour):
        """Set the start datetime"""
        self.startDateTime = datetime(year = year, month = month, day = day, hour = hour)
        self.previousDateTime = self.startDateTime
        self.nextDateTime = self.previousDateTime + timedelta(days = 1)

    def SetEndDateTime(self, year, month, day, hour):
        """Set the end datetime"""
        self.endDateTime = datetime(year = year, month = month, day = day, hour = hour)

    def ResetDateTime(self):
        """reset the stored datetimes to None"""
        self.startDateTime = None
        self.endDateTime = None
        self.nextDateTime = None
        self.previousDateTime = None

    def GetCurrentOneDayEpoch(self):
        """get the current previous and next datetimes as utc epoch"""
        start = time.mktime(self.previousDateTime.utctimetuple())
        end = time.mktime(self.nextDateTime.utctimetuple())

        return start, end

    def IncreaseOneDay(self):
        """increase the previous and next datetime by one day"""
        if self.startDateTime == None:
            print("No dates set")
            return

        self.previousDateTime = self.nextDateTime
        self.nextDateTime = self.nextDateTime + timedelta(days = 1)

    def GetCurrentStartEndDateTime(self):
        """get the previous and next datetimes"""
        return self.previousDateTime, self.nextDateTime
