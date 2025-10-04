import threading
import time

def print_lowercase():
    for ch in range(ord('a'), ord('z') + 1):
        print(f"Lowercase: {chr(ch)}")
        time.sleep(0.1)  # Slight delay for readability

def print_uppercase():
    for ch in range(ord('A'), ord('Z') + 1):
        print(f"Uppercase: {chr(ch)}")
        time.sleep(0.1)  # Slight delay for readability

if __name__ == "__main__":
    t1 = threading.Thread(target=print_lowercase)
    t2 = threading.Thread(target=print_uppercase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Alphabet printing complete.")
