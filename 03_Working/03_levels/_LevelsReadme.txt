ABOUT LEVEL FILES
=================

Level files are structued in such a way as to make them
humanly readable but at the same time be read easily by
Python.

This is achieved using a library called YAML, which
stands for 'Yet Another Markup Language'. It works by
creation lists within a plain ASCII text file that look
very much like those found in Markdown, which was
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