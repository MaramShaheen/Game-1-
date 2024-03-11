# File: game 1
# Purpose: player keep adding numbers from 1 to 10 to sum the first player to reach 100 wins
# Author: Maram Abdulnabi Yousif Mohamed Shaheen
# ID: 20230827

 
def get_valid_input(player): #Function to validate input from the players (numbers from 1-10)
    while True:
        try:
            player_input = int(input(f"{player}: enter a number from 1-10\n=====> "))
            if not (1 <= player_input <= 10):
                print("Invalid input, please enter a number from 1-10")
                continue
            return player_input
        except ValueError:
            print("Invalid input, Enter a valid number.")
 

def main_play_100game():
# Main function to play the 100 game.


    # welcome message and Rules
    
    print("=========================================================================")
    print('------------------------welcome to the 100 game--------------------------')
    print("=========================================================================")
    print("Rules:")
    print("1. Players take turns adding numbers from 1 to 10 to the sum.")
    print("2. The first player to reach exactly 100 wins.")
    print("3. If a player's move causes the sum to exceed 100, that move is invalid.")
    print("4. Enjoy the game!")
    print("=========================================================================")    
    
    #  Initialize sum
    Nsum = 0
    
    # player 1's turn
    
    try:  #try/Except to prevent user from entering anything other than numbers

        while True:
            while True:
                
                print(f"Total = {Nsum}")
                player1_input = get_valid_input("Player 1")
                
                # update sum and display
                Nsum += player1_input
                print(f"Total = {Nsum}")
                
                if Nsum == 100 : # Check winner
                    print('Player 1 is the winner')
                    break
                
                while Nsum > 100:  #if sum exceeded 100 make player try again
                    print("You can't exceed 100, Player 1, Please try again")
                    Nsum -= player1_input
                    print(f"Total = {Nsum}")
                    player1_input = int(input("=====>"))
                    Nsum += player1_input
                    print(f"Total = {Nsum}")

                
                #player 2's turn
                player2_input = get_valid_input("Player 2")
                
                # update sum and display
                Nsum += player2_input
                print(f"Total = {Nsum}")
                
                if Nsum == 100 : # Check winner
                    print('player 2 is the winner')
                    break  
                
                while Nsum > 100: #if sum exceeded 100 make player try again
                    print("You can't exceed 100, Player 2, Please try again")
                    Nsum -= player2_input
                    print(f"Total = {Nsum}")
                    player2_input = int(input("=====>")) 
                    Nsum += player2_input        

                             
            print("Game over!")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':  # Exit Game if player diidn't choose yes 
                print("Thanks for using our Game")
                break
            else:
                Nsum = 0  # if player wants to play again reset sum back to zero
            print("\n==========================================================\n")
    
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
    
    except ValueError:
         print("Invalid input. Restart the game and enter only numbers.")  
                   

main_play_100game()

