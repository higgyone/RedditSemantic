from TextFileManipulation import TextFileManipulation

class WordGetter(object):
    """description of class"""

    def __init__(self, path = None):
        self.path = path  
        self.wordsAndCounts = {}    
        self.tmf = TextFileManipulation()

    def ReadEachLine(self, file, function = None):
        with open(file, 'r' ) as f:
            for line in f:
                if function == None:
                    self.ProcessLine(line)
                else:
                    function(line)        

    def ProcessLine(self, line):
         words = str(line).replace("\n", "")
         for word in str(words).split(" "):
             lWord = str(word).lower()
             if lWord in self.wordsAndCounts:
                 val = self.wordsAndCounts.get(lWord)
                 val = val + 1
                 self.wordsAndCounts[lWord] = val
             else:
                 self.wordsAndCounts[lWord] = 1

    def WriteOutWordsAndCounts(self, outputFile):
        self.tmf.WriteDictLines(self.wordsAndCounts, outputFile)
        
        


