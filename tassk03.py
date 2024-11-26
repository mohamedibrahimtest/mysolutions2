import random 
words=["apple","orange","banana"]
orginal_word=random.choice(words)
word3=''.join(random.sample(orginal_word,len(orginal_word)))
print("welcome")
print(" welcome to the word guessing")
print(word3)
print("you have 5 choices")
attempts=5
while attempts > 0:
  guess=input("inter the word ")
  if guess==orginal_word:
    print("congratulations")
    break
  attempts-=1
  if  attempts >0 :
     print("try again")
  else :
     print("you lose the game")
