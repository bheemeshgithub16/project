import random

# List of possible choices
choices = ['rock', 'paper', 'scissors']

# Computer makes a random choice
comp = random.choice(choices)
# User input and normalization
user = input('Enter Your Choice (rock, paper, scissors): ').lower()

# Check if user input is valid
if user not in choices:
    print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
else:
    print(f"Computer choice is: {comp}")
    
    # Determine the winner
if comp == user:
    print('Draw')
elif (comp == 'rock' and user == 'paper') or \
     (comp == 'paper' and user == 'scissors') or \
     (comp == 'scissors' and user == 'rock'):
    print('You Won')
else:
    print('You Lost')
