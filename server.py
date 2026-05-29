import random

class Server:
    def __init__(self, id):
        self.id = id
        self.current_load = random.randint(10, 30)
        self.history = []

    def handle_request(self):
        self.current_load += random.randint(5, 15)
        self.current_load = min(self.current_load, 100)
        self.history.append(self.current_load)

    def decay(self):
        self.current_load -= random.randint(1, 5)
        self.current_load = max(self.current_load, 0)

    def get_load(self):
        return self.current_load

    def get_history(self):
        return self.history[-20:]
