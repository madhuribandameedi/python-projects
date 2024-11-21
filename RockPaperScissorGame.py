import random
options=['Rock','Paper','Scissor']
name=input("Enter your name :")
Computer_Score=0
Player_Score=0
NumberOfRounds=0
gameOn=True
print("Welcome:",name)
while NumberOfRounds<5:
  ComputerOption=random.choice(options)
  PlayerOption=input("Enter Rock/ Paper/ Scissor :").title()
  print("Computer option:",ComputerOption)
  print(f"{name.title()} option :{PlayerOption}")
  NumberOfRounds += 1
  if ComputerOption==PlayerOption:
    print('Tie')
  elif (ComputerOption =='Rock' and PlayerOption== 'Scissor'):
      print("Computer wins")
      Computer_Score =Computer_Score+1
  elif(ComputerOption=='Scissor' and PlayerOption=='Paper'):
    print("Computer wins")
    Computer_Score =Computer_Score+1
  elif(ComputerOption=='Paper' and PlayerOption=='Rock'):
    print("Computer wins")
    Computer_Score =Computer_Score+1
  elif (PlayerOption=='Rock' and ComputerOption == 'Scissor'):
      print(f"{name.title()} wins")
      Player_Score =Player_Score+1
  elif(PlayerOption=='Scissor' and
  ComputerOption=='Paper'):
      print(f"{name.title()} wins")
      Player_Score =Player_Score+1
  elif(PlayerOption=='Paper' and ComputerOption=='Rock'):
      print(f"{name.title()} wins")
      Player_Score =Player_Score+1
  else:
    print("Choose a valid option to play this game.")
  print(f"Round No: {NumberOfRounds}")
  print("Score Board")
  print(f"{name.title()}: {Player_Score} | Computer: {Computer_Score}")
  if NumberOfRounds==5:
    gameOn=False
    break
if Player_Score==Computer_Score:
  print("tie!!")
elif Player_Score>Computer_Score:
  print(f"Congrats {name.title()}, You won the game!!")
else:
  print(f"Oops Computer won the game!! Better luck next time {name.title()}!")
print("Thanks for playing")