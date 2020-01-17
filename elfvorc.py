import random
import time

class Player(object):
    
    def __init__(self, name):
        self.name = name
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

def create_player():
    player_name = input("Enter your name to begin: ")
    player = Player(player_name)
    return player

def display_stats(player):
    print(f"""{player.name}, You have:
        {player.health} health,
        {player.mana} mana, 
        {player.power} power,
        {player.magic} magic,
        {player.armor} armor,
        {player.gold} gold
        """)

def wait():
    time.sleep(0.5)

def get_choice(map):
    """
    Returns a player's choice based on a map
    """
    for k, v in map.items():
        print(f"{k}: {v}")

    choice = None
    while choice is None:
        try:
            choice = int(input("> "))
            if choice in map.keys():
                player_choice = choice
            else:
                choice = None
                print("Select a choice")
        except ValueError:
            print("Enter a number")
    return player_choice

def set_critical(threshold):
    critical = False
    if roll_20() > threshold:
        critical = True
    return critical

def buy_upgrade(player, upgrade):
    print(f"You bought {upgrade}")
    player.gold -= 10
    if shop_choice == 1:
        player.health += 1
    elif shop_choice == 2:
        player.mana += 1
    elif shop_choice == 3:
        player.magic += 1
    elif shop_choice == 4:
        player.power += 1
    elif shop_choice == 5:
        player.armor += 1

def get_outcome(player, enemy):
    if player.health <= 0:
        print("You have been knocked unconscious.")
        if player.gold >= enemy.gold:
            print("Orc pilfers {enemy.gold} gold from your body!")
            player.gold -= enemy.gold
        else:
            print(f"Orc pilfers {player.gold} gold from your body!")
            player.gold = 0     
    elif enemy.health <= 0:
        print("You have defeated orc!")
        print(f"You collect {enemy.gold} gold!")
        player.gold += enemy.gold
    elif flee == True:
        print("You have fled!")
        dropped_gold = round(enemy.gold / 2)
        if player.gold < dropped_gold:
            dropped_gold = player.gold
        print(f"You dropped {dropped_gold} gold")
        player.gold -= dropped_gold

def get_orc():
    health = 50 + random.randint(-50, 50)
    power = 10 + random.randint(-5, 5)
    armor = 5 + random.randint(-2, 2)
    gold = 10 + random.randint(-10, 10)
    orc = Enemy(health, power, armor, gold)
    return orc

def show_enemy_stats(enemy):
    print(f"""
        Orc has:
        {enemy.health} health,
        {enemy.power} power,
        {enemy.armor} armor,
        {enemy.gold} gold,
        """)

def get_physical_damage(player, enemy):
    critical = set_critical(15)
    modifier = round(player.power * .25)
    damage = random.randint(-1 * modifier, modifier) + player.power - enemy.armor
    if damage <= 0:
        damage = 1
    if critical == True:
        damage *= 2
    return critical, damage

def get_magical_damage(player, enemy):
    critical = set_critical(15)
    modifier = round(player.magic * .25)
    damage = random.randint(-1 * modifier, modifier) + player.magic
    if damage <= 0:
        damage += 1
    if critical == True:
        damage *= round(1.5)
    return critical, damage

def roll_20():
    return random.randint(1,20)

def rest(player):
    if player.health >= 80:
        player.health = 100
    else:
        player.health += 20
    if player.mana >= 80:
        player.mana = 100
    else:
        player.mana += 20
    return player

rest_choice_map = {
    1: "Go Adventuring",
    2: "Rest",
    3: "See Stats",
    4: "Shop",
    5: "End Game"
}

item_map = {
    1: "+1 Health, 10g",
    2: "+1 Mana: 10g",
    3: "+1 Magic: 10g",
    4: "+1 Power: 10g",
    5: "+1 Armor: 10g",
    6: "Leave Shop",
}

battle_choice_map = {
    1: "Attack",
    2: "Cast Spell",
    3: "Flee",
}

print("Welcome to Elves vs Orcs RPG Battle Game!")

player = create_player()
display_stats(player)

continue_playing = True
while continue_playing:

    print(f"What would you like to do?")

    player_choice = get_choice(rest_choice_map)

    print(f"You chose {rest_choice_map[player_choice]}")

    wait()

    if player_choice == 5:
        continue_playing = False
        print(f"You collected {player.gold} gold.")
        print("Thank you for playing.")

    elif player_choice == 4:
        print("Welcome to the shop")
        shop_choice = get_choice(item_map)
        if shop_choice != 6:
            upgrade = item_map[shop_choice]
            if player.gold >= 10:
                wait()
                buy_upgrade(player, upgrade)
            else:
                print("You don't have enough gold for that!")
                wait()

    elif player_choice == 3:
       display_stats(player)

    elif player_choice == 2:
        print("You go to sleep.")
        time.sleep(5)
        print("You wake up feeling refreshed!")
        player = rest(player)
        print(f"{player.health} health and {player.mana} mana.")

    elif player_choice == 1:
        print("You go adventuring and encounter an orc!")
        orc = get_orc()
        show_enemy_stats(orc)

        flee = False
        while orc.health > 0 and player.health > 0 and flee == False:

            wait()

            print(f"You have {player.health} health and {player.mana} mana")
            print(f"Orc has {orc.health} health")
            print("What do you do?")

            battle_choice = get_choice(battle_choice_map)

            print(f"You chose {battle_choice_map[battle_choice]}")

            if battle_choice == 1:
                critical, damage = get_physical_damage(player, orc)
                if roll_20() > 5:
                    if critical == True:
                        print("CRITICAL HIT!")
                    print(f"You hit orc for {damage}.")
                    orc.health -= damage
                else:
                    print("You missed!")

            if battle_choice == 2:
                critical, damage = get_magical_damage(player, orc)
                if player.mana >= player.magic:
                    if roll_20() > 5:
                        print(f"Your spell damaged orc for {damage} damage!")
                        orc.health -= damage
                        player.mana -= player.magic
                    else:
                        print("Orc resisted your spell")
                else:
                    print(f"You only have {player.mana} mana.  You need {player.magic} mana to do that.")
                
            if battle_choice == 3:
                flee = True
        
            wait()
            if orc.health > 0 or flee == False:
                if roll_20() > 5:
                    critical, damage = get_physical_damage(orc, player)
                    if critical == True:
                        print("CRITICAL HIT!")
                    print(f"Orc hits you for {damage} damage")
                    player.health -= damage
                else:
                    print("Orc missed you.")


        wait()

        get_outcome(player, orc)






