# Path Finding Visualizer using Pygame

This Python script utilizes Pygame to create a visual representation of pathfinding algorithms on a grid. It allows users to visualize how algorithms like A\* search algorithm find the shortest path between a start and an end point.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## Overview

This script provides a graphical user interface (GUI) to visualize the process of pathfinding algorithms on a grid. It enables users to set a start point, an end point, and add barriers, demonstrating how the selected pathfinding algorithm navigates through obstacles to reach the target.

## Features

- Allows users to set the start and end points on the grid.
- Provides the ability to create barriers to observe obstacle traversal.
- Utilizes the A\* search algorithm to find the shortest path.
- Visualizes the process step-by-step using Pygame's graphical interface.

## Usage

To use the pathfinding visualizer:

1. **Set Start and End Points:**
   - Left-click on the grid to set the start point (orange color) and the end point (turquoise color).
2. **Create Barriers:**
   - Left-click and drag to create barriers (black color) that the algorithm should navigate around.
   - Right-click on a barrier to remove it.
3. **Run the Algorithm:**
   - Press the `SPACEBAR` after setting the start and end points to initiate the algorithm.
4. **Clear the Grid:**
   - Press `C` to clear the grid and start over.

## How to Run

To run the code, follow these steps:

1. Ensure you have Python installed on your system.
2. Install Pygame library if not already installed:
   ```bash
   pip install pygame
   ```
3. Run the Python script `pathfinding_visualizer.py`.

Example:

```bash
python pathfinding_visualizer.py
```

## Contributing

Contributions are welcome! If you have any ideas for improvement, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](License)
