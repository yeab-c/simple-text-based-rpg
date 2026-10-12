A short text game for the terminal, written in Python.

Floods have cut off a village in the highlands. Four travelers carry the only medicine that can save it. Ten trials stand in the way, and not everyone will make it.

## How to play

1. Enter four character names, separated by commas.
2. Each name is randomly given a role: Scout, Blacksmith, Healer, or Hunter.
3. For each trial, read the story and choose who will do the task.
4. Every task costs the chosen traveler some health. If their health reaches 0, they die, but the task still counts as done.
5. You win if at least one traveler is alive after all trials. You lose if all four die first.

## Roles and starting health

| Role | Health |
|------|--------|
| Scout | 30 |
| Healer | 35 |
| Hunter | 40 |
| Blacksmith | 45 |

Health is hidden during play, so choose carefully. The trials cost 165 health in total, which is more than the group has, so someone has to take the heavy tasks and fall.

## Run it

Requires Python 3.

```
python game.py
```

## Features

- Roles are assigned randomly each game.
- Trials are shuffled each game, so the path is different every time.
- Built with classes: a `Character` base class, one subclass per role, a private health value, and class methods to check whether everyone is dead.

## Ideas for later

- Show each traveler's health in the choice menu.
- Give each role a strength or weakness for certain tasks.
- Different endings depending on how many travelers survive.
- Play again without restarting the program.
