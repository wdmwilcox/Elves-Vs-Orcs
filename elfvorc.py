import random
import time

class Player(object):
    
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.power = 10
        self.mana = 100
        self.magic = 10
        self.armor = 5
        self.gold = 10

class Enemy(object):

    def __init__(self, health, power, armor, gold):
        self.health = health
        self.power = power
        self.armor = armor
        self.gold = gold

def wait():
    time.sleep(0.5)
    return None

print("Welcome to Elves vs Orcs RPG Battle Game!")

player_name = input("Enter your name to begin: ")
player = Player(player_name)

print(f"""{player.name}, You have:
    {player.health} health,
    {player.level} level,
    {player.mana} mana, 
    {player.power} power,
    {player.magic} magic,
    {player.armor} armor,
    {player.gold} gold
    """)

continue_playing = True
while continue_playing:

    print(f"What would you like to do?")

    rest_choice_map = {
        1: "Go Adventuring",
        2: "Rest",
        3: "See Stats",
        4: "Shop",
        5: "End Game"
    }

    for k, v in rest_choice_map.items():
        print(f"{k}: {v}")

    choice = None
    while choice is None:
        try:
            choice = int(input("> "))
            if choice in rest_choice_map.keys():
                player_choice = choice
            else:
                choice = None
                print("Select a choice")
        except ValueError:
            print("Enter a number")

    print(f"You chose {rest_choice_map[player_choice]}")

    wait()

    if player_choice == 5:
        continue_playing = False
        print(f"You collected {player.gold} gold.")
        print("Thank you for playing.")

    if player_choice == 4:
        print("Welcome to the shop")
        
        item_map = {
            1: ["+1 Health, 10g", 10],
            2: ["+1 Mana: 10g", 10],
            3: ["+1 Magic: 10g", 10],
            4: ["+1 Power: 10g", 10],
            5: ["+1 Armor: 10g", 10],
        }

        for k, v in item_map.items():
            print(f"{k}: {v[0]}")

        choice = None
        while choice is None:
            try:
                choice = int(input("> "))
                if choice in item_map.keys():
                    shop_choice = choice
                else:
                    choice = None
                    print("Select a choice")
            except ValueError:
                print("Enter a number")

        if player.gold >= item_map[shop_choice][1]:

            wait()

            if shop_choice == 1:
                print(f"You bought {item_map[shop_choice][0]}")
                player.gold -= item_map[shop_choice][1]
                player.health += 1

            if shop_choice == 2:
                print(f"You bought {item_map[shop_choice][0]}")
                player.gold -= item_map[shop_choice][1]
                player.mana += 1

            if shop_choice == 3:
                print(f"You bought {item_map[shop_choice][0]}")
                player.gold -= item_map[shop_choice][1]
                player.magic += 1
            
            if shop_choice == 4:
                print(f"You bought {item_map[shop_choice][0]}")
                player.gold -= item_map[shop_choice][1]
                player.power += 1

            if shop_choice == 5:
                print(f"You bought {item_map[shop_choice][0]}")
                player.gold -= item_map[shop_choice][1]
                player.armor += 1

        else:
            print("You don't have enough gold for that!")
            wait()

    if player_choice == 3:
       print(f"""{player.name}, You have:
        {player.health} health,
        {player.level} level,
        {player.mana} mana, 
        {player.power} power,
        {player.magic} magic,
        {player.armor} armor,
        {player.gold} gold
        """)

    if player_choice == 2:
        print("You go to sleep.")
        time.sleep(5)
        print("You wake up feeling refreshed!")
        if player.health >= 80:
            player.health = 100
        else:
            player.health += 20
        if player.mana >= 80:
            player.mana = 100
        else:
            player.health += 20
        print(f"{player.health} health and {player.mana} mana.")

    if player_choice == 1:
        print("You go adventuring and encounter an orc!")

        health = 50 + random.randint(-50, 50)
        power = 10 + random.randint(-5, 5)
        armor = 5 + random.randint(-2, 2)
        gold = 10 + random.randint(-10, 10)

        orc = Enemy(health, power, armor, gold)

        print(f"""
        Orc has:
        {orc.health} health,
        {orc.power} power,
        {orc.armor} armor,
        {orc.gold} gold,
        """)

        flee = False
        while orc.health > 0 and player.health > 0 and flee == False:

            wait()

            print(f"You have {player.health} health and {player.mana} mana")
            print(f"Orc has {orc.health} health")

            print("What do you do?")

            battle_choice_map = {
                1: "Attack",
                2: "Cast Spell",
                3: "Flee",
            }

            for k, v in battle_choice_map.items():
                print(f"{k}: {v}")

            wait()

            choice = None
            while choice is None:
                try:
                    choice = int(input("> "))
                    if choice in battle_choice_map.keys():
                        battle_choice = choice
                    else:
                        choice = None
                        print("Select a choice")
                except ValueError:
                    print("Enter a number")

            print(f"You chose {battle_choice_map[battle_choice]}")

            if battle_choice == 1:
                critical = False
                if random.randint(1,20) > 15:
                    critical = True
                modifier = round(player.power * .25)
                damage = random.randint(-1 * modifier, modifier) + player.power - orc.armor
                if damage <= 0:
                    damage = 1
                if critical == True:
                    damage *= 2
                if random.randint(1,20) > 5:
                    if critical == True:
                        print("CRITICAL HIT!")
                    print(f"You hit orc for {damage}.")
                    orc.health -= damage
                else:
                    print("You missed!")

            if battle_choice == 2:
                critical = False
                if random.randint(1,20) > 15:
                    critical = True
                if random.randint(1,20) > 5:
                    modifier = round(player.magic * 0.5)
                    damage = random.randint(-1 * modifier, modifier) + player.magic
                    if critical == True:
                        damage *= 1.5
                    if player.mana > 0 + player.magic:
                        print(f"Your spell damaged orc for {damage} damage!")
                        orc.health -= damage
                        player.mana -= player.magic
                    else:
                        print(f"You only have {player.mana} mana.  You need {player.magic} mana to do that.")
                else:
                    print("Orc resisted your spell")

            if battle_choice == 3:
                flee = True
        
            wait()

            if random.randint(1,20) > 5:
                modifier = round(orc.power * .25)
                damage = random.randint(-1 * modifier, modifier) + orc.power - player.armor
                if damage <= 0:
                    damage = 1
                print(f"Orc hits you for {damage} damage")
                player.health -= damage
            else:
                print("Orc missed you.")

        wait()

        if player.health <= 0:
            print("You have been knocked unconscious.")
            if player.gold >= orc.gold:
                print("Orc pilfers {orc.gold} gold from your body!")
                player.gold -= orc.gold
            else:
                print("Orc pilfers {player.gold} gold from your body!")
                player.gold = 0
            
        elif orc.health <= 0:
            print("You have defeated orc!")
            print(f"You collect {orc.gold} gold!")
            player.gold += orc.gold

        elif flee == True:
            print("You have fled!")
            dropped_gold = round(orc.gold / 2)
            if player.gold < dropped_gold:
                dropped_gold = player.gold
            print("You dropped {dropped_gold}")
            player.gold -= dropped_gold






