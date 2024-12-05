import random

def get_player_move():
    while True:
        move = input("Enter your move (reload/shoot/shield): ").lower()
        if move in ['reload', 'shoot', 'shield']:
            return move
        print("Invalid move! Try again.")

def display_status(player_ammo, computer_ammo):
    print(f"\nYour ammo: {player_ammo}")
    print(f"Computer's ammo: {computer_ammo}")

def get_computer_move(computer_ammo):
    if computer_ammo == 0:
        return 'reload'
    moves = ['reload', 'shoot', 'shield']
    weights = [1, 2, 1] if computer_ammo > 0 else [3, 0, 1]
    return random.choices(moves, weights=weights)[0]

def main():
    print("Welcome to 007 Spy Game!")
    print("Rules: You need ammo to shoot. Reload to get ammo.")
    print("Shield blocks shots. First to hit their opponent wins!")
    
    player_ammo = 0
    computer_ammo = 0
    
    while True:
        display_status(player_ammo, computer_ammo)
        player_move = get_player_move()
        computer_move = get_computer_move(computer_ammo)
        
        print(f"\nComputer chose: {computer_move}")
        
        # Handle player reload
        if player_move == 'reload':
            player_ammo += 1
            if computer_move == 'shoot' and computer_ammo > 0:
                print("You got shot while reloading! Game Over.")
                return False
                
        # Handle computer reload
        if computer_move == 'reload':
            computer_ammo += 1
            if player_move == 'shoot' and player_ammo > 0:
                print("You shot the computer while it was reloading! You win!")
                return True
                
        # Handle shooting
        if player_move == 'shoot':
            if player_ammo > 0:
                player_ammo -= 1
                if computer_move != 'shield':
                    print("You shot the computer! You win!")
                    return True
                print("Computer blocked your shot!")
            else:
                print("Click! You're out of ammo!")
                
        if computer_move == 'shoot':
            if computer_ammo > 0:
                computer_ammo -= 1
                if player_move != 'shield':
                    print("You got shot! Game Over.")
                    return False
                print("You blocked computer's shot!")
            
if __name__ == "__main__":
    while True:
        result = main()
        if not input("\nPlay again? (y/n): ").lower().startswith('y'):
            break
