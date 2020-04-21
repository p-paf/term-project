### Align3 - a simple game
This repository covers the development of a simple board game step by step into a modular, maintainable and resuable code base.

### Changes
This branch adds a few bells and whistles to `stage_2` branch namely,

1. Check if user has clicked a filled tile
2. Add a border of randomly chosen images at the bottom and right end of the board

You can check the open [PR](https://github.com/p-paf/term-project/pull/1) from `stage_3` to `stage_2` to see the differences.

### Running the game
Run the game with `python3 play.py`. If this fails you might need to install `python3-tk` library for your python version.

For debugging, you can open a module in the interpreter with the following command `python3 -i state.py`. Following this you can type commands related to state into the interpreter and see their result.

### Making your own game
1. Fork the repo
2. Make your own game

The code has been designed to be modular and will suit the needs of most 2D, perfect information, turn-based strategy board games.
