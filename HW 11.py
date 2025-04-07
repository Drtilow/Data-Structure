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

#Task 3
class DictionaryApp:
    def __init__(self):
        self.dictionary = {}
        self.request_counter = {}

    def add_word(self, word, translation):
        self.dictionary[word] = translation
        self.request_counter[word] = 0

    def replace_word(self, old_word, new_word, translation):
        if old_word in self.dictionary:
            del self.dictionary[old_word]
            del self.request_counter[old_word]
        self.dictionary[new_word] = translation
        self.request_counter[new_word] = 0

    def delete_word(self, word):
        if word in self.dictionary:
            del self.dictionary[word]
            del self.request_counter[word]

    def add_translation(self, word, translation):
        if word in self.dictionary:
            self.dictionary[word] = translation

    def replace_translation(self, word, translation):
        self.add_translation(word, translation)

    def delete_translation(self, word):
        if word in self.dictionary:
            self.dictionary[word] = None

    def display_word(self, word):
        if word in self.dictionary:
            self.request_counter[word] += 1
            print(f"{word}: {self.dictionary[word]}")
        else:
            print(f"{word} not found in dictionary.")

    def display_top_words(self, top_n=10, least=False):
        sorted_words = sorted(self.request_counter.items(), key=lambda x: x[1], reverse=not least)
        for word, count in sorted_words[:top_n]:
            print(f"{word}: {count} requests")

# Example usage
app = DictionaryApp()
app.add_word('hello', 'hola')
app.add_word('world', 'mundo')
app.add_word('goodbye', 'adiós')

app.display_word('hello')
app.display_word('world')
app.display_word('goodbye')
app.display_word('hello')

app.replace_word('goodbye', 'farewell', 'adiós')
app.display_word('farewell')

app.delete_word('world')

app.display_top_words()
app.display_top_words(least=True)

#Task 4
class TaxOfficeDatabase:
    def __init__(self):
        self.database = {}

    def add_person(self, id_code, name, city):
        self.database[id_code] = {'name': name, 'city': city, 'penalties': []}

    def add_penalty(self, id_code, penalty_type, amount):
        if id_code in self.database:
            self.database[id_code]['penalties'].append({'type': penalty_type, 'amount': amount})

    def delete_penalty(self, id_code, penalty_type):
        if id_code in self.database:
            self.database[id_code]['penalties'] = [p for p in self.database[id_code]['penalties'] if p['type'] != penalty_type]

    def replace_person_info(self, id_code, name, city):
        if id_code in self.database:
            self.database[id_code]['name'] = name
            self.database[id_code]['city'] = city

    def full_hard_copy(self):
        for id_code, info in self.database.items():
            print(f"ID: {id_code}, Name: {info['name']}, City: {info['city']}, Penalties: {info['penalties']}")

    def hard_copy_by_code(self, id_code):
        if id_code in self.database:
            info = self.database[id_code]
            print(f"ID: {id_code}, Name: {info['name']}, City: {info['city']}, Penalties: {info['penalties']}")

    def hard_copy_by_penalty_type(self, penalty_type):
        for id_code, info in self.database.items():
            penalties = [p for p in info['penalties'] if p['type'] == penalty_type]
            if penalties:
                print(f"ID: {id_code}, Name: {info['name']}, City: {info['city']}, Penalties: {penalties}")

    def hard_copy_by_city(self, city):
        for id_code, info in self.database.items():
            if info['city'] == city:
                print(f"ID: {id_code}, Name: {info['name']}, City: {info['city']}, Penalties: {info['penalties']}")

# Příklad použití
db = TaxOfficeDatabase()
db.add_person('123', 'Alice', 'Prague')
db.add_person('456', 'Bob', 'Brno')
db.add_penalty('123', 'Late Payment', 100)
db.add_penalty('123', 'Tax Evasion', 500)
db.add_penalty('456', 'Late Payment', 150)

db.full_hard_copy()
db.hard_copy_by_code('123')
db.hard_copy_by_penalty_type('Late Payment')
db.hard_copy_by_city('Prague')

db.replace_person_info('123', 'Alice Smith', 'Prague')
db.delete_penalty('123', 'Tax Evasion')

db.full_hard_copy()
