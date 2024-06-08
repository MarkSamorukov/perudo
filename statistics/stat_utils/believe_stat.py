import json


with open('../all_games.json', 'r', encoding='utf-8') as file:
    all_games = json.load(file)

res = []

for game in all_games:
    for round in game['rounds']:

        train = []

        inspector = round['moves'][-1][0]
        inspector_dice = round['player_dice'][inspector]

        for i in (1, 2, 3, 4, 5, 6):
            train.append([inspector_dice.count(i) / 5, i / 6])

        train.append([0, len(round['player_dice'][inspector]) / 5])

        for p in round['player_names']:
            if p != inspector:
                train.append([0, len(round['player_dice'][p]) / 5])

        for move in round['moves'][:-1][::-1][:4]:
            train.append([move[1]['quantity'] / 10, move[1]['value'] / 6])

        for _ in range(12 - len(train)):
            train.append([0, 0])

        test = inspector != round['loser']

        res.append({
            "train": train,
            "test": test
        })

with open('../believe_normalize_data.json', 'w', encoding='utf-8') as file:
    json.dump(res, file, indent=2)
