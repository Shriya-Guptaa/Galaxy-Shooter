# 🚀 Galaxy Shooter

This is a simple **two-player space shooter game** built with **Pygame**.  
Players can control their spaceships, shoot at each other, and try to deplete their opponent's health to win.

---

## ✨ Key Features

- 🎮 **Two-Player Gameplay**: Compete against a friend on the same keyboard.  
- ❤️ **Health System**: Each player starts with 10 health points.  
- 🔫 **Bullet Mechanics**: Players can fire a limited number of bullets at a time.  
- 🔊 **Sound Effects**: Audio cues for firing bullets and hitting an opponent.  
- 📦 **Modular Codebase**: Organized into three separate files (`main.py`, `game_functions.py`, and `constants.py`) for clarity and easy maintenance.  

---

## ▶️ How to Play

**🟡 Yellow Spaceship (Left side):**
- Move: `W`, `A`, `S`, `D`  
- Fire: `Left Ctrl`  

**🔴 Red Spaceship (Right side):**
- Move: Arrow Keys (`↑`, `↓`, `←`, `→`)  
- Fire: `Right Ctrl`  

👉 The first player to reduce their opponent's health to **zero** wins the round.

---

## 💻 Installation

Before running the game, ensure you have **Python 3.8+** installed.

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/galaxy-shooter.git
   cd galaxy-shooter


2. **Create and activate a virtual environment(recommended)**

   ```bash
   python -m venv venv
   ```

   * On **Windows**:

     ```bash
     venv\Scripts\activate
     ```
   * On **macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt   

---

## 🕹️ Running the Game

After installing the dependencies, start the game with:

```bash
python main_game.py
```

---

## 📁 File Structure

```
galaxy-shooter/
│── main_game.py         # Main entry point of the game (game loop, input, state management)
│── game_functions.py    # Core game logic (drawing, movement, bullets, etc.)
│── constants.py         # Global variables (dimensions, colors, fonts, assets)
│── requirements.txt     # Required Python libraries (pygame)
│── Assets/              # Images and sound effects used in the game
```

---

## 🙏 Acknowledgements

I want to express my sincere gratitude to [Tech with Tim (Tim Ruscica)](https://github.com/techwithtim) for his invaluable **Python Game Development Tutorials**.  
His clear, well-structured videos were instrumental in providing the foundational knowledge and practical examples necessary to build this game.  

This project was directly inspired by his content, and his guidance was essential to my learning process.

---


