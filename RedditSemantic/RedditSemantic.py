from TextFileManipulation import TextFileManipulation
from WordGetter import WordGetter
from PrawWrapper import PrawWrapper

wg = WordGetter()
pw = PrawWrapper()
tfm = TextFileManipulation()

# bad search terms showing too many non-related results:
# tim - thought farron but time appears a lot
# paul - as in nuttal too many different pauls


searchTerms = [
    "may", 
    "theresa", 
    "labour", 
    "corbyn", 
    "jeremy", 
    "tory", 
    "tories",
    "conservative", 
    "lib", 
    "dem",  
    "farron", 
    "prime",
    "ukip",
    "pm",
    "boris",
    "johnson",
    "diane",
    "abbot",
    "amber",
    "rudd",
    "nuttall",
    "nutal",
    "philip",
    "hammond",
    "mcdonald",
    "blair",
    "cameron",
    "davies",
    "kier",
    "starmer"
    ]

#for i in range (1,53):
#    tfm.RemoveFile("data\\titles" + str(i) + ".txt")

for i in range (1,53):
    tfm.RemoveFile("data\\SearchedTitles" + str(i) + ".txt")

#pw.GetTitlesInElectionRange()

#wg.ResetDictionary()

#for i in range(1,52,1):
#    outputFile = "data\\titles" + str(i) + ".txt"
#    print(outputFile)
#    wg.ReadEachLine(outputFile)

#print("Writing files")
#wg.WriteOutWordsAndCountsKeySorted("WordsKeySorted.txt")
#wg.WriteOutWordsAndCountsValueSorted("WordsValueSorted.txt")


for i in range(1,52,1):
    inputFile = "data\\titles" + str(i) + ".txt"
    of = "data\\SearchedTitles" + str(i) + ".txt"
    print(of)
    wg.GetLinesContainingWordList(inputFile, searchTerms)
    wg.WriteOutSentances(of)
    wg.ResetSentanceList()