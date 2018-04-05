from Game import Game

game = Game()
game.start()

while True:

    player_name = str(game.whose_turn())  # return playerX or playerO
    player_choice = 0

    while player_choice < 1 or player_choice > 9:
        game.refresh()
        player_choice = input("\n(%s) Please choose 1 - 9 > " % player_name)
        if player_choice.isnumeric():
            player_choice = int(player_choice)
        else:
            player_choice = -1

    player_choice -= 1
    game.update(player_choice, player_name)
    game.refresh()
    # Check for win
    if game.is_winner(player_name):
        print("\n%s won!\n" % player_name)  # decides whose turns
        play_again = str(input("Would you like to play again? (Y/N) > ").upper())

        if play_again == "Y":
            game.reset()
            continue
        else:
            break
    # Check if it is not win and if the piles are full, end the game
    elif game.is_tie():
        print("\nTie Game!\n")
        play_again = str(input("Would you like to play again? (Y/N) > ").upper())

        if play_again == "Y":
            game.reset()
            continue
        else:
            break
