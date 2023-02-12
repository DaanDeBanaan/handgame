#-----variables------#
p1h1, p1h2, p2h1, p2h2 = 1,1,1,1
game_end = False
#------functions------#
def checkloss(hand1, hand2):
  if hand1 == 0 and hand2 == 0:
    game_end = True
#------program------#
while game_end == False:
  print(f" {p2h1}        {p2h2} \n\n\n\n {p1h1}        {p1h2} \n\n")
  which_hand_attacks= input("Player 1, do you want to attack with your left or right hand? (l/r): ")
  which_hand_attacked = input("Player 1, do you want to attack the left or right hand? (l/r): ")
  if which_hand_attacks== "l":
    if which_hand_attacked == "l":
      p2h1 += p1h1
      if p2h1 >= 5:
        p2h1 -= 5
    elif which_hand_attacked == "r":
      p2h2 += p1h1
      if p2h2 >= 5:
        p2h2 -= 5
  elif which_hand_attacks== "r":
    if which_hand_attacked == "l":
      p2h1 += p1h2
      if p2h1 >= 5:
        p2h1 -= 5
    elif which_hand_attacked == "r":
      p2h2 += p1h2
      if p2h2 >= 5:
        p2h2 -= 5
  checkloss(p2h1, p2h2)
  print(f" {p1h1}        {p1h2} \n\n\n\n {p2h1}        {p2h2} \n\n")
  which_hand_attacks = input("Player 2, do you want to attack with your left or right hand? (l/r): ")
  which_hand_attacked = input("Player 2, do you want to attack the left or right hand? (l/r): ")
  if which_hand_attacks == "l":
    if which_hand_attacked == "l":
      p1h1 += p2h1
      if p1h1 >= 5:
        p1h1 -= 5
    elif which_hand_attacked == "r":
      p1h2 += p2h1
      if p1h2 >= 5:
        p1h2 -= 5
  elif which_hand_attacks == "r":
    if which_hand_attacked == "l":
      p1h1 += p2h2
      if p1h1 >= 5:
        p1h1 -= 5
    elif which_hand_attacked == "r":
      p1h2 += p2h2
      if p1h2 >= 5:
        p1h2 -= 5
  checkloss(p1h1, p1h2)