import pandas as pd

#For this exercise we will read the excel file and store the Questions and answers as lists.
df = pd.read_excel('Quiz.xlsx', sheet_name = 0) #Read the excel file as a data set
questions=list(df['Questions']) #define list variable based on the Questions Column from the excel file. It will be s
answers=(list(df['Answers']))#define list variable based on the Answers Column from the excel file

#print(df)
#print(questions)
#print(answers)

print("Let's start the game")
point= 1 #define variable point. How many points you want to win per correct question answered.
total_points= 0 #this is a counter to track you total amounts of points.

for  i in range (0,len(questions)): #We want to iterate through all the questions in the list. 0 is the starting questions and len(questions) is the last one.    
        print("\n")
        print(questions[i]) 
        print("Enter your answer: ")
        answer_user=str(input())
        
        if answers[i].upper()==answer_user.upper():# the answer typed by the user needs to be the same as the answer per the excel file
            print("\nYour answer is correct!!!")
            print(f"You win  {point}  point!!")
            total_points += point
            print(f"\nYour total points are:{total_points}" )
        else:
            print("Answer incorrect")
            #After this will start again the loop showing the next question. You can add as many questions and answers as you want
            
print(f"Game Over. You won a total of:  {total_points} points" )