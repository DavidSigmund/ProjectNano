from game_play import setup_game, play_game

# Run the game
if __name__ == "__main__":
    name = input("What is your name?: ")
    player = setup_game(name)
    play_game(player)
