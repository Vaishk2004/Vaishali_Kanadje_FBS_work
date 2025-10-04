import threading
import time
import random

buffer = []
buffer_size = 5
condition = threading.Condition()

def producer(name):
    global buffer
    while True:
        item = random.randint(1, 100)
        with condition:
            while len(buffer) >= buffer_size:
                condition.wait()  # Wait if buffer is full

            buffer.append(item)
            print(f"Producer {name} produced: {item} | Buffer: {buffer}")
            condition.notifyAll()  # Wake up consumers

        time.sleep(random.uniform(0.5, 1.5))  # Simulate production time

def consumer(name):
    global buffer
    while True:
        with condition:
            while len(buffer) == 0:
                condition.wait()  # Wait if buffer is empty

            item = buffer.pop(0)
            print(f"Consumer {name} consumed: {item} | Buffer: {buffer}")
            condition.notifyAll()  # Wake up producers

        time.sleep(random.uniform(0.5, 1.5))  # Simulate consumption time

if __name__ == "__main__":
    producers = [threading.Thread(target=producer, args=(i,)) for i in range(1, 3)]
    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(1, 3)]

    for p in producers:
        p.start()
    for c in consumers:
        c.start()

    for p in producers:
        p.join()
    for c in consumers:
        c.join()
