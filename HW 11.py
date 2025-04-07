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