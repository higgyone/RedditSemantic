# RedditSemantic
Semantic analysis of Reddit r/unitedkingdom during the 2017 general election to test peoples thoughts on the 4 major political parties based solely on the subreddits titles.

This code extracts the r/unitedkingdon titles between 18th April 2017 (when the general election was announced) and 9th June 2017 (after the election was over). If the title contains one of the search terms (see code) for the different parties (Labour, Lib Dem, Tory and Ukip) it adds them to their party's file. 

The titles for each party where then manually put through semantic analysis using SentiStrength (with default settings) to get the postive and negative-ness of each title. The results are then tabulated in Analysis.xlsx.

Analysis.xlsx shows that Labour titles are more positive than the Tories then Lib Dems and unsurprisingly Ukip. Also negative sentiment has Lib Dems thought of as less negative than Labour then the Tories with Ukip most negative.

There are many caveats to this, notably the sentiment analysis was not trained to headlines so was just picking out words, the search terms found titles that included more than one party in a title and this was not removed from individual party searches. I will probably not have got all relevant titles for each party. I definately have got a few extra titles not related to the elections e.g searching for May through up Mayor and the Manchester Mayor race that had nothing to do with the election or the Tory party. I think they will even themselves out, but not done any analysis of this.

The python code was written at night when my brain was not functioning too well, so it is not great nor commented much. It was just an excuse to play with PRAW, test a theory of mine and teach myself some python.

Unless anything else changes this is probably the end of the commits for this project.

Higgyone 
9th July 2017
