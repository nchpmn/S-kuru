ABOUT LEVEL FILES
=================

Level files are structued in such a way as to make them
humanly readable but at the same time be read easily by
Python.

This is achieved using a library called YAML, which
stands for 'Yet Another Markup Language'. It works by
creating lists within a plain ASCII text file that look
very much like a <ul> as found in Markdown, which was
created by Daring Fireball.

Structure of a Level
--------------------

From Python's perspective, the level file has four main
sections:

  1. List of level text
    - LevelName, HintText, [WinType, WinCondition]
  2. List of balls in level
    - A list per circle of: [PosX, PosY], CircleSize, ColourID
  3. List of circles in level
    - [PosX, PosY], BallSize, BallColourID
  4. List of exits in level
    - [PoxX, PosY], ExitSize, ExitColourID

In the YAML level file, these are represented as:

    - - Level Name                 ----+
      - Level Hint                     |-- Level Text
      - [WinType, WinCondition]    ----+
    - - - !!python/tuple [PosX, PosY] --+            -----------+
        - Size (Radius)                 |-- Single Circle       |
    - ColourID                    --+                       |-- Circles List
      - - !!python/tuple [300, 200]                             |
        - 150                                                   |
        - 2                                          -----------+
    - - - !!python/tuple [175, 180]
        - 15
        - 0
      - - !!python/tuple [200, 200]
        - 15
        - 0
      - - !!python/tuple [280, 100]
        - 20
        - 0

WinType, WinCondition
---------------------

These two variables to control how the player can win a
level. These are WinType and WinCondition.

To access these from within Python, we use:

    loadText[2][0] and loadText[2][1]

WinType defines what type of level this is: timed, circles
or some other type that I haven't thought of yet.
WinCondition sets the condition for winning: finish within
30 seconds, use less than 3 circles, that sort of thing.

### WinType Parameters ###

Set WinType to this to play this sort of level.

1. Timed. Get all balls to exits within X seconds.
2. Circles. Use less than X circles to complete level.
3. Selection. Only get X colourID balls to exit.
