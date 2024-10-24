class TickCounter():

    def __init__(self):
        self.tick_counter = 0

    def tick(self):
        self.tick_counter += 1
    
    def get_count(self):
        return self.tick_counter
    
    def reset(self):
        self.tick_counter = 0


if __name__ == "__main__":
    counter = TickCounter()
    for _ in range(45):
        counter.tick()
    print("The current count: ", counter.get_count())
    for _ in range(12):
        counter.tick()
    print("The current count: ", counter.get_count())
    counter.reset()
    for _ in range(31):
        counter.tick()
    print("The current count: ", counter.get_count())