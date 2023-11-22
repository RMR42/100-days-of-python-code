import random

# user = int(input('Pick one, Rock = 1, Paper = 2, Scissor = 3 '))
# computer = random.randint(1,3)


# this could have been done in dictionary format and avoid the if statements
def hand_symbols(choice):
        """
        To print the hand gesture whenever the user and the computer chooses
        """
        if choice==1:
                print('Rock')
                print("""
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
                """)
        elif choice== 2:
                print('Paper')
                print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
                """)
        elif choice==3:
                print('Scissors')
                print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
                """)


def who_wins(user,computer):
    if user==computer:
            print('its a draw!!')
            print('play again ')
    elif (user==1 and computer==3) or (user==2 and computer==1) or (user==3 and computer==1):
            print('User wins!!')
    else:
           print('computer wins ')


while True:
        user = int(input('Pick one, Rock = 1, Paper = 2, Scissor = 3 '))
        if 1<=user<=3:
                computer = random.randint(1,3)
                hand_symbols(user)
                print('\n')
                print('computer chooses')
                hand_symbols(computer)
                who_wins(user,computer)
        else:
               print('Enter a valid option. (1 or 2 or 3)')

        if input('Do you want to play again? (yes/no) ').lower() != 'yes':
               print('Thank you for playing!! ')
               break
