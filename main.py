from game import Game
from core.player import Player

start_the_game = Game()
user_decision = start_the_game.start()
while True:
    if user_decision == "battle":
        create_the_player = Player("moti")
        print_message = create_the_player.speak()
        create_the_monster = start_the_game.choose_random_monster()
        start_the_battle = start_the_game.battle(create_the_player, create_the_monster)
        break
    elif user_decision == "exit":
        break
    else:
        user_decision = start_the_game.start()