# This is a guess the number game.
import sys
import random
while True:
    secretNumber=random.randint(1,20)
    print('I am thinking of a number between 1 and 20.')
    
    for guessesTaken in range(1,7):
        try:
            print('Take a guess.')
            guess=int(input())
            if guess<secretNumber:
                print('Your guess is too low.')
            elif guess>secretNumber:
                print('Your guess is too high.')
            else:
                break 
        except:
            print ('Try numbers, okay?')
            continue
    
    if guess==secretNumber:
       print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
       print('That was fun! Do you want to play again?')
       response=input()
       response=(response.lower())
       while response!='no' and response!='n' and response!='yes' and response!='y':
           print ('Que? Do you want to play again?')
           response=input()
           response=(response.lower())
       if response=='Yes' or response=='yes' or response=='y':
           continue
       elif response=='No' or response=='no' or response=='n':
            print('Until next time!')
            sys.exit()           
    else:
       print('Nope. The number I was thinking of was ' + str(secretNumber))
       print('That was fun! Do you want to play again?')
       response=input()
       response=(response.lower())
       while response!='no' and response!='n' and response!='yes' and response!='y':
           print ('Que? Do you want to play again?')
           response=input()
           response=(response.lower())
       if response=='Yes' or response=='yes' or response=='y':
           continue
       elif response=='No' or response=='no' or response=='n':
            print('Until next time!')
            sys.exit()      
    
