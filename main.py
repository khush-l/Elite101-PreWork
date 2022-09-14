import pyjokes
def run_joke(numJokes):
  int(numJokes)
  for i in range(numJokes):
    print(pyjokes.get_joke(language="en", category="neutral"))
    print('\n')
def word_find(sentence, find_word):#function to find key words
    if sentence.startswith(find_word + " "):
        return True
        startswithit=True
    if sentence.endswith(" " + find_word):
        return True
        endswithit=True
    if sentence.find(" " + find_word + " ") != -1:
        return True
    else:    
      return False
print("Hi, this is the chatbot")
answer=input('How are you doing?\n')
goodemotions=['well', 'excellent', 'really good', 'amazing','good','great',"yay", "happy" "great", "happy", "fantastic", "awesome", "good",]
bademotions=['terrible','really bad','sucks','dumb', "no", "bad", "awful", "hate", "tired", "sad", "no",  "awful", "hate", "tired", "sad", "No", "Awful", "Hate", "Tired", "Sad","awful", "hate", "tired", "not good", "sad", "not great"]
respondmyemotion= False
answer=answer.lower()
words=answer.split()
if (word_find(answer, "how are you"))==True or (word_find(answer, "how are you doing"))==True or (word_find(answer, "what about you"))==True or (word_find(answer, "how about you")) == True:
  respondmyemotion = True
else:
  pass
imdoing=False
im=False
if (word_find(answer, "I'm doing"))==True or (word_find(answer, "Im doing"))==True or (word_find(answer, "i'm doing"))==True or (word_find(answer, "im doing"))==True:
  imdoing=True
  if words[2] in goodemotions or words[2] in bademotions:
    answer=words[2]
  else:
    answer=words[3]
elif (word_find(answer, "i'm"))==True or (word_find(answer, "im"))==True:
  im=True
else:
  pass
if imdoing ==False and respondmyemotion== True and im==True:
  answer=words[1]
elif imdoing ==False and respondmyemotion== True and im==False:
  answer=words[0]
elif imdoing== False and respondmyemotion==False and im==True:
  if words[1] in goodemotions:
    answer=words[1]
  elif words[2] in goodemotions:
    answer=words[2]
  else:
    pass
if answer in goodemotions and respondmyemotion==True:
  print("That's excellent! I'm doing great")
elif answer in goodemotions and respondmyemotion == False:
  print("That's excellent!")
elif answer in bademotions: 
  answersad= input("Oh no, why are you feeling " + answer + "?\n")
  print("Sorry to here that")
answerjoke = input("Do you want to hear some jokes?(y/n)")
#answerjoke=answerjoke.toLower()
keepGoing=True
while keepGoing==True:
  if answerjoke=="yes" or answerjoke== "y":
    numJoke= input("How many jokes do you want to here?")
    numJoke1=int(numJoke)
    run_joke(numJoke1)
    moreJokes=input("Do you want to hear any more jokes?")
    if moreJokes == "no" or moreJokes == "n":
      exit()
  else:
    keepGoing==False
    exit()