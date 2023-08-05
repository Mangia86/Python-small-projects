import random
print("Welcome to rock, paper and scissor")
print("Enter your choice:")
user_input=str(input()) #user will enter any option manually.
choices = ["rock", "paper", "scissor"] #computers options.
computer_input=random.choice(choices)
print("Computer's choice:")
print(computer_input)

while  user_input != 'rock' and user_input !='paper' and user_input !='scissor' :
#while user_input not in choices: #this is another way to re-write the above condition.    
    print("Enter your choice again, number between 1 and 3")
    user_input =str(input())
    
if (user_input =='rock' and computer_input=='paper'):
     print("Computer wins!!")
elif (user_input =='rock' and computer_input=='scissor'):
         print ("You Win!!")
elif (user_input =='paper' and computer_input=='scissor'):
         print("Computer win!!s")
elif (user_input =='paper' and computer_input=='rock'):
         print("You win!!")
elif (user_input =='scissor' and computer_input=='rock'):
         print("Computer wins!!")
elif (user_input =='scissor' and computer_input=='paper'):
    print("You win!!")
else:
    print("It's a Draw!!")