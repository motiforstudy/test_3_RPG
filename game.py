from random import randint
from core.orc import Orc
from core.goblin import Goblin


class Game:

    def start(self):
        user_decision_1 = self.show_menu()
        return user_decision_1

    def show_menu(self):
        user_choice = input("please choose, do you want to battle? \n"
                            "or do you want to exit? ")
        return user_choice

    def choose_random_monster(self):
        random_number = randint(1,2)
        if random_number == 1:
            create_orc = Orc("bob")
            create_orc.speak()
            return create_orc
        else:
            create_goblin = Goblin("bob")
            create_goblin.speak()
            return create_goblin

    def battle(self, player, monster):

        player_roll_dice_of_6 = Game.roll_dice(6)
        monster_roll_dice_of_6 = Game.roll_dice(6)
        add_to_dice_of_player_the_speed = player_roll_dice_of_6 + player.speed
        add_to_dice_of_monster_the_speed = monster_roll_dice_of_6 + monster.speed

        if add_to_dice_of_player_the_speed >= add_to_dice_of_monster_the_speed:
            while player.hp > 0 and monster.hp > 0:
                print("the player attack")
                the_player_roll_dice_of_20 = Game.roll_dice(20)
                add_the_dice_of_20_the_player_speed = the_player_roll_dice_of_20 + player.speed
                if add_the_dice_of_20_the_player_speed > monster.armor_rating:
                    print("the attack power is more than the monster armor")
                    player_roll_dice_of_6_2 = Game.roll_dice(6)
                    get_the_player_power = player_roll_dice_of_6_2 * player.power
                    monster.hp -= get_the_player_power
                    print(f"now the monster hp = {monster.hp}")
                    if 0 >= monster.hp:
                        print("the plyer win")
                        break
                the_monster_roll_dice_of_20 = Game.roll_dice(20)
                add_the_dice_of_20_the_monster_speed = the_monster_roll_dice_of_20 + monster.speed
                print("the monster attack")
                if add_the_dice_of_20_the_monster_speed > player.armor_rating:
                    print("the attack power is more than the player armor")
                    monster_roll_dice_of_6_2 = Game.roll_dice(6)
                    get_the_monster_power = monster_roll_dice_of_6_2 * monster.power
                    player.hp -= get_the_monster_power
                    print(f"now the player hp = {player.hp}")
                    if 0 >= player.hp:
                        print("the monster win")
                        break
        else:
            while player.hp > 0 and monster.hp > 0:
                print("the monster attack")
                the_monster_roll_dice_of_20 = Game.roll_dice(20)
                add_the_dice_of_20_the_monster_speed = the_monster_roll_dice_of_20 + monster.speed
                if add_the_dice_of_20_the_monster_speed > player.armor_rating:
                    print("the attack power is more than the player armor")
                    monster_roll_dice_of_6_2 = Game.roll_dice(6)
                    get_the_monster_power = monster_roll_dice_of_6_2 * monster.power
                    player.hp -= get_the_monster_power
                    print(f"now the player hp = {player.hp}")
                    if 0 >= player.hp:
                        print("the monster win")
                        break
                the_player_roll_dice_of_20 = Game.roll_dice(20)
                add_the_dice_of_20_the_player_speed = the_player_roll_dice_of_20 + player.speed
                print("the player attack")
                if add_the_dice_of_20_the_player_speed > monster.armor_rating:
                    print("the attack power is more than the monster armor")
                    player_roll_dice_of_6_2 = Game.roll_dice(6)
                    get_the_player_power = player_roll_dice_of_6_2 * player.power
                    monster.hp -= get_the_player_power
                    print(f"now the monster hp = {monster.hp}")
                    if 0 >= monster.hp:
                        print("the plyer win")
                        break


    @staticmethod
    def roll_dice(sides):
        get_dice_value = randint(1, sides)
        return get_dice_value