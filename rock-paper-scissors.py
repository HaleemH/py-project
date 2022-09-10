import random

name = input('What is your name: ')
score =[0,0]

print(f'Hi {name}')
def match():
  if score[0] == 0 and score[1] == 0:
    print(f'Let\'s get started')
  elif score[0] == 3:
    print('You WON!!!! CONGRATULATIONS!!!')
    quit() 
  elif score[1] == 3:
    print('Sorry you lost. Better luck next time.')
    quit()
  else:
    print(f'Current Score: {name}: {score[0]} - CPU: {score[1]}')

  choice = input('Type you answer ( Rock, Paper, Scissors): ')
  print(f'You  chose: {choice}')
  if choice.lower() == "rock" or choice.lower() == "paper" or choice.lower() == "scissors": 
    cpu_choice = random.choice(['rock','paper','scissors'])
    win(choice, cpu_choice)
  else:
    print("Please choose between: Rock | Paper | Scissors")
    match()

def win(user,cpu):
    if (user == 'rock' and cpu == 'scissors') or (user == 'scissors' and cpu == 'paper') or (user == 'paper' and cpu == 'rock'):
        print('You got me!')
        score[0] +=1
        match()
    elif user == cpu:
        print(' Tie! ')
        match()
    else:
        print('I won this round')
        score[1] +=1
        match()

match()