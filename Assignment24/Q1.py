import threading


results = [0, 0, 0, 0]

# Function to calculate sum of squares in a range
def sum_of_squares(start, end, index):
    total = 0
    for i in range(start, end + 1):
        total += i * i
    results[index] = total

if __name__ == "__main__":
    threads = []
    n = 100
    num_threads = 4
    range_size = n // num_threads

    # Create and start threads
    for i in range(num_threads):
        start = i * range_size + 1
        end = (i + 1) * range_size
        t = threading.Thread(target=sum_of_squares, args=(start, end, i))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Combine results
    total_sum_of_squares = sum(results)
    print("Sum of squares from 1 to 100 =", total_sum_of_squares)

