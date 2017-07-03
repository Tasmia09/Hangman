import random
#the word file

#match variable will keep track of whether we should cut the hangman
global match
match = 0

wordList = ['hunger','world','programming','bother','smart','swear','fancy','education','science','learning','science','computer']
lifeLine = ['leg','leg','hand','hand','head']

'''theFile = open('wordFile.txt', 'w')
for item in word:
    theFile.writelines("%s\n" % item)

theFile.close()'''

#randomly picking the word to guess
guessedWord = wordList[random.randint(0,len(wordList)-1)]

#converting the string to array
guessedWordList = list(guessedWord)

#newList will hide the alphabets and display hyphens
newList = []

#printing
'''print(guessedWord)
print(guessedWordList)
print(guessedWord)'''



def removeLetter( guessWord ):
    
    for l in guessWord:
        newList.append("_")
        print('_',end=' ')
    #print(newList)

def startPlay():
    guess = input('\nEnter your guess: ')
    global match
    for index,char in enumerate(guessedWordList):
        if (guess == char):
            newList[index] = guess            
            match +=1
            
    if(match == 0):        
        lifeLine.pop(0)        
        
    print('You have ',len(lifeLine),' guesses left out of 5')
            
            

removeLetter(guessedWord)


while len(lifeLine)>0 and newList.count('_')!=0:
    match = 0
    startPlay()
    print (', '.join(lifeLine))
    print(*newList)
if(newList.count('_')==0):
    print('You Won! :D')
else:
    print('You Lost! :( \nthe word was ', guessedWord )



    
    
