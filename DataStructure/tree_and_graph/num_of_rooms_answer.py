from collections import defaultdict

def solution(arrows):
    direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    curr_loc = (0, 0)
    visited_nodes = set([curr_loc])
    visited_edges = set()
    rooms = 0

    for arrow in arrows:
        x, y = direction[arrow]
        for _ in range(2):  # Move twice to handle diagonal steps
            next_loc = (curr_loc[0] + x, curr_loc[1] + y)
            if next_loc in visited_nodes:
                if (curr_loc, next_loc) not in visited_edges:
                    rooms += 1
            visited_nodes.add(next_loc)
            visited_edges.add((curr_loc, next_loc))
            visited_edges.add((next_loc, curr_loc))
            curr_loc = next_loc
    print(visited_nodes)
    print("nodes", len(list(visited_nodes)))

    return rooms

if __name__ == "__main__":
    arrows_input = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
    print("edges", len(arrows_input))
    print(solution(arrows_input))  # Output should be the number of rooms formed

