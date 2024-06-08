import json

from game.game import Game

from models.random_model import RandomModel
from models.math_expectation_model import MathExpectationModel
from models.human_model import HumanModel


new_stat = []
for i in range(10000):
    print(i)

    game = Game(2, ['Alice', 'Bob'],
                [MathExpectationModel, MathExpectationModel], print_mode=0)

    stat, player = game.start_game()

    new_stat.append(stat)


with open('../all_games.json', 'w', encoding='utf-8') as file:
    json.dump(new_stat, file, indent=2)
