def main():
    bookPath = "books/frankenstein.txt"
    print (f"--- Begin report of {bookPath} ---")

    file_contents = openBook(bookPath)
    wordCount = wordCounter(file_contents)
    print(f"{wordCount} words found in the document\n")

    charCount = charCounter(file_contents)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lettersOfAlphabet = list(alphabet)
    dicOfDics = labelDicValues(charCount,lettersOfAlphabet)
    for i in range(len(dicOfDics)):
        currentDict = dicOfDics.pop(0)
        print(f"The '{currentDict["Letter"]}' character was found {currentDict["Count"]} times")
    print (f"--- End report ---")

def openBook(closedBook):
    with open(closedBook) as f:
        return f.read()

def wordCounter(fileAsString):
    words = fileAsString.split()
    #print(f"wordCounter: {words}")
    return len(words)

# takes the text from the book as a string, 
#and returns the number of times each character appears 
#in the string. Convert any character to lowercase
def charCounter(words):
    lowercaseWords = words.lower()
    letterCountDic ={}
    x = 0
    for letter in lowercaseWords:
        if letterCountDic.get(letter) == None:
            letterCountDic.update({letter:1})
        else:
            x = letterCountDic.get(letter)
            letterCountDic.update({letter:x+1})
    return letterCountDic

def labelDicValues(dict,letters):
    labeledDict = []
    for letter in letters:
        labeledDict.append({"Letter":letter,"Count":dict[letter]})
   # print(labeledDict)
       # labeledDict = {"value":dic[value]}
    labeledDict.sort(reverse=True, key=sort_on)
    return labeledDict

def sort_on(dict):
    return dict["Count"]
       


main()