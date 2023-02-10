from art import logo, vs
from game_data import data
import random
import os

def clear():
  os.system('clear')

game_continue = True
score = 0 

def correct_answer(ans1,ans2):
  if ans1['follower_count'] > ans2['follower_count']:
    return 'A'
  else:
    return 'B'

def current_score(score):
  if score == 0:
    return
  else:
    print(f"You're right! Current score: {score}")
  
  
def higher_lower():
  choiceA = random.choice(data)
  choiceB = random.choice(data)
  while choiceA==choiceB:
    choiceB = random.choice(data)
  print(f"Compare A: {choiceA['name']}, a {choiceA['description']}, from {choiceA['country']}")
  print(vs)
  print(f"Against B: {choiceB['name']}, a {choiceB['description']}, from {choiceB['country']}")
  response = input("Who has more followers? Type 'A' or 'B' ")
  answer = correct_answer(choiceA,choiceB)
  
  if response == answer:
    return 1
  else:
    return 0

while game_continue:
  print(logo)
  current_score(score)
  result = higher_lower()
  if result == 1:
    score += 1
    clear()
  else:
    clear()
    game_continue = False
    print(logo)
    print(f"Game Over! Your score is {score}.")
  
    
  

  
  
