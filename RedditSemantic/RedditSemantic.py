from TextFileManipulation import TextFileManipulation
from WordGetter import WordGetter
from PrawWrapper import PrawWrapper

wg = WordGetter()
pw = PrawWrapper()
tfm = TextFileManipulation()

# bad search terms showing too many non-related results:
# tim - thought farron but time appears a lot
# paul - as in nuttal too many different pauls


searchTerms_Labour = [
    "labour",
    "Labour",
    "Corbyn", 
    "Jeremy C",
    "corbyn",  
    "jeremy c",
    "jeremy c",
    "Jeremy C",
    "diane",
    "abbot",
    "Diane",
    "Abbot",
    "Abbott",
    "abbott",
    "Mcdonald",
    "Blair",
    "Kier",
    "Starmer"
    "Emily",
    "Thornberry"
    ]

searchTerms_LibDem = [
    "Lib Dem", 
    "lib dem", 
    "liberal dem",
    "Liberal Dem",
    "Libs",
    "libs", 
    "farron", 
    "Farron" 
    ]

searchTerms_Ukip = [
    "ukip",
    "UKIP",
    "Ukip",
    "Nuttall",
    "Nutal",
    "nuttall",
    "nutal"
    ]


searchTerms_Tory = [
    "May", 
    "theresa", 
    "Theresa", 
    "tory", 
    "tories",
    "conservative", 
    "Tory", 
    "Tories",
    "Conservative",
    "Prime",
    "PM",
    "Boris",
    "Boris Johnson",
    "boris johnson",
    "boris J",
    "Amber",
    "Rudd",
    "rudd",
    "Philip Hammond",
    "philip hammond",
    "philip Hammond",
    "hammond",
    "Hammond",
    "Cameron",
    "Davies"
    ]

searches = {
    "Tory" : searchTerms_Tory, 
    "Labour" : searchTerms_Labour, 
    "LibDems" : searchTerms_LibDem, 
    "Ukip" : searchTerms_Ukip}

#for i in range (1,53):
#    tfm.RemoveFile("data\\titles\\titles" + str(i) + ".txt")

#for i in range (1,53):
#    tfm.RemoveFile("data\\SearchedTitles" + str(i) + ".txt")

for key in searches:
    print("Deleting: " + key + ".txt")
    tfm.RemoveFile("data\\results\\" + key + ".txt")

#pw.GetTitlesInElectionRange()

#wg.ResetDictionary()

#for i in range(1,52,1):
#    outputFile = "data\\titles\\titles" + str(i) + ".txt"
#    print(outputFile)
#    wg.ReadEachLine(outputFile)

#print("Writing files")
#wg.WriteOutWordsAndCountsKeySorted("WordsKeySorted.txt")
#wg.WriteOutWordsAndCountsValueSorted("WordsValueSorted.txt")

for key, value in searches.items():
    print("Working on: " + key)
    
    for i in range(1,52,1):
        inputFile = "data\\titles\\titles" + str(i) + ".txt"
        of = "data\\results\\" + str(key) + ".txt"
        wg.GetLinesContainingWordList(inputFile, value)
    
    wg.WriteOutSentances(of)
    wg.ResetSentanceList()

print("Done")