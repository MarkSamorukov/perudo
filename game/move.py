import random


class Move:
    def __init__(self, move) -> None:
        """
        move = {
            to_believe: bool,
            value: int,
            quantity: int,
            first_move: bool,
        }
        """
        self.move = move

    def __str__(self) -> str:
        if not self.move['to_believe']:
            return 'Не верю'
        else:
            phrase = random.choice(['Пусть будет', 'Думаю наберется', 'Уверен что есть', 'Наверное, я скажу'])
            return f'{phrase} {self.move["quantity"]} {self.move["value"]}'

    def __bool__(self) -> bool:
        return self.move['to_believe']

    def __gt__(self, other) -> bool:
        if isinstance(other, Move):
            if not self.move['to_believe']:
                return True
            else:
                if self.move['value'] == 1 and other.move['value'] == 1:
                    return self.move['quantity'] > other.move['quantity']
                elif self.move['value'] == 1:
                    return self.move['quantity'] >= other.move['quantity'] / 2
                elif other.move['value'] == 1:
                    return self.move['quantity'] >= other.move['quantity'] * 2 + 1
                else:
                    if self.move['quantity'] > other.move['quantity']:
                        return True
                    elif self.move['quantity'] == other.move['quantity']:
                        return self.move['value'] > other.move['value']
                    else:
                        return False

    def generate_all_valid_moves(self, dice_counter: int) -> list:
        all_moves = [Move({"to_believe": False, "value": 0, "quantity": 0, "first_move": False})]
        for value in (1, 2, 3, 4, 5, 6):
            if self.move['first_move'] and value == 1:
                continue
            for quantity in range(1, dice_counter + 1):
                all_moves.append(Move({
                    'to_believe': True,
                    'value': value,
                    'quantity': quantity,
                    'first_move': False,
                }))

        return list(filter(lambda x: x > self, all_moves))
