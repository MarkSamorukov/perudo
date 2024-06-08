from game.move import Move
import tensorflow as tf
import numpy as np


model_path = 'C:/Users/marks/mark/PycharmProjects/perudo/models/deep_model_perudo_1/deep_model_perudo_1.keras'


class DeepModelPerudo1:
    def __init__(self, move, dice_counter, dice, round_moves):
        self.move = move
        self.dice_counter = dice_counter
        self.dice = dice
        self.round_moves = round_moves

    def generate_normalize_data(self):

        data = []

        for i in (1, 2, 3, 4, 5, 6):
            data.append([self.dice.count(i) / 5, i / 6])

        data.append([0, len(self.dice) / 5])
        data.append([0, (self.dice_counter - len(self.dice)) / 5])

        for move in self.round_moves[:-1][::-1][:4]:
            data.append([move[1]['quantity'] / 10, move[1]['value'] / 6])

        for _ in range(12 - len(data)):
            data.append([0, 0])

        return np.array([data])

    def do_move(self):

        data = self.generate_normalize_data()

        if not self.move.move['first_move']:
            loaded_model = tf.keras.models.load_model(model_path)

            if loaded_model.predict(data)[0] > 0.5:
                return Move({
                    'to_believe': False,
                    'value': 0,
                    'quantity': 0,
                    'first_move': False
                })

        all_valid_movies = self.move.generate_all_valid_moves(self.dice_counter)

        dice_counter_without_me = self.dice_counter - len(self.dice)

        math_exp_list = [self.dice.count(1) + dice_counter_without_me / 6]
        for i in (2, 3, 4, 5, 6):
            math_exp_list.append(self.dice.count(i) + self.dice.count(1) + dice_counter_without_me / 3)

        diff = 999999
        res = Move({
            'to_believe': True,
            'value': 0,
            'quantity': 0,
            'first_move': False
        })
        for move in all_valid_movies:
            if not move.move['to_believe']:
                continue
            if abs(move.move['quantity'] - math_exp_list[move.move['value'] - 1]) < diff:
                if move > res:
                    diff = abs(move.move['quantity'] - math_exp_list[move.move['value'] - 1])
                    res = move
        return res
