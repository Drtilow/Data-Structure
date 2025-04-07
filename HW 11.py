#Task 1

import heapq
from datetime import datetime

class ServerQueue:
    def __init__(self):
        self.priority_queue = []
        self.statistics = []

    def add_request(self, user, priority):
        request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        heapq.heappush(self.priority_queue, (priority, user, request_time))
        self.statistics.append((user, request_time))

    def process_request(self):
        if self.priority_queue:
            priority, user, request_time = heapq.heappop(self.priority_queue)
            print(f"Zpracovávám požadavek od {user} s prioritou {priority} v {request_time}")
        else:
            print("Žádné požadavky k zpracování.")

    def print_statistics(self):
        print("Statistiky požadavků:")
        for user, request_time in self.statistics:
            print(f"Uživatel: {user}, Čas: {request_time}")

# Příklad použití
server_queue = ServerQueue()
server_queue.add_request('Uživatel1', 2)
server_queue.add_request('Uživatel2', 1)
server_queue.add_request('Uživatel3', 3)

server_queue.process_request()
server_queue.process_request()
server_queue.process_request()

server_queue.print_statistics()

#Task 2
import random
import time

class Pier:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_people = 0

    def arrive(self):
        if self.current_people < self.capacity:
            self.current_people += 1
            return True
        return False

    def depart(self, number):
        self.current_people = max(0, self.current_people - number)

def simulate_pier(passenger_interval, boat_interval, boat_capacity, simulation_time):
    pier = Pier(capacity=100)  # Nastavíme kapacitu mola na 100 lidí
    current_time = 0
    passenger_times = []

    while current_time < simulation_time:
        # Příchod pasažérů
        if random.random() < 1.0 / passenger_interval:
            if pier.arrive():
                arrival_time = current_time
                passenger_times.append(arrival_time)

        # Příchod lodí
        if random.random() < 1.0 / boat_interval:
            empty_seats = random.randint(0, boat_capacity)
            pier.depart(empty_seats)
            print(f"Loď připlula s {empty_seats} volnými místy v čase {current_time}")

        current_time += 1
        time.sleep(0.01)  # Simulace času

    # Výpočet průměrného času na molu
    if passenger_times:
        avg_time_on_pier = sum(passenger_times) / len(passenger_times)
    else:
        avg_time_on_pier = 0

    print(f"Průměrný čas na molu: {avg_time_on_pier:.2f} minut")
    print(f"Aktuální počet lidí na molu: {pier.current_people}")

# Příklad použití
simulate_pier(passenger_interval=5, boat_interval=15, boat_capacity=20, simulation_time=100)