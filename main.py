############### Blackjack Project #####################
import random
import os

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card



def calculate_score(cards):
  if(sum(cards) == 21 and len(cards) == 2):
    return 0
  elif(11 in cards and sum(cards) > 21):
    cards.remove(11)
    cards.append(1)
  else:
    return sum(cards)




def printscores(user_score, user_cards, comp_score, computer_cards):
  print(f"Your Score : {user_score} \n Your Cards: {user_cards}")
  print(f"Computer Score : {comp_score} \n Computer Card: {computer_cards[0]}")
  


def compare(user_score, comp_score):
  if(user_score == comp_score):
    return ("Draw")
  elif(comp_score == 0):
    return ("You Lose!")
  elif(user_score == 0):
    return ("You Win!")
  elif(user_score > 21):
    return ("OverDrawn, You Lose! ")
  elif(comp_score > 21):
    return ("OverDrawn, You Win!")
  elif(user_score > comp_score):
    return ("You Win!")
  else:
    return ("You Lose!")



def play():
  from art import logo
  print(logo)

  user_cards = []
  comp_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())
  game_over = False

  
  while not game_over:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    

    printscores(user_score, user_cards, comp_score, comp_cards)
    
    if comp_score == 0 or user_score == 0 or user_score > 21:
      game_over = True
    else:
      ch = input("Do You want to draw another card? Y/N : ")
      if ch == "Y":
        user_cards.append(deal_card())
      else:
        game_over = True

  while comp_score != 0 and comp_score < 17:
    comp_cards.append(deal_card())
    comp_score = calculate_score(comp_cards)

  print(f"Your final hand is {user_cards} and your final score is {user_score}")
  print(f"Computer's final hand is {comp_cards} and computer final score is {comp_score}")

  print(compare(user_score, comp_score))



while input("Do You want to start a game of Blackjack? Y/N : ") == "Y":
  os.system('cls')
  play()
