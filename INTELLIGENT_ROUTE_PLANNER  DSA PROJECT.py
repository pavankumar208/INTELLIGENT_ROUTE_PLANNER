import heapq

# ----------------- Graph and Dijkstra ---------------------
class Graph:
    def __init__(self):
        self.edges = {}  # city: list of (neighboring_city, base_cost)

    def add_edge(self, from_city, to_city, cost):
        self.edges.setdefault(from_city, []).append((to_city, cost))
        self.edges.setdefault(to_city, []).append((from_city, cost))  # Bidirectional

    def dijkstra(self, start, end, modifier_fn):
        queue = [(0, start)]
        visited = set()
        min_cost = {start: 0}
        parent = {start: None}

        while queue:
            current_cost, city = heapq.heappop(queue)
            if city in visited:
                continue
            visited.add(city)

            if city == end:
                break

            for neighbor, base_cost in self.edges.get(city, []):
                modified_cost = modifier_fn(city, neighbor, base_cost)
                new_cost = current_cost + modified_cost
                if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    parent[neighbor] = city
                    heapq.heappush(queue, (new_cost, neighbor))

        path = []
        current = end
        while current:
            path.append(current)
            current = parent.get(current)
        return path[::-1], min_cost.get(end, float('inf'))

# ----------- Traffic and Weather Delay Simulations ---------
def get_traffic_delay(from_city, to_city):
    traffic_delay = {
        ('Hyderabad', 'Chennai'): 1.4,
        ('Chennai', 'Bangalore'): 1.2,
        ('Mumbai', 'Pune'): 1.6,
        ('Delhi', 'Bhubaneswar'): 1.3,
        ('Vijayawada', 'Visakhapatnam'): 1.5,
    }
    return traffic_delay.get((from_city, to_city), traffic_delay.get((to_city, from_city), 1.0))

def get_weather_delay(city):
    weather_delay = {
        'Mumbai': 1.4,
        'Chennai': 1.3,
        'Bhubaneswar': 1.5,
        'Visakhapatnam': 1.2
    }
    return weather_delay.get(city, 1.0)

def combined_modifier(from_city, to_city, base_cost):
    traffic = get_traffic_delay(from_city, to_city)
    weather = get_weather_delay(to_city)
    return base_cost * traffic * weather

# ------------------- Graph Builder ------------------------
def build_city_graph():
    g = Graph()
    edges = [
        ('Hyderabad', 'Vijayawada', 275), ('Vijayawada', 'Guntur', 35), ('Guntur', 'Ongole', 120),
        ('Ongole', 'Nellore', 130), ('Nellore', 'Chennai', 175), ('Chennai', 'Vellore', 140),
        ('Vellore', 'Bangalore', 210), ('Bangalore', 'Mysore', 150), ('Mysore', 'Mangalore', 250),
        ('Mangalore', 'Goa', 360), ('Goa', 'Belgaum', 100), ('Belgaum', 'Pune', 335),
        ('Pune', 'Mumbai', 150), ('Mumbai', 'Nagpur', 820), ('Nagpur', 'Raipur', 285),
        ('Raipur', 'Bilaspur', 120), ('Bilaspur', 'Jagdalpur', 330), ('Jagdalpur', 'Bhubaneswar', 600),
        ('Bhubaneswar', 'Cuttack', 25), ('Cuttack', 'Rourkela', 300), ('Visakhapatnam', 'Srikakulam', 120),
        ('Visakhapatnam', 'Vijayawada', 350), ('Hyderabad', 'Warangal', 145), ('Warangal', 'Khammam', 130),
        ('Khammam', 'Vijayawada', 140), ('Chennai', 'Tirupati', 140), ('Tirupati', 'Chittoor', 80)
    ]
    for from_city, to_city, cost in edges:
        g.add_edge(from_city, to_city, cost)
    return g

# ---------------- Display Cities by State ------------------
def display_cities_by_state():
    state_cities = {
        "Andhra Pradesh": ["Vijayawada", "Visakhapatnam", "Guntur", "Ongole", "Nellore", "Tirupati", "Chittoor", "Srikakulam"],
        "Telangana": ["Hyderabad", "Warangal", "Karimnagar", "Khammam"],
        "Tamil Nadu": ["Chennai", "Vellore", "Salem", "Coimbatore", "Madurai", "Tirupati"],
        "Kerala": ["Kochi", "Thiruvananthapuram", "Kozhikode"],
        "Karnataka": ["Bangalore", "Mysore", "Mangalore"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
        "Goa": ["Goa", "Belgaum"],
        "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela"],
        "Chhattisgarh": ["Raipur", "Bilaspur", "Jagdalpur"]
    }

    print("\\n=== Available Cities by State ===\\n")
    for state, cities in state_cities.items():
        print(f"{state}:")
        for city in cities:
            print(f"  - {city}")
        print()

# -------------------- Main Program ------------------------
def main():
    print("=== Intelligent Multi-Stop Route Planner ===")
    display_cities_by_state()

    g = build_city_graph()

    start = input("Enter starting city: ").strip().title()

    # Validate city
    all_cities = [city for cities in {
        "Andhra Pradesh": ["Vijayawada", "Visakhapatnam", "Guntur", "Ongole", "Nellore", "Tirupati", "Chittoor", "Srikakulam"],
        "Telangana": ["Hyderabad", "Warangal", "Karimnagar", "Khammam"],
        "Tamil Nadu": ["Chennai", "Vellore", "Salem", "Coimbatore", "Madurai", "Tirupati"],
        "Kerala": ["Kochi", "Thiruvananthapuram", "Kozhikode"],
        "Karnataka": ["Bangalore", "Mysore", "Mangalore"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
        "Goa": ["Goa", "Belgaum"],
        "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela"],
        "Chhattisgarh": ["Raipur", "Bilaspur", "Jagdalpur"]
    }.values() for city in cities]

    if start not in all_cities:
        print(f"Starting city '{start}' not found in available cities.")
        return

    try:
        num_stops = int(input("How many stops do you want to add? (0 for direct): ").strip())
        if num_stops < 0:
            print("Number of stops cannot be negative.")
            return
    except ValueError:
        print("Invalid input for number of stops.")
        return

    stops = []
    for i in range(num_stops):
        stop = input(f"Enter stop {i+1}: ").strip().title()
        if stop not in all_cities:
            print(f"Stop city '{stop}' not found in available cities.")
            return
        stops.append(stop)

    end = input("Enter final destination city: ").strip().title()
    if end not in all_cities:
        print(f"Destination city '{end}' not found in available cities.")
        return

    full_route = [start] + stops + [end]
    total_cost = 0
    full_path = []

    for i in range(len(full_route)-1):
        segment_path, segment_cost = g.dijkstra(full_route[i], full_route[i+1], combined_modifier)
        if not segment_path:
            print(f"No route found between {full_route[i]} and {full_route[i+1]}.")
            return
        # Avoid repeating intermediate cities
        if i > 0:
            segment_path = segment_path[1:]
        full_path += segment_path
        total_cost += segment_cost

    print(f"\\nOptimal Route: {' -> '.join(full_path)}")
    print(f"Estimated Total Travel Distance (with traffic & weather): {total_cost:.2f} km")

if __name__ == "__main__":
    main()
