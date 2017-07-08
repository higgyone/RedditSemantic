from TextFileManipulation import TextFileManipulation

class WordGetter(object):
    """description of class"""

    def __init__(self, path = None):
        self.path = path  
        self.wordsAndCounts = {}    
        self.sentances = []
        self.tmf = TextFileManipulation()

    def ResetDictionary(self):
        self.wordsAndCounts.clear()

    def ResetSentanceList(self):
        self.sentances.clear()

    def ReadEachLine(self, file, function = None):
        with open(file, 'r' ) as f:
            for line in f:
                if function == None:
                    self.ProcessLine(line)
                else:
                    function(line)        

    def ProcessLine(self, line):
         words = str(line).replace("\n", "")
         words = str(words).replace("\"", "")
         words = str(words).replace("\'", "")
         words = str(words).replace(",", "")
         words = str(words).replace(".", "")
         words = str(words).replace(":", "")
         words = str(words).replace("?", "")
         for word in str(words).split(" "):
             lWord = str(word).lower()
             if lWord in self.wordsAndCounts:
                 val = self.wordsAndCounts.get(lWord)
                 val = val + 1
                 self.wordsAndCounts[lWord] = val
             else:
                 self.wordsAndCounts[lWord] = 1

    def GetLinesContainingWordList(self, file, wordList):
        with open(file, 'r' ) as f:
            for line in f:
                for word in wordList:
                    if word in line:
                        self.sentances.append(line)
                        break 
        

    def WriteOutWordsAndCounts(self, outputFile):
        self.tmf.WriteDictLines(self.wordsAndCounts, outputFile)

    def WriteOutWordsAndCountsKeySorted(self, outputFile):
        self.tmf.WriteDictLinesSortedKey(self.wordsAndCounts, outputFile)

    def WriteOutWordsAndCountsValueSorted(self, outputFile):
        self.tmf.WriteDictLinesSortedValue(self.wordsAndCounts, outputFile)

    def WriteOutSentances(self, outputFile):
        self.tmf.WriteList(self.sentances, outputFile)
        