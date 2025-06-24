"""
This implements a simple Pokemon game where the user picks a monster and an attack
and the computer picks another monster and an attack and they repeated battle until
the health of one or the other is zero.
"""

import random # We need this module to generate random numbers for attack damage.
import time   # We'll use this to pause the game briefly, making it more readable.

import monsters

def print_intro_to_game():
    """ print a brief intro about what the game is and how to play """
    print("Welcome to the Simple Monster Battle!")
    print("------------------------------------\n")

 
def pick_monster(available_monsters):
    """ selects the number of the monster you choose and accesses it through the dictionary, while accepting errors """
    player_monster = None
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
    return player_monster

def choose_opponent_monster(available_monsters): 
    # --- Opponent's monster is randomly selected from the remaining ones ---
    # Ensures the opponent is not the same monster as the player's.
    opponent_monster = random.choice(available_monsters)
    # Display opponent's monster details including its attacks
    opponent_attack_names = ", ".join([att['name'] for att in opponent_monster['attacks']])
    print(f"Your opponent is: {opponent_monster['name']} (Health: {opponent_monster['health']}, Attacks: {opponent_attack_names})\n")
    return opponent_monster

def print_stats(player_monster, opponent_monster, turn): 
    '''prints out the stats & turn number'''
    print(f"--- Turn {turn} ---")
    print(f"Your {player_monster['name']} Health: {player_monster['health']}")
    print(f"Opponent {opponent_monster['name']} Health: {opponent_monster['health']}\n")


def choose_player_attack(player_monster):
    '''player inputs their attack & returns chosen player attack'''
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
    return chosen_player_attack

def game_start():
    """
    This function sets up and runs the main game loop.
    It now uses dictionaries to store monster data, allows user monster selection,
    and prompts for attack confirmation each turn.
    """

    print_intro_to_game()
    available_monsters = monsters.get_available_monsters()

    print("Choose your monster:")
    monsters.print_monsters(available_monsters)
    player_monster = pick_monster(available_monsters)

    opponent_monster = choose_opponent_monster(available_monsters)




    time.sleep(2) # Pause before the battle begins.
    print("--- Battle Start! ---\n")

    # --- Main Game Loop ---
    # The game continues as long as both monsters have health above zero.

 
    turn = 1



    
    while player_monster['health'] > 0 and opponent_monster['health'] > 0:
        print_stats(player_monster, opponent_monster, turn)
        # --- Player's turn to choose action / attack ---
        chosen_player_attack = choose_player_attack(player_monster)



        # 1. Your monster attacks the opponent using the chosen attack
        monsters.attack(player_monster, opponent_monster, chosen_player_attack)

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
        monsters.attack(opponent_monster, player_monster, chosen_opponent_attack)

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
