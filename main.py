import os
import random
import time
import pickle
import subprocess

def clear():
  os.system('clear')

shellscript = subprocess.Popen(["./autocommit.sh"], stdin=subprocess.PIPE)
returncode = shellscript.wait()   

save_file_name = 'game_state.pkl'
choice = ''
reset = "\033[0m"
bold = "\033[1m"
green = "\033[0;32m"
gold = "\033[0;33m"
cyan = "\033[0;36m"
magenta = "\033[0;35m"
red = "\033[0;31m"
blue = "\033[0;34m"
yellow = "\033[0;33m"
locations = [
    "Safe House",
    "Abandoned Store",
    "Hospital",
    "Police Station",
    "Warehouse",
]
player = {
    "name": "",
    "health": 100,
    "inventory": {
        "weapon": "fists",
        "food": 2,
        "armor": "none"
    },
    "hunger": 0,
    "days_survived": 1,
    "Coins": 0,
    "location": "...",
}
mark_reduction = 0

print('V1.51')
print("GitHub Save system")
print("Save system fixed")
print("Weapon/armor upgrade system \nMore balanced gameplay")
horde_multiplier = 1.4


def new_game():
  print('===Choose Your Character===')
  print(
      f"\n(1) {bold}Sam{reset}: Sam is a person who likes to keep food in his bags all the time. {green}You start with 6 food and 135 health!{reset} \n(2) {bold}Bob{reset}: Bob is a person who doesn't eat food as much. {green}He gets hungry slower{reset} \n(3) {bold}Joe{reset}: Joe is a talented mathematician. {green}Maths minigame score +1{reset}  \n(4) {bold}Mark{reset}: Mark is a Muay Tha fighter, {green}doesn't lose as much health{reset} when fighting zombies"
  )
  character = input("Choose your character: 1/2/3/4")
  mark_reduction = 0
  if character == '1':
    player['name'] = 'Sam'
  if player['name'] == 'Sam':
    player["inventory"]["food"] = 6
    player['health'] = 135
  elif character == '2':
    player['name'] = 'Bob'
  elif character == '3':
    player['name'] = 'Joe'
  elif character == '4':
    player['name'] = 'Mark'
  if player['name'] == 'Mark':
    mark_reduction = random.randint(15, 40)
  else:
    mark_reduction = 0
  print("You woke up one day and you found yourself")
  input("Enter...")
  print(f"You find yourself in the midst of a {red}zombie apocalypse.{reset}")
  input("Enter...")
  call = input("Do you want to call your girlfriend? y/n").lower()
  if call == 'y':
    print("You tried to call your girlfriend", end='')
    for _i in range(5):
      time.sleep(1)
      print(".", end='', flush=True)
    print("\nYou: Where are you!")
    input("")
    print("Her: I was saved by the military. Your city is on lockdown")
    input("")
    print(
        "Her: I'll come to your aid in four weeks. However, if you don't survive, I may have to find someone else."
    )
    print(
        f'I have given you some {green}Tips{reset} to survive there. Good luck!'
    )
    print("\n\n")
    print("Signal lost....")
    time.sleep(1)
    print(f"====={green}Tips{reset}=====")
    print(
        "--Your girlfriend is coming to help you in 4 weeks. So, DONT DIE...")
    print(
        f"\n{red}Be aware of your Hunger level. Your health might decrease if it exceeds {cyan}4{reset}"
    )
    input("Press Enter..")
    print(
        f"Your hunger level cannot go below {red}zero{reset}. {bold}Don't eat too much{reset}"
    )
    input("Press Enter..")
    print(f"{green}Fighting zombies my earn you some rewards!{reset}")
  else:
    print(
        "What a pity Your girlfriend could have given you some tips to survive! Anyways, you are alone and don't know what to do. Try to surive"
    )


def math_quiz():
  find_opponent = random.random()
  print("You are finding a zombie to be your opponent...")
  zombie_opp = [
      'Police officer', 'High school student', 'Engineer', 'Physicist',
      'Mathematician'
  ]
  zombie_opp_ran = random.choice(zombie_opp)
  zombie_score = zombie_opp.index(zombie_opp_ran)
  time.sleep(3)
  if find_opponent < 0.8:
    print("You found an opponent!")
    time.sleep(1)
    print(f"He was a {zombie_opp_ran} with some coins in his pocket")
    time.sleep(1)
    print(
        f"He's challenging you to a maths minigame answer each one within {bold}4 seconds{reset}"
    )
    input("Press enter")
  else:
    print(
        f"You didn't find an opponent you wasted your time and energy to find an opponent...{red}Hunger+2.5{reset}"
    )
    player['hunger'] += 2

    return
  zombie_maths = random.randint(zombie_score + 1, 7)
  correct_answers = 0
  if player['name'] == 'Joe':
    correct_answers += 1
  for _ in range(7):
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    operator = random.choice(['+', '-', 'x'])
    question = f"{num1} {operator} {num2} = ?"
    print(f"\nMath Quiz: {question}")

    start_time = time.time()
    answer = input("Your answer: ")

    try:
      answer = int(answer)
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    elapsed_time = time.time() - start_time

    if elapsed_time <= 4:
      if operator == '+':
        correct_result = num1 + num2
      elif operator == '-':
        correct_result = num1 - num2
      elif operator == 'x':
        correct_result = num1 * num2

      if answer == correct_result:
        print("Correct!")
        correct_answers += 1
      else:
        print("Incorrect!")
    else:
      print("Time's up! You didn't get a point for this question.")
  if zombie_maths > correct_answers:
    if player['name'] == 'Joe':
      print("Score +1")
    print(f"The zombie got {zombie_maths} questions!")
    print(
        f"You answered {correct_answers} questions correctly you lost {(zombie_maths - correct_answers)*3} coins!"
    )
    print("You lost the math quiz! Better luck next time!")
  elif zombie_maths == correct_answers:
    if player['name'] == 'Joe':
      print("Score + 1")
    print(
        f"You got {correct_answers} questions right! So did the zombie! You earn no coins at all"
    )
  elif zombie_maths < correct_answers:
    if player['name'] == 'Joe':
      print("Score + 1")
    print(
        f"You are better than a {zombie_opp_ran} with a half of his brain. You got {correct_answers} questions right and the zombie got {zombie_maths}! You won {(correct_answers - zombie_maths)*3} coins!"
    )
  earned_coins = (correct_answers - zombie_maths) * 3
  player['Coins'] += earned_coins
  if player['Coins'] < 0:
    player['Coins'] = 0


def display_food_emoji(food_level):
  return "🍖" * food_level


def save_game(player, horde_multiplier):
  save_data = {
      'player': player,
      'horde_multiplier': horde_multiplier,
  }
  with open(save_file_name, 'wb') as file:
    pickle.dump(save_data, file)
  shellscript = subprocess.Popen(["./autocommit.sh"], stdin=subprocess.PIPE)
  returncode = shellscript.wait()   


def load_game():
  try:
    with open(save_file_name, 'rb') as file:
      save_data = pickle.load(file)
    return save_data['player'], save_data['horde_multiplier']
  except FileNotFoundError:
    return None, None
  shellscript = subprocess.Popen(["./autocommit.sh"], stdin=subprocess.PIPE)
  returncode = shellscript.wait()   
  clear()


print("Do you want to (1) Load the game or (2) Start a new game?")
choice = input("Enter your choice: ")
if choice == "1":
  save_name = input("Enter the name of your save(Exactly letter by letter):")
  save_file_name = f'game_state_{save_name}.pkl'
  player, horde_multiplier = load_game()
  if player is None or horde_multiplier is None:
    print("Failed to load the game. Starting a new game.")
    player = {
        "name": "",
        "health": 100,
        "inventory": {
            "weapon": "fists",
            "food": 2,
            "armor": "none"
        },
        "hunger": 0,
        "days_survived": 1,
        "Coins": 0,
        "location": "...",
    }
    new_game()
    horde_multiplier = 1.4
  else:
    print("Game loaded successfully.")
elif choice == "2":
  pass
else:
  print("Invalid choice. Starting a new game.")
  new_game()
if choice == '2':
  new_game()



coin_probability = 0.6

weapons_list = [
    "fists", "baseball bat", "knife", "machete", "shotgun", "assault rifle"
]
armor_names = [
    "none",
    "Leather Jacket",
    "Cloth Robe",
    "Leather Armor",
    "Iron Armor",
    "Chainmail",
    "Plate Armor",
    "Kevlar Vest",
]
events = [
    "You found a fridge and find some food.",
    "A group of zombies approaches, what would you do?",
    "You find a first-aid kit and heal some of your wounds.",
    "You come across a survivor who gives you a weapon.",
    "You're going out to find some food",
    "A zombie horde is chasing you, and you need to escape.",
    "You find a hidden cache of supplies, including food and some small parts of the first-aid kit.",
    "You encounter a lone zombie and must decide whether to fight or sneak past it.",
]


def display_status():
  global new_location
  while True:
    secret_location = random.randint(1, 6)
    enter_input = input("Press Enter...")
    print(
        f"\n(1)Safe House\n(2)Abandoned Store \n(3)Hospital \n(4)Police Station \n(5)Warehouse"
    )
    new_location = input("Where do you want to go next? 1/2/3/4/5\n:")
    if new_location.isdigit():
      new_location = int(new_location)
      if 1 <= new_location <= 5:
        break
      else:
        print("Invalid choice. Please choose a number between 1 and 5.")
    else:
      print("Invalid input. Please enter a number.")
  if secret_location == new_location:
    time.sleep(1)
    random_coins_events = random.randint(1, 5)
    str_location = locations[new_location - 1]
    if random_coins_events == 1:
      print(
          f"During the trip to the {str_location}, you encountered a dying man who gave you some coins before he passed away"
      )
    elif random_coins_events == 2:
      print(
          f"While exploring a dilapidated building on your way to the {str_location}, you stumble upon a hidden stash of coins hidden in a dusty old chest."
      )
    elif random_coins_events == 3:
      print(
          f"As you make your way to the {str_location}, you notice an abandoned vehicle by the roadside. Upon searching it, you find some coins hidden in the glove compartment."
      )
    elif random_coins_events == 4:
      print(
          f"While traveling to the {str_location}, you find a weathered map with cryptic markings. Upon deciphering it and following the clues, you unearth a buried treasure chest filled with coins."
      )
    elif random_coins_events == 5:
      print(
          f"On your journey to the {str_location}, you come across a survivor in distress. After helping them fend off some zombies, they express their gratitude by giving you a handful of coins."
      )
    time.sleep(2)
    earn_coins()
  new_location = locations[new_location - 1]
  if new_location == player['location']:
    print(player['name'], "has decided to stay at", player['location'])
  else:
    print("You are going to the", new_location)
    for _i in range(3):
      time.sleep(0.5)
      print(".", end='', flush=True)

  player['location'] = new_location
  print(f"\n{bold}Name:{reset} {player['name']}")
  player['health'] = round(player['health'], 1)
  print(f"{bold}Health: {green}{player['health']} {reset}")
  print(f"{bold}Weapon:{reset} {player['inventory']['weapon']}")
  print(f"Food: {display_food_emoji(player['inventory']['food'])}")
  print(f"{bold}Armor:{reset} {player['inventory']['armor']}")
  print(f"{bold}Hunger:{red}{player['hunger']}{reset}")
  print(f"{bold}Days Survived: {blue}{player['days_survived']}{reset}")
  print(f"{bold}Coins: {gold}{player['Coins']}{reset}")
  print(f"{bold}Location:{reset} {player['location']}")


weapon_rank = weapons_list.index(player['inventory']['weapon'])
armor_rank = armor_names.index(player['inventory']['armor'])


def handle_event():
  event = random.choice(events)
  clear()
  print(
      f"{'==='} {'Days Survived:'}{blue}{player['days_survived']}{reset}{'==='}"
  )
  print("Don't let your hunger level exceed 5!!!")
  print(event)
  if "zombies" in event:
    fight_or_run()
  elif "cache" in event:
    find_cache()
  elif "food" in event:
    find_food()
  elif "weapon" in event:
    find_weapon()
  elif "heal" in event:
    heal_wounds()
  elif "escape" in event:
    escape_zombies()
  elif "encounter" in event:
    encounter_zombie()

  if random.random() < coin_probability:
    earn_coins()

  player['days_survived'] += 1


def store():
  print(f"{bold}Welcome to the Shop!{reset}")
  print("Here are the items available for purchase:")
  print("1. 3 Foods (10 coins)")
  print("2. Armors  - Provides protection.")
  print("3. First-aid kit (15 coins) - Restores health.")
  print("4. Weapons  - Improves combat capabilities.")
  choice = input("Enter the number of the item you want to buy (1/2/3/4): ")

  if choice == "1":
    buy_food()
  elif choice == "2":
    buy_armor()
  elif choice == "3":
    buy_healing_item()
  elif choice == "4":
    buy_weapon()
  else:
    print("Invalid choice. Please choose a valid option.")
    time.sleep(2)


def buy_food():
  if player["Coins"] >= 10:
    player["Coins"] -= 10
    player["inventory"]["food"] += 3
    print("You bought food")
  else:
    print("You don't have enough coins to buy food.")


def buy_armor():
  armors = {
      f"{gold}Leather Jacket":
      ("Leather Jacket", 10,
       "A basic leather jacket that provides some protection."),
      "Cloth Robe":
      ("Cloth Robe", 15,
       "A simple cloth robe that doesn't offer much protection."),
      "Leather Armor":
      ("Leather Armor", 17, "Lightweight leather armor for agility."),
      "Iron Armor":
      ("Iron Armor", 20, "A sturdy iron armor that offers good protection."),
      "Chainmail": ("Chainmail", 30,
                    "A chainmail suit that provides decent defense."),
      "Plate Armor": ("Plate Armor", 40,
                      "Heavy plate armor for maximum protection."),
      "Kevlar Vest": ("Kevlar Vest", 50,
                      f"Kevlar vest for excellent protection.{reset}")
  }

  print("Available armors:")
  for armor, (armor_name, cost, description) in armors.items():
    print(f"{gold}{armor_name} ({cost} coins) - {description}{reset}")

  choice = input("Enter the name of the armor you want to buy or upgrade: "
                 ).strip().title()
  if choice in armors:
    current_armor = player['inventory']['armor']
    if current_armor == 'none' or armors[current_armor][1] >= armors[choice][1]:
      if player['Coins'] >= armors[choice][1]:
        player['Coins'] -= armors[choice][1]
        player['inventory']['armor'] = choice
        print(f"You bought a {choice}")
      else:
        print("You don't have enough coins to buy or upgrade this armor.")
    else:
      print(
          f"You are upgrading your armor by only paying the prie difference! {current_armor}. Do you want to upgrade? (y/n): "
      )
      upgrade_choice = input()
      if upgrade_choice.lower() == 'y':
        price_difference = armors[choice][1] - armors[current_armor][1]
        if player['Coins'] >= price_difference:
          player['Coins'] -= price_difference
          player['inventory']['armor'] = choice
          print(
              f"{green}You upgraded to a {choice} by paying the price difference of {price_difference} coins.{reset}"
          )
        else:
          print(f"You don't have enough coins to upgrade to {choice}.")
      else:
        print("Upgrade canceled.")
  else:
    print("Invalid armor choice.")


def buy_weapon():
  weapons = {
      "baseball bat":
      ("baseball bat", 15, "A sturdy baseball bat that packs a punch."),
      "knife": ("knife", 20, "A really sharp knife"),
      "machete": ("machete", 25, "A good weapon to kill someone"),
      "shotgun":
      ("shotgun", 30, "A powerful shotgun that deals massive damage."),
      "assault rifle": ("assault rifle", 40, f"The best weapon you can find")
  }

  print("Available weapons:")
  for weapon, (weapon_name, cost, description) in weapons.items():
    print(f"{magenta}{weapon_name} ({cost} coins) - {description}{reset}")

  choice = input(
      "Enter the name of the weapon you want to buy or upgrade: ").lower()
  if choice in weapons:
    current_weapon = player['inventory']['weapon']
    if weapons_list.index(current_weapon) >= weapons_list.index(
        choice) or current_weapon == 'fists':
      if player['Coins'] >= weapons[choice][1]:
        player['Coins'] -= weapons[choice][1]
        player['inventory']['weapon'] = choice
        print(f"You bought a {choice}")
      else:
        print("You don't have enough coins to buy or upgrade this weapon.")
    else:
      print(
          f"You are upgrading your weapon by paying the price difference from: {current_weapon}. Do you want to upgrade? (y/n): "
      )
      upgrade_choice = input()
      if upgrade_choice.lower() == 'y':
        price_difference = weapons[choice][1] - weapons[current_weapon][1]
        if player['Coins'] >= price_difference:
          player['Coins'] -= price_difference
          player['inventory']['weapon'] = choice
          print(
              f"{green}You upgraded to a {choice} by paying the price difference of {price_difference} coins.{reset}"
          )
        else:
          print(f"You don't have enough coins to upgrade to {choice}.")
      else:
        print("Upgrade canceled.")
  else:
    print("Invalid weapon choice.")


def earn_coins():
  coins_earned = random.randint(1, 5)
  player["Coins"] += coins_earned
  time.sleep(1.5)
  print(f"You found {coins_earned} coins!")


def fight_or_run():
  print("\nZombies are approaching!")
  choice = input(
      "Do you want to (f) fight, (r) run, or (e) eat food? ").lower()
  if choice == "f":
    fight_zombies()
  elif choice == "r":
    print("You run away from the zombies.")
  elif choice == "e":
    eat_food()
  else:
    print("Invalid choice. The zombies catch up to you!")
    fight_zombies()


def fight_zombies():
  print("\nYou engage in battle with the zombies!")
  damage_reduction_weapon = random.randint((weapon_rank + 1) * 4,
                                           ((weapon_rank + 3) * 4))
  if weapon_rank == 0:
    damage_reduction_weapon = 0
  base_damage = random.randint(5, 55)

  damage_reduction_armor = random.randint((weapon_rank + 3) * 3,
                                          ((weapon_rank + 5) * 3))
  if armor_rank == 0:
    damage_reduction_armor = 0
  damage_reduction = damage_reduction_armor + damage_reduction_weapon + mark_reduction

  total_damage = max(0, base_damage - damage_reduction)

  zombie_damage = random.randint(12, 15)
  player['health'] -= total_damage

  print(f"You deal {zombie_damage} damage to the zombies.")
  print(f"{red}You lost {total_damage} health during the fight{reset}")

  if player['health'] <= 0:
    print("You have been overwhelmed by zombies. Game over!")
    exit()
  else:
    print(f"Your health: {player['health']}")
    if random.random() < 0.85:
      reward = random.choice(["food", "weapon", "armor", "food"])
      get_reward(reward)


def get_reward(reward):
  print("You found something during the fight!")
  time.sleep(2)
  if reward == "food":
    food_found = random.randint(1, 4)
    player['inventory']['food'] += food_found
    print(f"You find {food_found} food items.")
  elif reward == "weapon":
    new_weapon = random.choice(weapons_list)
    if weapons_list.index(new_weapon) > weapons_list.index(
        player['inventory']['weapon']):
      player['inventory']['weapon'] = new_weapon
      print(f"You find a {new_weapon}. It's better than your current weapon.")
    elif new_weapon == 'fists':
      print("A cat stole it from you, you coudn't catch it..")
    else:
      print("You found...", (new_weapon),
            "but it's not any better than your current weapon")
  elif reward == "armor":
    armor_found = random.choice(armor_names)
    if armor_names.index(armor_found) > armor_names.index(
        player['inventory']['armor']):
      player['inventory']['armor'] = armor_found
      print(f"You find a {armor_found}. It's better than your current armor.")
    elif armor_found == 'none':
      print("A random survivor stole it from you when you were picking it up!")
    else:
      print(
          "The armor you found is not any better than what you have already..."
      )


def find_food():
  food_found = random.randint(1, 3)
  player['inventory']['food'] += food_found
  player['health'] += 2
  print(f"You find {food_found} food items.")
  print(f"Total food in inventory: {player['inventory']['food']}")


def find_weapon():
  new_weapon = random.choice(weapons_list)
  if weapons_list.index(new_weapon) > weapons_list.index(
      player['inventory']['weapon']):
    player['inventory']['weapon'] = new_weapon
    print(f"You find a {new_weapon}. It's better than your current weapon.")
  elif new_weapon == 'fists':
    print("You thought you found something but it was just a hallucination")
  else:
    print("You found...", (new_weapon),
          "but it's not any better than your current weapon")


def heal_wounds():
  heal_amount = random.randint(10, 30)
  player['health'] += heal_amount
  print(
      f"You use a first-aid kit to heal yourself and gain {heal_amount} health."
  )
  print(f"Your health: {player['health']}")


def escape_zombies():
  print("\nA horde of zombies is chasing you! Will you make it?")
  escape_chance = random.randint(1, 6)
  time.sleep(2)
  if escape_chance > 2:
    print("You manage to escape and find a safe spot.")
  else:
    if player['name'] == 'Mark':
      print(
          "Luck is really not on your side. You are unable to escape and get surrounded by zombies... but because Mark is a Muay Thai fighter he managed to get out with a half of his health!"
      )
      player['health'] /= 2
    else:
      print(
          "Luck is really not on your side. You are unable to escape and get surrounded by zombies... You managed to get out with a quater of your health!"
      )
      player['health'] /= 4


def find_cache():
  print("\nYou discover a hidden cache of supplies!")
  food_found = random.randint(2, 5)
  aid_parts = random.randint(1, 7)
  player['inventory']['food'] += food_found
  print(f"You find {food_found} food items and gain {aid_parts} health.")
  player['health'] += aid_parts
  print(f"Total food in inventory: {player['inventory']['food']}")


def encounter_zombie():
  print("\nYou encounter a lone zombie.")
  choice = input(
      "Do you want to (f) fight, (s) sneak past it, or (e) eat food? ").lower(
      )
  if choice == "f":
    fight_zombies()
  elif choice == "s":
    print("You manage to sneak past the zombie and avoid a confrontation.")
  elif choice == "e":
    eat_food()
  else:
    print("Invalid choice. The zombie notices you!")
    fight_zombies()


def eat_food():
  if player['inventory']['food'] > 0:
    while True:
      try:
        amount_to_eat = int(
            input("Enter the amount of food to eat (0 to cancel): "))
        if amount_to_eat < 0:
          print("Invalid input. Please enter a non-negative number.")
        elif amount_to_eat == 0:
          print("Canceled eating food.")
          break
        elif amount_to_eat <= player['inventory']['food']:
          player['inventory']['food'] -= amount_to_eat
          if player['name'] == 'Bob':
            player['hunger'] -= (amount_to_eat) + 0.75
          else:
            player['hunger'] -= (amount_to_eat) + 1
          player['health'] += 2 * amount_to_eat
          print(
              f"You ate {amount_to_eat} food and feel less hungry. You also gained {2 * amount_to_eat} health."
          )
          break
        else:
          print("You don't have enough food to eat that much.")
      except ValueError:
        print("Invalid input. Please enter a valid number.")
  else:
    print("You don't have any food left to eat!")


def horde_night():
  global horde_multiplier
  horde_multiplier += 1
  player['days_survived'] += 1
  print(f"\n {red}It's the last night of the week which is a Horde Night...")
  time.sleep(3)
  print(f"You encounter a zombie horde{reset}")
  time.sleep(2.5)
  damage_reduction_weapon = random.randint((weapon_rank + 1) * 4,
                                           ((weapon_rank + 3) * 4))
  if weapon_rank == 0:
    damage_reduction_weapon = 0
  base_damage = random.randint(15, 50) * horde_multiplier

  damage_reduction_armor = random.randint((weapon_rank + 3) * 3,
                                          ((weapon_rank + 5) * 3))
  if armor_rank == 0:
    damage_reduction_armor = 0
  damage_reduction = damage_reduction_armor + damage_reduction_weapon + mark_reduction

  total_damage = max(0, base_damage - damage_reduction)
  total_damage = round(total_damage, 1)
  zombie_damage = random.randint(12, 15)
  player['health'] -= total_damage
  player['health'] = round(player['health'], 1)
  print(f"You deal {zombie_damage} damage to the zombies.")
  print(f"{red}You lost {total_damage} health during the fight{reset}")
  if player['health'] <= 0:
    print("You have been overwhelmed by zombies. Game over!")
    exit()
  else:
    print(f"{green}Your health: {player['health']}{reset}")
    if random.random() < 0.75:
      reward = random.choice(["food", "weapon", "armor", "food"])
      get_reward(reward)


f = open('title.text', 'r')
print(''.join(list(f)))
print(
    f"Welcome to {red}Don't Die ToGetHer{reset} by {magenta}Warot Komontree{reset}"
)
print("Press enter to continue...")
input("")

ask_location = True
while player['days_survived'] <= 28:
  if ask_location == True:
    display_status()
  else:
    ask_location = True
  print("\nOptions:")
  print("(1) Advance")
  print("(2) Eat food")
  print("(3) Maths Minigame")
  print("(4) Shop")
  print("(5) Save Game(only works on local computer(Prem's computer!))")

  if player['days_survived'] % 7 != 0:
    choice = input("Choose an option: ")
    if choice == "1":
      handle_event()
      if player['name'] == 'Bob':
        player['hunger'] += 0.75
        if player['hunger'] < 0:
          player['hunger'] = 0
      else:
        player['hunger'] += 1
        if player['hunger'] < 0:
          player['hunger'] = 0
    elif choice == "2":
      eat_food()
      if player['name'] == 'Bob':
        player['hunger'] += 0.75
        if player['hunger'] < 0:
          player['hunger'] = 0
      else:
        player['hunger'] += 1
        if player['hunger'] < 0:
          player['hunger'] = 0
    elif choice == "3":
      if player['Coins'] > 3:
        math_quiz()
        if player['name'] == 'Bob':
          player['hunger'] += 0.25
          if player['hunger'] < 0:
            player['hunger'] = 0
        else:
          player['hunger'] += 0.5
          if player['hunger'] < 0:
            player['hunger'] = 0
        player['days_survived'] += 1

      else:
        print("You don't have enough coins to play the maths minigame.")
    elif choice == "4":
      store()
      ask_location = False
    elif choice == "5":
      save_name = input(
          "Enter the name of your save(Exactly letter by letter):")
      save_file_name = f'game_state_{save_name}.pkl'
      save_game(player, horde_multiplier)
      print("Game saved successfully.")
    else:
      print("Invalid choice.")
      ask_location = False

    if player['hunger'] >= 5:
      player['health'] -= 10
      print(
          "\nYou are getting hungry, and your health is decreasing due to hunger."
      )
    if player['health'] <= 0:
      print(
          "Your health has reached zero. You didn't survive the zombie apocalypse. Game over!"
      )
      print(f"You survived for {player['days_survived']} days.")
      exit()
    elif player['hunger'] >= 10:
      print(
          "Your hunger has reached a critical level. You collapse from starvation. Game over!"
      )
      print(f"You survived for {player['days_survived']} days.")
      exit()
  else:
    horde_night()

print("!")
print("Your girlfriend has come and saved you.")
time.sleep(3)
print(
    "You earned a Bravery medal from The Great Leaders around the world...well done",
    player['name'])
print("🎖️")
