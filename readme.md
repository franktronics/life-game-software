# Conway's Game of Life

A Conway's **Game of Life** simulation on a large toroidal grid, built with **PyQt5** and **NumPy**.

## Description

This software simulates cell evolution according to Conway's Game of Life rules on a toroidal grid (edges wrap around). It offers two modes:

- **Auto Mode**: the simulation runs continuously with an adjustable speed (1 to 10).
- **Manual Mode**: advance step by step using the "Next" button.

Users can:
- Click cells to toggle them alive/dead
- Play / Pause the simulation
- Reset the grid with a glider pattern at the center
- Clear the entire grid

## Project structure

```
├── main.py                  # Entry point
├── game/
│   └── game_of_life.py      # Game logic (NumPy matrix, generations)
├── ui/
│   ├── main_window.py       # Main window
│   ├── grid_widget.py       # Clickable cell grid
│   ├── controls_widget.py   # Control panel (play, pause, speed, mode)
│   ├── cell_button.py       # Button representing a single cell
│   └── form_fiel.py         # Generic label + content widget
├── utils/
│   └── variables.py         # Centralized configuration (grid size, etc.)
├── styles/
│   └── style.qss            # Qt stylesheet
├── resources/               # Resources (empty for now)
└── requirements.txt
```

## Prerequisites

- Python 3.8 or higher

## Installation

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   - Linux / macOS:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scriptsctivate
     ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py
```

## Dependencies

- **numpy** — matrix computation for cell state
- **PyQt5** — graphical user interface
