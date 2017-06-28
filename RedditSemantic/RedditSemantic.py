import praw
import time
import datetime
from RedditApiSecrets import RedditApiSecrets 
from TextFileManipulation import TextFileManipulation
from DateIterator import DateIterator

outputFile = "data.txt"
headers = []

apiSecrets = RedditApiSecrets()
di = DateIterator()

# date eletion announced
di.SetStartDateTime(2017,4,18,00)

#date election ended
di.SetEndDateTime(2017,6,9,00)


tfm = TextFileManipulation(outputFile)

for i in range (1,53):
    tfm.RemoveFile("data" + str(i) + ".txt")

reddit = praw.Reddit(client_id= apiSecrets.GetClientId(),
                     client_secret= apiSecrets.GetClientSecret(),
                     user_agent= apiSecrets.GetUserAgent())

print(reddit.read_only)

subreddit = reddit.subreddit('unitedkingdom')

print(subreddit.display_name)  
print(subreddit.title)         

i = 1

while di.previousDateTime < di.endDateTime:
    print("Start: %s/%s/%s %s:%s:%s - end: %s/%s/%s %s:%s:%s" %(
        di.previousDateTime.day, di.previousDateTime.month, di.previousDateTime.year, \
        di.previousDateTime.hour, di.previousDateTime.minute, di.previousDateTime.second,\
        di.nextDateTime.day, di.nextDateTime.month, di.nextDateTime.year, \
        di.nextDateTime.hour, di.nextDateTime.minute, di.nextDateTime.second))
    
    prev,next = di.GetCurrentOneDayEpoch()

    search_str = "timestamp:" + str(int(prev)) + ".." + str(int(next))

    print(search_str)

    search_results = list(subreddit.search(search_str, syntax='cloudsearch', limit=None))

    tfm.SetFile("data" + str(i) + ".txt")

    if len(search_results) > 0:
        print(len(search_results))
        for sub in search_results:
            headers.append(sub.title)
            
    if len(search_results) > 999:
        print("********999*******")

    tfm.WriteLines(headers)

    headers.clear()

    i +=1

    di.IncreaseOneDay()
