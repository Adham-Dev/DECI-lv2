import time
import sys

# Advanced delayed print function
def delayedPrint(string, int):
    print(string)
    time.sleep(int)

# Player choice
def choice():
    while True:
        try:
            playerChoice = int(input("Enter your choice (1 or 2):\n--> "))
            if playerChoice in [1, 2]:
                return playerChoice
            else:
                print("Your input is incorrect. Please enter 1 or 2.")
        except ValueError:
            print("Your input is incorrect. Please enter 1 or 2.")

# Check win or lose conditions
def check_win_lose(total_score, turn_count, max_turns, win_score, died=False):
    if died:
        total_score -= 50  # Deduct score when the player dies
        delayedPrint("You lost some points for dying.", 2)
    
    if total_score >= win_score:
        delayedPrint(f"Congratulations! You have won the game with a total score of {total_score}!", 2)
        return True
    elif total_score <= 0:
        delayedPrint("You have lost the game. Your score dropped to 0.", 2)
        return False
    elif turn_count >= max_turns and total_score < win_score:
        delayedPrint(f"You have lost the game. You didn't reach the required score of {win_score} within {max_turns} turns.", 2)
        return False
    return True

# Main game function
def play_game():
    delayedPrint("===== Welcome to \"TITAN'S HOLLOW QUEST\" Game =====", 0.7)
    delayedPrint("======== This game fully made by Adham ========", 1)
    print(" ")
    input("Press (Enter) to start game")
    delayedPrint("===================================", 1)

    animate()
    delayedPrint("===================================", 1)

    # Initialize score and turn count
    total_score = 0
    turn_count = 0
    max_turns = 7
    win_score = 200

    while True:
        delayedPrint("Welcome traveller, You're now in Eldoria Empire.", 2)
        delayedPrint("Please go to the town to get your quests.", 2)
        delayedPrint("You went to town", 2)
        turn_count += 1

        delayedPrint("Hey there, Are you new here?", 2)
        delayedPrint("Oh, don't care I have a HARD mission for you.", 2)
        delayedPrint("listen to him (1) ignore him (2)", 0.5)
        choice_1 = choice()
        if choice_1 == 2:
            delayedPrint("You ignored the greatest warrior in the empire and he killed you :)", 2)
            if not check_win_lose(total_score, turn_count, max_turns, win_score, died=True):
                break
        else:
            total_score += 10
            delayedPrint(f"Your total score is: {total_score}", 2)
            if not check_win_lose(total_score, turn_count, max_turns, win_score):
                break

        turn_count += 1

        delayedPrint("Okay, You have to go to Titan's Hollow and destroy it by killing the WARDEN.", 2)
        delayedPrint("Take this map, Weapons and items.", 2)
        turn_count += 1

        delayedPrint("You went to the CAVE to destroy it.", 2)
        delayedPrint("You are hearing a sound behind you.", 2)
        delayedPrint("Check what is behind you (1) ignore it (2)", 0.5)
        choice_2 = choice()
        if choice_2 == 2:
            delayedPrint("There was a long-range monster that killed you", 2)
            if not check_win_lose(total_score, turn_count, max_turns, win_score, died=True):
                break
        else:
            total_score += 30
            delayedPrint(f"Your total score is: {total_score}", 2)
            if not check_win_lose(total_score, turn_count, max_turns, win_score):
                break

        turn_count += 1

        delayedPrint("You found a long-range monster aiming at you!", 2)
        delayedPrint("You must avoid his arrow.", 2)
        delayedPrint("Hide behind a rock (1), Use your shield (2)", 0.5)
        choice_3 = choice()

        if choice_3 == 2:
            delayedPrint("Your shield is broken now, but you are still alive.", 2)
            delayedPrint("You killed the monster.", 2)
            have_shield = False
            total_score += 30  # Adjust points based on using shield
        else:
            delayedPrint("You found a huge rock next to you and hid behind it.", 2)
            delayedPrint("Now the monster doesn't see you.", 2)
            delayedPrint("You killed the monster.", 2)
            have_shield = True
            total_score += 50  # Higher points for successfully hiding

            delayedPrint(f"Your total score is: {total_score}", 2)
            if not check_win_lose(total_score, turn_count, max_turns, win_score):
                break

        turn_count += 1

        delayedPrint("While you are walking, you found something strange.", 2)
        delayedPrint("It looks like a sword.", 2)
        delayedPrint("You took it.", 2)
        total_score += 10
        delayedPrint(f"Your total score is: {total_score}", 2)
        if not check_win_lose(total_score, turn_count, max_turns, win_score):
            break

        turn_count += 1

        delayedPrint("You went to WARDEN's home.", 2)
        delayedPrint("The WARDEN felt that someone entered his home.", 2)
        delayedPrint("The WARDEN teleported behind you.", 2)
        delayedPrint("You attacked him, But your sword is now broken.", 2)
        delayedPrint("Run away (1), Use the strange weapon (2)", 0.5)
        choice_4 = choice()
        if choice_4 == 1:
            delayedPrint("The WARDEN teleported and killed you", 2)
            if not check_win_lose(total_score, turn_count, max_turns, win_score, died=True):
                break
        else:
            total_score += 100
            delayedPrint(f"Your total score is: {total_score}", 2)
            if not check_win_lose(total_score, turn_count, max_turns, win_score):
                break

        turn_count += 1

        delayedPrint("You attacked the WARDEN with the Harven's blade.", 2)
        delayedPrint("You killed the WARDEN successfully.", 2)
        delayedPrint("Congratulations! You have completed the quest.", 2)
        delayedPrint(f"Your final score is: {total_score}", 2)

        # End of game loop
        break

    # Ask if player wants to play again
    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            play_game()  # Restart the game
            break
        elif play_again == "no":
            delayedPrint("Thank you for playing!",0)
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Animation function
def animate():
    for i in range(3):
        for char in "|/-\\":
            sys.stdout.write(f'\rGame is loading {char}')
            time.sleep(0.1)
            sys.stdout.flush()
    sys.stdout.write('\rGame loaded successfully!\n')
    time.sleep(1)

# Start the game
play_game()
