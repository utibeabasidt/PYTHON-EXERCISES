import random

user_wins = 0
computer_wins = 0
playing = True

while playing:
  computer_guess = random.randint(1, 10)
  try: 
    user_guess = int(input('Guess a number from 1-10: '))
    if user_guess > 10:
      print('Number should not be greater than 10. Try again.')
      continue
    elif user_guess == computer_guess:
      print('You win!')
      user_wins += 1
    else:
      print('You lose. Better luck next time!')
      computer_wins += 1
    
    print(f'Your guess: {user_guess}, Secret number: {computer_guess}')
    print(f'Your wins: {user_wins}, Computer wins: {computer_wins}')
  except ValueError:
    print('Invalid input. Please enter a number.')
    continue
  
  while True:
    user_choice = input('Play again? (y/n): ').lower()
    if user_choice == 'n':
      playing = False
      print(f'Final score - You: {user_wins}, Computer: {computer_wins}. Thanks for playing!')
      break
    elif user_choice == 'y':
      break
    else:
      print('Invalid choice. Please enter y or n.')
      continue

'''Note: Break is for exiting the loop completely, while continue is for skipping the current iteration and moving to the next one, which would mean repetition of the while loop.'''