import json

from game.game import Game

from models.random_model import RandomModel
from models.math_expectation_model import MathExpectationModel
from models.human_model import HumanModel
from models.deep_model_perudo_1.deep_model_perudo_1 import DeepModelPerudo1


game = Game(2, ['Alice', 'Kirill'],
            [MathExpectationModel, DeepModelPerudo1], print_mode=1)

stat, winner = game.start_game()

