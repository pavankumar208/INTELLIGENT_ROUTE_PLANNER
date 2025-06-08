
# Intelligent Multi-Stop Route Planner with Traffic & Weather Adjustments

## Overview
This Python project provides an intelligent route planning system capable of computing the shortest path between multiple cities while considering real-world factors like traffic and weather delays. It uses Dijkstra's algorithm with dynamically adjusted edge weights for more realistic travel estimations.

## Features
- **Graph-Based Navigation**: Cities and roads are modeled as a graph using adjacency lists.
- **Dijkstra’s Algorithm**: Finds the shortest path between two cities.
- **Traffic & Weather Adjustments**: Route costs are dynamically modified using simulated delay data.
- **Multi-Stop Routing**: Users can plan routes with multiple intermediate stops.
- **State-Wise City Categorization**: Allows users to select cities based on Indian states.

## Key Components
- `Graph`: A class for building and navigating the graph of cities and roads.
- `dijkstra()`: Computes shortest path using a custom modifier function.
- `combined_modifier()`: Modifies travel costs using simulated traffic and weather data.
- `display_cities_by_state()`: Lists all available cities grouped by their respective states.
- `main()`: CLI-based user interaction for entering city names, stops, and computing the final route.

## Dependencies
- No external dependencies beyond Python’s standard libraries (`heapq`, `input`, `print`)

## Example Usage
```
=== Intelligent Multi-Stop Route Planner ===
Enter starting city: Hyderabad
How many stops do you want to add? (0 for direct): 2
Enter stop 1: Vijayawada
Enter stop 2: Chennai
Enter final destination city: Bangalore

Optimal Route: Hyderabad -> Vijayawada -> Guntur -> Ongole -> Nellore -> Chennai -> Vellore -> Bangalore
Estimated Total Travel Distance (with traffic & weather): 1093.23 km
```

## How to Run
1. Save the script in a file, e.g., `route_planner.py`
2. Run it using Python 3:
   ```bash
   python route_planner.py
   ```

## Author
Pavan Kumar

## License
This project is provided for educational purposes only.
