# Object Oriented Game

## Overview
This project is an implementation of the classic Connect 4 game using Java. The game allows two players to take turns dropping colored discs from the top into a vertically suspended grid. The objective is to be the first player to form a horizontal, vertical, or diagonal line of four of one's own discs.

For an in-depth breakdown of the code, please read the presentation found at 'objectOrientedGame.pdf'

## Features
- Two-player gameplay.
- Graphical user interface (GUI) for interactive play.
- Detection of win conditions (horizontal, vertical, and diagonal).
- Detection of draw condition when the board is full.

## Getting Started

### Prerequisites
- Java Development Kit (JDK) 8 or higher.
- An Integrated Development Environment (IDE) like Visual Studio Code.

### Classes
- connect4Game.java: Manages the text-based version of the game and allows it to be run. Handles all printing in the terminal. 
- connect4Board.java: Manages the game board and checks if a player has won.
- connect4GUI.java: Manages the Graphical User Interface (GUI) version of the game and allows it to be run.

### Installation
Clone the repository:

git clone https://github.com/qmmartin/Portfolio

Open the project in your preferred IDE.

### Running the Game 
#### For Text-Based Game
1. Open the 'gameProject' folder in Visual Studio or other IDE
2. Run 'connect4Gameame.java'
3. Use Terminal to input text according to prompt

<img src="images\textGame1.PNG" width="400">

#### For GUI-Based Game
1. Open 'gameProject' in Visual Studio or other IDE
2. Run 'connect4GUI.java'
3. Click columns to place pieces

<img src="images\guiGame1.PNG" width="400">

### How to Play
1. Start the game by running the Main.java file.
2. Players take turns to drop their discs by clicking on a column.
3. The game will automatically check for win or draw conditions after each turn.
4. The game ends when a player forms a line of four discs or the board is full without a winner.
5. Press any key to start a new game.

## Acknowledgements
- Inspired by the classic Connect 4 game.

