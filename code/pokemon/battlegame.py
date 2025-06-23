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


def game_start():
    """
    This function sets up and runs the main game loop.
    It now uses dictionaries to store monster data, allows user monster selection,
    and prompts for attack confirmation each turn.
    """
    print("Welcome to the Simple Monster Battle!")
    print("------------------------------------\n")

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

    # --- Player chooses their monster ---
    player_monster = None # Initialize to None, will be set by user choice
    print("Choose your monster:")
    for i, monster in enumerate(available_monsters):
        # Display monster's attacks for selection
        attack_names = ", ".join([att['name'] for att in monster['attacks']])
        print(f"{i + 1}. {monster['name']} (Health: {monster['health']}, Attacks: {attack_names})")

    while player_monster is None:
        try:
            choice = int(input("Enter the number of your monster: "))
            if 1 <= choice <= len(available_monsters):
                # We use .pop(index - 1) to remove the chosen monster from
                # available_monsters and assign it to player_monster.
                # This ensures the opponent will be a different monster.
                player_monster = available_monsters.pop(choice - 1)
                print(f"You chose {player_monster['name']}!")
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        print("\n") # Add a newline for better readability

    # --- Opponent's monster is randomly selected from the remaining ones ---
    # Ensures the opponent is not the same monster as the player's.
    opponent_monster = random.choice(available_monsters)
    # Display opponent's monster details including its attacks
    opponent_attack_names = ", ".join([att['name'] for att in opponent_monster['attacks']])
    print(f"Your opponent is: {opponent_monster['name']} (Health: {opponent_monster['health']}, Attacks: {opponent_attack_names})\n")


    time.sleep(2) # Pause before the battle begins.
    print("--- Battle Start! ---\n")

    # --- Main Game Loop ---
    # The game continues as long as both monsters have health above zero.
    turn = 1
    while player_monster['health'] > 0 and opponent_monster['health'] > 0:
        print(f"--- Turn {turn} ---")
        print(f"Your {player_monster['name']} Health: {player_monster['health']}")
        print(f"Opponent {opponent_monster['name']} Health: {opponent_monster['health']}\n")

        # --- Player's turn to choose action / attack ---
        chosen_player_attack = None
        while chosen_player_attack is None:
            print(f"Choose an attack for {player_monster['name']}:")
            for i, attack_option in enumerate(player_monster['attacks']):
                print(f"{i + 1}. {attack_option['name']} (Damage: {attack_option['min_damage']}-{attack_option['max_damage']})")

            try:
                action_choice = input("Enter the number of your attack, or type 'quit' to exit: ").lower()
                if action_choice == 'quit':
                    print("Exiting game. Goodbye!")
                    return # Exit the game_start function entirely
                
                action_index = int(action_choice)
                if 1 <= action_index <= len(player_monster['attacks']):
                    chosen_player_attack = player_monster['attacks'][action_index - 1]
                else:
                    print("Invalid attack choice. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number or 'quit'.")
            print("\n") # Add a newline for better readability


        # 1. Your monster attacks the opponent using the chosen attack
        attack(player_monster, opponent_monster, chosen_player_attack)

        # Check if opponent is defeated after your attack
        if opponent_monster['health'] <= 0:
            print(f"\n{opponent_monster['name']} fainted!")
            print("--- YOU WIN! Congratulations! ---")
            break # Exit the loop because the opponent is defeated.

        # 2. Opponent monster attacks your monster (only if opponent is still alive)
        print("-" * 30) # Separator for clarity
        print(f"It's {opponent_monster['name']}'s turn!")
        time.sleep(1) # Small pause before opponent attacks

        # Opponent randomly chooses one of its attacks
        chosen_opponent_attack = random.choice(opponent_monster['attacks'])
        attack(opponent_monster, player_monster, chosen_opponent_attack)

        # Check if your monster is defeated after opponent's attack
        if player_monster['health'] <= 0:
            print(f"\n{player_monster['name']} fainted!")
            print("--- YOU LOSE! Better luck next time! ---")
            break # Exit the loop because your monster is defeated.

        print("\n" + "=" * 40 + "\n") # Big separator for next turn
        time.sleep(1.5) # Pause before the next turn.
        turn += 1

# --- Run the game ---
# This line calls the game_start function to begin the game when the script is run.
if __name__ == "__main__":
    game_start()
