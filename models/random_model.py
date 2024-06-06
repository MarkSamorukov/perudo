import random


class RandomModel:
    def __init__(self, move, dice_counter, *_):
        self.move = move
        self.dice_counter = dice_counter

    def do_move(self):
        all_valid_movies = self.move.generate_all_valid_moves(self.dice_counter)

        return random.choice(all_valid_movies)
