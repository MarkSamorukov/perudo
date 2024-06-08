from game.game import Game

from models.random_model import RandomModel
from models.math_expectation_model import MathExpectationModel
from models.human_model import HumanModel
from models.deep_model_perudo_1.deep_model_perudo_1 import DeepModelPerudo1

model_1, model_2 = DeepModelPerudo1, DeepModelPerudo1

deep = 50

result = {"model_1": 0, "model_2": 0}

for _ in range(deep // 2):
    game = Game(2, ["model_1", "model_2"], [model_1, model_2], print_mode=0)
    print(_)

    stat, player = game.start_game()
    winner = player.name
    result[winner] += 1

for _ in range(deep // 2):
    game = Game(2, ["model_2", "model_1"], [model_2, model_1], print_mode=0)
    print(_ + deep // 2)

    stat, player = game.start_game()
    winner = player.name
    result[winner] += 1

print(result)


