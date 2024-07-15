import random

def guessing_game():
    # Dictionary of video game titles and their clues
    games_clues = {
        "The Legend of Zelda": "This game features a hero named Link who saves Princess Zelda.",
        "Super Mario Odyssey": "In this game, Mario travels between different kingdoms to rescue Princess Peach.",
        "Red Dead Redemption 2": "This game is set in the American Wild West and follows outlaw Arthur Morgan.",
        "The Witcher 3: Wild Hunt": "You play as Geralt of Rivia, a monster hunter in a dark fantasy world.",
        "Dark Souls": "This game is known for its challenging gameplay and intricate world design.",
        "Overwatch": "A team-based multiplayer first-person shooter where players select from a diverse cast of heroes.",
        "Minecraft": "A sandbox game where players can build structures and explore a blocky, procedurally-generated world.",
        "Grand Theft Auto V": "Set in the fictional state of San Andreas, players follow the lives of three criminals.",
        "Fortnite": "A popular battle royale game where players fight to be the last one standing.",
        "League of Legends": "A multiplayer online battle arena game where players control a champion with unique abilities."
    }
    
    # Shuffle the list of game titles
    games = list(games_clues.keys())
    random.shuffle(games)
    
    # Welcome message
    print("Welcome to the Video Game Guessing Game!")
    print("I will provide you with a clue about a video game. Can you guess which game it describes?")
    
    # Game loop
    for game in games:
        # Get the clue for the current game
        clue = games_clues[game]
        
        # Generate multiple choice options
        choices = list(games_clues.keys())
        choices.remove(game)  # Remove the correct game from choices
        choices = random.sample(choices, 3)  # Randomly select 3 other games as choices
        choices.append(game)  # Add the correct game to choices list
        random.shuffle(choices)  # Shuffle the choices to randomize their order
        
        # Display the clue
        print(f"\nClue: {clue}")
        
        # Display the multiple choice options
        print("\nHere are your choices:")
        for index, choice in enumerate(choices, start=1):
            print(f"{index}. {choice}")
        
        # Ask the player to guess which game matches the clue
        while True:
            try:
                guess_index = int(input("\nEnter the number of your guess: "))
                
                if guess_index < 1 or guess_index > len(choices):
                    raise ValueError("Invalid input. Please enter a number within the given range.")
                
                guessed_game = choices[guess_index - 1]
                
                if guessed_game == game:
                    print(f"\nCorrect! '{game}' is the game that matches the clue.")
                    break
                else:
                    print("\nOops! That's not the correct game. Try again!")
            
            except ValueError as ve:
                print(ve)
    
    print("\nThank you for playing!")

# Run the game
guessing_game()
