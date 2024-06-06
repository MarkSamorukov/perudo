from game.move import Move


class MathExpectationModel:
    def __init__(self, move, dice_counter, dice, *_):
        self.move = move
        self.dice_counter = dice_counter
        self.dice = dice

    def do_move(self):
        all_valid_movies = self.move.generate_all_valid_moves(self.dice_counter)

        value = self.move.move['value']
        quantity = self.move.move['quantity']
        dice_counter_without_me = self.dice_counter - len(self.dice)

        math_exp_list = [self.dice.count(1) + dice_counter_without_me / 6]
        for i in (2, 3, 4, 5, 6):
            math_exp_list.append(self.dice.count(i) + self.dice.count(1) + dice_counter_without_me / 3)

        math_exp_value = math_exp_list[value - 1]

        if quantity > math_exp_value:
            return Move({
                'to_believe': False,
                'value': 0,
                'quantity': 0,
                'first_move': False
            })

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
            if abs(move.move['quantity'] - math_exp_list[move.move['value'] - 1]) <= diff:
                if move > res:
                    diff = abs(move.move['quantity'] - math_exp_list[move.move['value'] - 1])
                    res = move
        return res
