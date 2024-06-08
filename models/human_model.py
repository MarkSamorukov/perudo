from game.move import Move


class HumanModel:
    def __init__(self, move, dice_counter, dice, *_):
        self.move = move
        self.dice_counter = dice_counter
        self.dice = dice

    def do_move(self):
        print(f"Ваш ход (на столе {self.dice_counter} костей). Ваши кости:")
        print(*self.dice)
        move = input()
        try:
            quantity, value = map(int, move.split())
            return Move({
                'to_believe': True,
                'value': value,
                'quantity': quantity,
                'first_move': False
            })
        except ValueError:
            return Move({
                'to_believe': False,
                'value': 0,
                'quantity': 0,
                'first_move': False
            })
