# Object Oriented Game Project

*This markdown file is meant to serve as a quick summary of the pdf presentation listed within this file*

This project was created in my Programming II class focused on learning object oriented methods of coding through java, as well as learning basic Python skills. 

This project required the creation of a text-based back-end for a game that would later be connected to an interactive Graphical User Interface (GUI) front-end created using Java's Swing library. 

To start my game, I decided to code two separate classes for the game and board. The Game class would handle all the game logic, such as checking if a player has won and keeping track of whose turn it is. The Board object, meanwhile, kept track of the board state and where pieces had been placed.

When adding a piece, the add function would iteratively cycle through the rows in the column from top to bottom until it hit either a full space or the last space. Once this was reached, a piece would be placed depending on which player was taking their turn. 

If a move is invalid, i.e. off the board or in a full column, then the player would need to take a different move before the game can progress. 

When a column is hovered over with the mouse, the lowest empty space in that column is highlighted with a bright circle. 

To end the game, the board checks after each valid move to see whether or not a player has 4 pieces in a row horizontally, vertically, or diagonally.

The horizontal check scanned from the bottom row to the top row, and from left to right, checking if any 4 pieces in a row were the same.

The veritcl check scanned each column from left to right, and from the bottom to the top, checking if any 4 pieces in a column were the same color and in sequence.

The diagonal check first scanned from the top left of the board to the bottom right in diagonal stripes to see if any 4 of the pieces were sequential in a diagonal. The diagonal check then scanned from top right to bottom left of each diagonal stripe to check for the same.

If any player has won, the GUI shows a screen saying which player has won.

