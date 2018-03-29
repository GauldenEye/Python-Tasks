import random
guesses=0

myName = input('Hello what is your name?')

print ('Hello, %s' % myName )

number =random.randint(1,20)

guess = int(input('Try and guess my number out of 20!'))

def guess_number():
  global guess
  global guesses

  if guess < number:
    print('Your guess is too low')
    guess = int(input('Guess again!'))
    guesses = guesses + 1 
    guess_number()
    return
  
  if guess > number:
    print('Your guess is too high')
    guess = int(input('Guess again!'))
    guesses = guesses + 1
    guess_number()
    return
  
  if guess == number:
    guesses = str(guesses)
    print('Congratulations, ' + myName + ' you guessed my number!')
    print('It took you: ' + guesses + ' guesses to guess my number' )
    
guess_number()