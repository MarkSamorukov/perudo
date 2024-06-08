from itertools import cycle
from typing import Type

from game.move import Move
from game.player import Player

from models.random_model import RandomModel
from models.math_expectation_model import MathExpectationModel
from models.human_model import HumanModel


class Game:
    def __init__(self, players_counter: int, players_name: [str],
                 models: list[Type[RandomModel | MathExpectationModel | HumanModel]],
                 dice_counter: [int] = None,
                 print_mode: int = 1) -> None:
        if not dice_counter:
            dice_counter = [5] * players_counter
        self.players_counter = players_counter
        self.all_dice_counter = sum(dice_counter)
        self.players = [Player(players_name[i], i, dice_counter[i], models[i]) for i in range(self.players_counter)]
        self.print_mode = print_mode
        self.game_stat = {'rounds': [], 'winner': None}

    def __str__(self) -> str:
        fres: str = f""
        for i in range(self.players_counter):
            fres += f"Игрок {self.players[i].name}:\n{self.players[i]}"

        return fres

    def start_game(self):
        while sum(map(int, map(bool, self.players))) >= 2:
            player_index, round_stat = self.start_round()

            self.game_stat['rounds'].append(round_stat)

            self.players = self.players[player_index:] + self.players[:player_index]
            self.all_dice_counter -= 1

            for player in self.players:
                if not player:
                    del self.players[self.players.index(player)]
                    self.players_counter -= 1

            for player in self.players:
                player.reroll_dice()

        for player in self.players:
            if player:
                if self.print_mode == 1:
                    print(f"Игрок {player.name} победил!")
                self.game_stat['winner'] = player.name

                return self.game_stat, player

    def start_round(self):
        round_stat = {
            'players_counter': self.players_counter,
            'player_names': [],
            'player_dice': {},
            'moves': [],
            'loser': None
        }
        for player in self.players:
            round_stat['player_names'].append(player.name)
            round_stat['player_dice'][player.name] = player.dice

        pre_move: Move = Move({
            'believe': True,
            'value': 0,
            'quantity': 0,
            'first_move': True
        })

        for i in cycle(range(self.players_counter)):
            move: Move = self.players[i].do_move(pre_move, self.all_dice_counter, self.players[i].dice,
                                                 round_stat['moves'])

            round_stat['moves'].append((self.players[i].name, move.move))
            if self.print_mode == 1:
                print(f'Игрок {self.players[i].name} говорит:')
                print(move)
            if not move:
                if self.print_mode == 1:
                    print('Вскрываемся:')
                check_player_index = (i - 1 + self.players_counter) % self.players_counter
                check_move: Move = pre_move
                if self.is_lie(check_move):
                    self.players[check_player_index].discard_dice()
                    if self.print_mode == 1:
                        print(f"Игрок {self.players[check_player_index].name} выбрасывает кубик")
                        print("=" * 100)
                    round_stat['loser'] = self.players[check_player_index].name
                    return check_player_index, round_stat
                else:
                    self.players[(check_player_index + 1) % self.players_counter].discard_dice()
                    if self.print_mode == 1:
                        print(
                            f"Игрок {self.players[(check_player_index + 1) % self.players_counter].name} выбрасывает кубик")
                        print("=" * 100)
                    round_stat['loser'] = self.players[(check_player_index + 1) % self.players_counter].name
                    return (check_player_index + 1) % self.players_counter, round_stat

            pre_move = move

    def is_lie(self, check_move: Move) -> bool:
        value = check_move.move['value']
        quantity = check_move.move['quantity']
        real_quantity = sum(map(lambda x: x.counting_dice(value, self.print_mode), sorted(self.players)))
        return not real_quantity >= quantity
