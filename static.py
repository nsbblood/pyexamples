class WordSet:
    def __init__(self):
        self.words=set()

    def addText(self,text):
        text=self.cleanText(text)

    def cleanText(self,text):
        text=text.replace('!', '').replace('.','')

wordSet=WordSet()

wordSet.addText('hi, I\'m Ryan! Here is a sencte!')
wordSet.addText(' Here is another sencte!')


