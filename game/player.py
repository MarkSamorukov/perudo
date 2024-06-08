import random
from art import text2art


class Player:
    def __init__(self, name, turn: int, dice_counter: int, model) -> None:
        self.name = name
        self.in_game: bool = True
        self.turn: int = turn
        self.dice_counter: int = dice_counter
        self.model = model
        self.dice: list[int] = self.generate_dice()

    def __str__(self) -> str:
        return text2art("".join(map(str, self.dice)), font='block')

    def __lt__(self, other) -> bool:
        if isinstance(other, Player):
            return self.turn < other.turn

    def generate_dice(self) -> list[int]:
        dots = [1, 2, 3, 4, 5, 6]
        dice = []
        for _ in range(self.dice_counter):
            dice.append(random.choice(dots))

        return dice

    def counting_dice(self, value: int, print_mode) -> int:
        if self:
            if print_mode == 1:
                print(f"{self.name}) ", end='')
                print(*self.dice)
            if value == 1:
                return self.dice.count(value)
            else:
                return self.dice.count(value) + self.dice.count(1)
        else:
            return 0

    def reroll_dice(self):
         self.dice = self.generate_dice()

    def discard_dice(self) -> None:
        self.dice_counter -= 1
        if self.dice_counter == 0:
            self.in_game = False

    def set_turn(self, turn: int) -> None:
        self.turn = turn

    def __bool__(self) -> bool:
        return self.in_game

    def do_move(self, *data):
        return self.model(*data).do_move()


# print(Player(1, 5, 0))
