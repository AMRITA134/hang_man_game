import random
def hang_man():
  # list of words to guess
  words=["apple","banana","berry","strawberry","watermelon"]
  word_to_guess=random.choice(words)
  guessed_letters=['_']*len(word_to_guess)
  attempts=6
  print("welcome to hangman")
  print("you have {} attempts to guess the word.".format(attempts))
  while True:
    print(" ".join(guessed_letters))
    user_guess=input("guess a letter: ")
    if user_guess.lower()=="quit":
      print("okay,the word was {}".format(word_to_guess))
      break
      if len(user_guess)!=1:
        print("please guess a single letter!")
        continue
    if user_guess in word_to_guess:
      print("good guess!")
      for i in range(len(word_to_guess)):
        if word_to_guess[i]==user_guess:
          guessed_letters[i]=user_guess
    else:
      print("wrong guess!")
      attempts-=1
      print("you have {} attempts left.".format(attempts))
    if "_" not in guessed_letters:
      print("congratulations! you guessed the word {}".format(word_to_guess))
      break
    elif attempts==0:
     print("sorry, you didn't guess the word : {}.".format(word_to_guess))
     break
hang_man()       