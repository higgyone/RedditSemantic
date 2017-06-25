import praw
import time
import datetime
from RedditApiSecrets import RedditApiSecrets 
from TextFileManipulation import TextFileManipulation

outputFile = "data.txt"
headers = []

apiSecrets = RedditApiSecrets()
tfm = TextFileManipulation(outputFile)

tfm.RemoveFile()

reddit = praw.Reddit(client_id= apiSecrets.GetClientId(),
                     client_secret= apiSecrets.GetClientSecret(),
                     user_agent= apiSecrets.GetUserAgent())

print(reddit.read_only)

subreddit = reddit.subreddit('unitedkingdom')

print(subreddit.display_name)  
print(subreddit.title)         
print(subreddit.description)

start_dt = datetime.datetime(year=2017, month=4, day=18, hour=11).timetuple()
end_dt = datetime.datetime(year=2017, month=4, day=18, hour=20).timetuple()

s_t = time.mktime(start_dt)
e_t = time.mktime(end_dt)

search_str = "timestamp:" + str(int(s_t)) + ".." + str(int(e_t))

search_results = list(subreddit.search(search_str, syntax='cloudsearch', limit=None))

i = 1

if len(search_results) > 0:

    for sub in search_results:
        headers.append(str(i) + ": " + sub.title)
        i +=1
    tfm.WriteLine("Test")
    tfm.WriteLines(headers)

    #with open(outputFile, "a") as myfile:
     #   for sub in search_results:
      #      print(str(i) + ": " + sub.title)
       #     date = datetime.datetime.fromtimestamp(sub.created_utc)
        #    print(date)
         #   myfile.write(str(i) + ": " + sub.title + "\n")
          #  i = i + 1


