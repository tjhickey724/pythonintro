"""
this module implements pokemon monsters.
It defines 4 monsters, has a function to print them out, and
a function to have monster fight another with a give attack.
"""

import random # We need this module to generate random numbers for attack damage.
import time   # We'll use this to pause the game briefly, making it more readable.


def attack(attacker, target, attack_details):
    """
    This function defines how one monster attacks another using a specific attack.
    It takes the attacker dictionary, target dictionary, and the details of the
    specific attack being used (from its 'attacks' list).
    It calculates random damage and reduces the target's health.
    """
    # Generate a random damage value within the chosen attack's range.
    # We now use 'min_damage' and 'max_damage' from the attack_details dictionary.
    damage = random.randint(attack_details['min_damage'], attack_details['max_damage'])

    # Print who is attacking whom with which attack and how much damage they deal.
    print(f"\n{attacker['name']} uses {attack_details['name']} on {target['name']}!")
    print(f"{attacker['name']} deals {damage} damage.")

    # Reduce the target monster's health by the damage dealt.
    target['health'] -= damage

    # Make sure health doesn't go below zero.
    if target['health'] < 0:
        target['health'] = 0

    # Print the target monster's new health.
    print(f"{target['name']} now has {target['health']} health left.")
    time.sleep(1) # Pause for 1 second to make the output easier to follow.


   
def get_available_monsters():
    # --- Define a list of available monsters with multiple attacks ---
    # Each monster now has an 'attacks' key, which is a list of dictionaries.
    # Each inner dictionary represents a specific attack with its name and damage range.
    available_monsters = [
        {
            'name': "Charmander",
            'health': 100,
            'attacks': [
                {'name': 'Scratch', 'min_damage': 15, 'max_damage': 25},
                {'name': 'Ember', 'min_damage': 10, 'max_damage': 30}
            ]
        },
        {
            'name': "Squirtle",
            'health': 90,
            'attacks': [
                {'name': 'Tackle', 'min_damage': 10, 'max_damage': 20},
                {'name': 'Water Gun', 'min_damage': 15, 'max_damage': 25}
            ]
        },
        {
            'name': "Bulbasaur",
            'health': 110,
            'attacks': [
                {'name': 'Vine Whip', 'min_damage': 12, 'max_damage': 22},
                {'name': 'Razor Leaf', 'min_damage': 8, 'max_damage': 35} # Example of wider range
            ]
        },
        {
            'name': "Pikachu",
            'health': 85,
            'attacks': [
                {'name': 'Quick Attack', 'min_damage': 18, 'max_damage': 28},
                {'name': 'Thunder Shock', 'min_damage': 13, 'max_damage': 32}
            ]
        }
    ]
    return available_monsters

def print_monsters(available_monsters):
    """ prints the monsters with an index and the list of their attack names """
    for i, monster in enumerate(available_monsters):
        # Display monster's attacks for selection
        attack_names = ", ".join([att['name'] for att in monster['attacks']])
        print(f"{i + 1}. {monster['name']} (Health: {monster['health']}, Attacks: {attack_names})")
