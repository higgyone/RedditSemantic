import praw
from RedditApiSecrets import RedditApiSecrets 
from DateIterator import DateIterator
from TextFileManipulation import TextFileManipulation

class PrawWrapper(object):
    """Class that wraps PRAW"""

    def __init__(self):
        self.apiSecrets = RedditApiSecrets()
        self.di = DateIterator()
        self.subreddit = 'unitedkingdom'
        self.reddit = None
        self.tfm = TextFileManipulation()
        self.headers = []

    def GetTitlesInElectionRange(self,):

        # election start date
        self.di.SetStartDateTime(2017,4,18,00)


        # election end date
        self.di.SetEndDateTime(2017,6,9,00)

        reddit = praw.Reddit(client_id= self.apiSecrets.GetClientId(),
                     client_secret= self.apiSecrets.GetClientSecret(),
                     user_agent= self.apiSecrets.GetUserAgent())

        print(reddit.read_only)

        subr = reddit.subreddit(self.subreddit)

        print(subr.display_name)  
        print(subr.title)         

        i = 1

        while self.di.previousDateTime < self.di.endDateTime:
            print("Start: %s/%s/%s %s:%s:%s - end: %s/%s/%s %s:%s:%s" %(
                self.di.previousDateTime.day, self.di.previousDateTime.month, self.di.previousDateTime.year, \
                self.di.previousDateTime.hour, self.di.previousDateTime.minute, self.di.previousDateTime.second,\
                self.di.nextDateTime.day, self.di.nextDateTime.month, self.di.nextDateTime.year, \
                self.di.nextDateTime.hour, self.di.nextDateTime.minute, self.di.nextDateTime.second))
    
            prev,next = self.di.GetCurrentOneDayEpoch()

            search_str = "timestamp:" + str(int(prev)) + ".." + str(int(next))

            print(search_str)

            search_results = list(subr.search(search_str, syntax='cloudsearch', limit=None))

            self.tfm.SetFile("data\\titles" + str(i) + ".txt")

            if len(search_results) > 0:
                print(len(search_results))
                for sub in search_results:
                    self.headers.append(sub.title)
            
            if len(search_results) > 999:
                print("********999*******")

            self.tfm.WriteLines(self.headers)

            self.headers.clear()

            i +=1

            self.di.IncreaseOneDay()


