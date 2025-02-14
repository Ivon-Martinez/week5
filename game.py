import random

#Play a game of Rock, Paper, Scissors with the computer
#Prompt the user to enter a value: R, P or S
#Convert the value into Rock, Paper, or Scissors
#Ask the computer to generate a random value between 0 and 2
#Convert the computer's choice. 0 becomes Rock, 1 becomes Paper, 2 becomes Scissors
#Compare the user's choice with the computer's choice to display and message indicating whether the user on, lost or drew against the computer

#Defined a function that prompt the user to enter an action between S, P or R
#At the same time the computer generate as integer from 0 to 2
#Created conditional to convert computer number to action

#**** method 1**** User pass character on console
def game():
    """ # document string
    this function plays the game Rock, Paper, Scissors
    this function prompt the user to enter a value
    User has to enter a value of S, P or R
    Function will generate a random value for the computer
    Both values are compared and a winner is selected
    return: str
    """
    action_user = input(f"Please enter which action would you like to play.\nPlease select from R, P or S")
    # return value_user
    action_computer = random.randint(0,2)
    convert = None
    if action_computer == 0:
        convert = 'R'
    elif action_computer == 1:
        convert = 'P'
    else :
        convert = 'S'
    print(f"The computer action is {convert}")

    # if action_user == action_computer:
    #     print("Draw! Please try again")
    if action_user == 'S' and convert == 'R' or action_user == 'P' and convert == 'S' or action_user == 'R' and convert == 'P':
        print('Sorry! Computer wins!')
    elif action_user == 'S' and convert == 'P' or action_user == 'P' and convert == 'R' or action_user == 'R' and convert == 'S':
        print('Congratulations! you are the winner!!')
    else:
        print("Draw! Please try again")
        game()

# if __name__ == "__main__":
#     game()










# print(type(action_computer))
    # convert = lambda a, b, c: 'R' if action_computer == 0 else ('P' if action_computer == '1' else 'S')
    # compare = lambda a, b: -1 if a < b else (+1 if a > b else 0)