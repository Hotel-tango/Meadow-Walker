import random as r
import warnings as w

def error(fatal=False, warning=False, message="N/A", Location="N/A"):
    # Code 0: Debugging
    # Code 1: Value has gone into a range not accepted, coding error

    if fatal is True:
        raise RuntimeError(message)
    elif warning is True:
        w.warn(message)
    else:
        raise RuntimeError("Error called has no severity")

class Player:

    def __init__(self, name):
        self.name = name
        self.level = 0
        self.xp = 0
        self.strength = 0
        self.vigour = 75
        self.weapon_pro = 0
        self.armour = "Rags"
        self.hp = 0
        self.get_hp()

    def __str__(self):
        return(f"""
            {self.name}'s statistics:
            Level: {self.level}
            Strength: {self.strength}
            Max HP: {self.max_hp}
            Current HP: {self.hp}
            Weapon proficiency: {self.weapon_pro}
            """)

    def get_hp(self):
        self.max_hp = self.vigour
        self.hp = self.max_hp - self.hp

    def take_damage(self, attacker, damage_amount):
        attacker = attacker.capitalize()
        print(f"{attacker} attacked you, dealing {armour_calculation(damage_amount, self.armour)} damage.")
        self.hp -= armour_calculation(damage_amount, self.armour)
        print(f"Your hp is now {self.hp}")
        print("")

    def add_xp(self, xp_amount):
        if xp_amount > 0:
            self.xp += xp_amount
            print(f"You gained {xp_amount}")
        else:
            error(warning=True, message="Code 1, add_xp got negative xp_amount")

    def get_xp(self):
        if self.xp > 5000:
            self.level_up
            self.xp -= 5000

    def level_up(self, amount):
        if amount < 1:
            error(fatal=True, message="Code 1, Level up amount is negative or zero")
        else:
            self.level += amount
        print("You've leveled up!")
        print(f"Your level is now {self.level}!")
        print("")

class Enemy:

    def __init__(self, name, hp, damage, armour_type):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armour_type = armour_type

class Town:

    def __init__(self):
        pass

# Just some armour stuff

armour_dictionary = {"Rags": 0, "Gambeson": 10, "Chainmail": 30, "Lamellar": 50, "Plate": 65}
def armour_calculation(attack_damage, armour):
    final_damage = max(0, round(attack_damage * (1 - armour_dictionary.get(armour) / 100)))
    return(final_damage)


# Debug

player = Player("John Doe")

def debug():
    debug_dict = {1: "print", 2: "take damage", 3: "give armour", 4: "gain xp"}
    if input("Enter debug mode? Y/N> ").lower() == "y":
        debug_mode = True
        print("Entering debug mode")

        while debug_mode == True:
            print("Debug options ('exit' or 'n' to exit debug mode): ")
            for k, v in debug_dict.items():
                print(f"{k}: {v}")
            print("")
            debug_choice = input("> ").lower()
            if debug_choice.isalpha():
                debug_choice = next(k for k, v in debug_dict.items() if v == debug_choice)
            elif debug_choice.isdigit():
                debug_choice = int(debug_choice)
            match debug_choice:
                case 1:
                    print(player)
                case 2:
                    player.take_damage("jane doe", int(input("Damage amount?(Must be number) > ")))
                case 3:
                    player.armour = "Null"
                    print("Choose armour: ")
                    print("\n".join(f"{k}: {v}" for k, v in armour_dictionary.items()))
                    while player.armour not in armour_dictionary.keys():
                        player.armour = input("> ").capitalize()
                case 4:
                    player.add_xp(int(input("How much xp would you like to add?(Must be number, 5000 is to level up) > ")))
                case _:
                    pass
            
    else:
        print("Exiting debug mode")

debug()