"""

Bus Routes :  https://leetcode.com/problems/bus-routes/

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

--- Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

--- Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

"""


from collections import defaultdict, deque
from typing import List


# defaultdict: its like a regular dictionary, but it provides a default value if the key does not exist. 
# In this case, we use it to map bus stops to the buses that stop there.

# deque: This is a double-ended queue, which is more efficient for popping elements from the front (using popleft())
# compared to a regular list. You use it to perform a breadth-first search (BFS) in the code.


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        print(f"Input routes: {routes}, source: {source}, target: {target}")
        
        if source == target:
            print("Source is the same as target. Returning 0.")
            return 0
        
        # Step 2: Create stop_to_buses mapping

        stop_to_buses = defaultdict(list)  """ This creates a dictionary where every new key (bus stop) is automatically assigned an empty list as its value if it doesn’t already exist. If you access a key that isn’t in the dictionary yet, instead of getting an error, you’ll get an empty list. """

        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus)
        print(f"stop_to_buses: {dict(stop_to_buses)}")
        

        # Step 3: Initialize BFS queue and visited sets

        queue = deque([source])
        visited_stops = set([source])
        visited_buses = set()
        buses_taken = 0
        print(f"Starting BFS with queue: {list(queue)}, visited_stops: {visited_stops}")
        
        # Step 4: BFS Loop
        while queue:
            buses_taken += 1
            print(f"\nBuses taken so far: {buses_taken}")
            for _ in range(len(queue)):
                current_stop = queue.popleft()
                print(f"Exploring stop: {current_stop}")
                
                # Step 5: Check buses from stop 1

                for bus in stop_to_buses[current_stop]:
                    if bus in visited_buses:
                        continue
                    
                    # Step 6: Second iteration of BFS Loop

                    visited_buses.add(bus)
                    print(f"Taking bus {bus}, visiting stops: {routes[bus]}")
                    for next_stop in routes[bus]:
                        if next_stop == target:
                            print(f"Found target {target} at stop {next_stop} with {buses_taken} buses.")
                            return buses_taken
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append(next_stop)
                            print(f"Adding stop {next_stop} to queue. Queue is now {list(queue)}")

        print("Target not reachable.")
        return -1

if __name__ == "__main__":
    solution = Solution()
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6
    result = solution.numBusesToDestination(routes, source, target)
    print(f"Result: {result}")

"""
input: 
routes = [[1, 2, 7], [3, 6, 7]]
source = 1
target = 6

output: 2 
"""