import threading


current = 1
max_number = 10
condition = threading.Condition()

def print_odd():
    global current
    while current <= max_number:
        with condition:
            while current % 2 == 0:  # Wait for odd turn
                condition.wait()
            print(f"Odd: {current}")
            current += 1
            condition.notify()  # Wake up even thread

def print_even():
    global current
    while current <= max_number:
        with condition:
            while current % 2 != 0:  # Wait for even turn
                condition.wait()
            print(f"Even: {current}")
            current += 1
            condition.notify()  # Wake up odd thread

if __name__ == "__main__":
    t1 = threading.Thread(target=print_odd)
    t2 = threading.Thread(target=print_even)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
