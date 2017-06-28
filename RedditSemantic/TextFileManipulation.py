import os

class TextFileManipulation(object):
    """Read and write to text file helpers"""

    def __init__(self, path = None):
        self.path = path 

    def SetFile(self, path):
        self.path = path

    def RemoveFile(self, path = None):
        filePath = path
        if path == None:
            filePath = self.path

        if filePath == None:
            print("No file path defined")
            return

        try:
            os.remove(filePath)
        except OSError as e:  ## if failed, report it back to the user ##
            print ("Error: %s - %s." % (e.filename,e.strerror))


    def WriteLine(self, text, path = None):
        filePath = path
        if path == None:
            filePath = self.path

        if filePath == None:
            print("No file path defined")
            return

        with open(filePath, "w") as appendFile:
            appendFile.write(text + "\n")

    def WriteLines(self, text, path = None):
        filePath = path
        if path == None:
            filePath = self.path

        if filePath == None:
            print("No file path defined")
            return

        with open(filePath, "a") as appendFile:
            for line in text:
                txt = line.encode('ascii', 'ignore').decode('ascii')
                appendFile.write(txt + "\n")
            