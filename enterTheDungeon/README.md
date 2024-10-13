# Adventure Game

## Overview

Welcome tot the Adventure Game project! This is a text-based adventure game designed to introduce you to Object-Oriented
Programming (OOP) concepts in Python. Through this project, you will become familiar with how to create classes, and
instantiate objects to build a scalable and modular codebase.

## Structure of the codebase

```
AdventureGameOOP/
├── main.py             # Entry point for runnning the game
├── game_play.py        # Game loop
├── README.md
└── game
    ├── __init__.py     # Initializes the `game` package
    ├── item.py         # Contains the Item class
    ├── player.py       # Contains the Player class
    ├── room.py         # Contains the Room class
    
```

## Getting Started
### Prerequisites
- Python 3.x installed on your computer
- A text editor or IDE (like PyCharm, VSCode etc.)

### How to run the game
1. Fork this repo to your local machine
2. Navigate to the project directory in your terminal
3. Run the game using the following command:

```
    python game.py
```

This will start the adventure game and prompt you for commands as you navigate through the rooms and interact with items.

## Understanding the Code
This adventure game is built using basic OOP principles. Here's how the main components work:

### Classes and Objects
- Classes are blueprints for creating objects. Each class defines the attributes (data) and methods (behavior) that its objects will have.
- Objects are instances of classes. For example an "Item" is a class, and a "sword" is an object (instance) of a class

### Key Classes in the Game
- "Room" represents a room in the game. It has a name, a description, and coordinates to place the room on a map. The rooms won't be visible to the player yet. The player needs to discover the rooms before the player could display the room on the map.
- "Item" represents items that players could interact with. The only interaction right now is "picking it up". It is up to you to add more functionality to this part.
- "Player" represents the player, who can move between rooms and picking up items
Ideas of new classes to add:
- "Building" represents a building in which certain rooms are present
- "Enemy" represents a certain character with bad intentions

## Exercise: Extending the Game
The way to get familiar with the idea of Object-Oriented programming (note: we're only scratching the surface of OOP) is to get your hands dirty!

### Creating new rooms
The way to start understanding the code a bit better.
To create a new room:
1. Open "game_play.py"
2. Instantiate a new "Room" object with a name, description, and coordinates.
3. Add the room to the list of all rooms

### Creating new items
1. Open "game_play.py"
2. Instantiate a new "Item" object with a name and description
3. Add it to a room

### Enhancing gameplay
To actually learn how to add new classes and instantiate object (or instances) of those objects. You will need to start thinking about how to make the game play more interestingly.
- Add health points to the player
- Add an enemy class, and place those enemies in the different rooms
  - These enemies provide riddles/puzzles to solve
  - By failing to solve the riddles: the health of the player goes down
- Add a treasure class
- Develop a storyline
- The possibilities are only limited by your own creativity!

## Conclusion
This project serves as a base to explore and learn OOP concepts in Python. By creating new features, you will gain experiencing in designing and working with classes, and insitializing objects.

Feel free to modify and expand te game as you see fit.

Happy coding :)