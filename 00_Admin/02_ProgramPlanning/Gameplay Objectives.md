Gameplay Objectives
===================

This document is a wishlist and area for planning for features and actions that are to be implemented in Sakuru.

Divided into sections, the contents list below is a useful resource for navigating through this document.

***

Contents
--------

1. Colour Interactions
2. Level Handling


***

1. Colour Interactions
----------------------

### 1.1 Thesis ###

*Balls can pass through coloured circles that they are composed of.*

That is:

  1. A white ball passes through
    - All colours
  2. A green ball passes through
    - Green
    - White
  3. An orange ball will pass through
    - White
    - Red
    - Yellow

### 1.2 Matrix ###

<table>
  <tr>
    <td>&nbsp;</td>
    <td>White</td>
    <td>Red</td>
    <td>Yellow</td>
    <td>Blue</td>
    <td>Orange</td>
    <td>Purple</td>
    <td>Green</td>
  </tr>
  <tr>
    <td>White</td>
    <td>Y</td>
    <td>Y</td>
    <td>Y</td>
    <td>Y</td>
    <td>Y</td>
    <td>Y</td>
    <td>Y</td>
  </tr>
  <tr>
    <td>Red</td>
    <td>Y</td>
    <td>Y</td>
    <td>-</td>
    <td>-</td>
    <td>Y</td>
    <td>Y</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Yellow</td>
    <td>Y</td>
    <td>-</td>
    <td>Y</td>
    <td>-</td>
    <td>Y</td>
    <td>-</td>
    <td>Y</td>
  </tr>
  <tr>
    <td>Blue</td>
    <td>Y</td>
    <td>-</td>
    <td>-</td>
    <td>Y</td>
    <td>-</td>
    <td>Y</td>
    <td>Y</td>
  </tr>
</table>

### 1.3 Notes ###

-  If a ball cannot pass through a circle (for example, a red ball through a yellow circle), it then bounces off as it would any other ball.


***

2. Level Handling
-----------------

### 2.1 Method Brainstorm ###
- Hugh suggested YAML for handling level input / output.
  * This stores as plain text, but in a structured mannar.
  * Easy to edit etc. - one of YAML's major features is that it is easy to be humanly readable.
- Using pickle
  * Again, saves as plain text, but using a splitter item (for example, {><} as with the Learner Driver Logbook makes it harder to understand.

### 2.2 Data Representation ###
- Each level needs the follow data to function:
  * The starting positions and characteristics of balls and circles (separately).
  * The limit on circles / whatever
  * The Obsessive Completion Distinction criteria
  * Any storyline or tutorial text that must appear in level
  * Level name and number

***

3. Game Loop Planning
---------------------

### 3.1 Method Brainstorm ###

