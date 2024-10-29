# Rock Paper Scissors Game

## Overview
This is a simple command-line Rock Paper Scissors game developed in Python. The game includes user authentication, allowing players to create accounts and log in to play. Players can track their scores, lives, and draws while competing against the computer.

## Features
- User authentication with username and password
- Strong password validation
- Score tracking
- Lives system
- Help commands for game rules and status
- Clear terminal output for game over

## Getting Started

### Prerequisites
- Python 3.x installed on your machine
- Basic knowledge of running Python scripts

### Installation
- Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Rock-Paper-Scissors.git
   cd Rock-Paper-Scissors
   ```

### Running the Game
1. To set up an account, run:
   ```bash
   python acc_setup.py
   ```

2. To play the game, run:
   ```bash
   python main.py
   ```

### How to Play
- After logging in, you will be prompted to choose between Rock, Paper, or Scissors.
- You can also use the following commands:
  - `!help`: Display the game rules
  - `!lives`: Check remaining lives
  - `!score`: Check your score
  - `!drew`: Check how many times you've drawn
  - `exit`: Exit the game

## File Structure
Rock Paper Scissors <br>
|-- acc_setup.py        # Account setup script for creating user accounts <br>
|-- main.py             # Main game logic for the Rock Paper Scissors game <br> 
|-- accounts.txt        # File storing usernames and passwords <br>
|-- README.md           # Project documentation <br>


## Author
Developed by Yash Mittal.  
Visit [Website](https://yashmittalz.github.io) for more projects.
