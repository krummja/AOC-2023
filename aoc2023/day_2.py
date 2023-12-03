from __future__ import annotations
from typing import NamedTuple, Literal
import re
from functools import reduce
from load import load_input


Color = Literal["red"] | Literal["green"] | Literal["blue"]
GameId = int


class Game(NamedTuple):
    game_id: GameId
    game_values: list[list[tuple[int, str]]]


def parse_game_id(gamestr: str) -> tuple[GameId, str] | None:
    re_game_id = re.compile(r"^Game (\d*):")
    if matched := re_game_id.match(gamestr):
        group_part = matched.group()
        remainder = gamestr[len(group_part):].strip()
        return int(matched.groups()[0]), remainder


def parse_value(valuestr: str) -> tuple[int, str]:
    count, color = valuestr.split(" ")
    return (int(count), color.strip())


def parse_game_values(gamestr: str):
    selections = [selection.strip() for selection in gamestr.split(";")]
    selections = [
        [value.strip() for value in selection.split(",")]
        for selection in selections
    ]

    game_values = []
    for selection in selections:
        game_selections = []
        for valuestr in selection:
            selection_value = parse_value(valuestr)
            game_selections.append(selection_value)
        game_values.append(game_selections)
    return game_values


def parse_game(gamestr: str, games: list[Game]):
    if result := parse_game_id(gamestr):
        game_id, remainder = result
        game_values = parse_game_values(remainder)

        game = Game(
            game_id=game_id,
            game_values=game_values,
        )

        games.append(game)
    return games


def validate_game_one(game: Game, reds: int, greens: int, blues: int) -> int:
    max_reds = 0
    max_greens = 0
    max_blues = 0

    for game_selection in game.game_values:
        for game_value in game_selection:
            if game_value[1] == "red":
                max_reds = max(game_value[0], max_reds)
            if game_value[1] == "green":
                max_greens = max(game_value[0], max_greens)
            if game_value[1] == "blue":
                max_blues = max(game_value[0], max_blues)

    if max_reds > reds or max_greens > greens or max_blues > blues:
        return 0
    return game.game_id


def validate_game_two(game: Game, reds: int, greens: int, blues: int) -> int:
    """
    Game 1:
        r   g   b
        4   0   3
        1   2   6
        0   2   0
        ---------
        4   2   6
    """
    max_reds = 0
    max_greens = 0
    max_blues = 0

    result = []

    for game_selection in game.game_values:
        for game_value in game_selection:
            if game_value[1] == "red":
                max_reds = max(game_value[0], max_reds)
            if game_value[1] == "green":
                max_greens = max(game_value[0], max_greens)
            if game_value[1] == "blue":
                max_blues = max(game_value[0], max_blues)

        result = [max_reds, max_greens, max_blues]

    return reduce((lambda n, m: n * m), result)


def main() -> None:
    with load_input(2) as file:
        inputs = [line.rstrip("\n") for line in file]

        games = []
        for game in inputs:
            parse_game(game, games)

        game_results = []
        for game in games:
            result = validate_game_one(game, reds=12, greens=13, blues=14)
            game_results.append(result)

        print(sum(game_results))

        game_results = []
        for game in games:
            result = validate_game_two(game, reds=12, greens=13, blues=14)
            game_results.append(result)

        print(sum(game_results))


if __name__ == '__main__':
    main()
