import itertools
import threading
import time
import sys

# Function to display a loading indicator
def loading_indicator(stop_event):
    spinner = itertools.cycle(['-', '/', '|', '*'])
    while not stop_event.is_set():
        sys.stdout.write(f"\rLoading {next(spinner)}")
        sys.stdout.flush()
        time.sleep(0.1)

# Function to print content while the loading indicator runs
def print_content():
    print("\nStarting long task...")
    time.sleep(3)  # Simulating a long task
    print("Task step 1 completed.")
    time.sleep(2)
    print("Task step 2 completed.")
    time.sleep(2)
    print("All tasks completed.")

# Main program
if __name__ == "__main__":
    stop_event = threading.Event()  # Event to stop the loading indicator

    # Start the loading indicator in a separate thread
    loading_thread = threading.Thread(target=loading_indicator, args=(stop_event,))
    loading_thread.start()

    # Perform the task (while the loading indicator is running)
    print_content()

    # Signal the loading indicator to stop
    stop_event.set()

    # Wait for the loading indicator to finish
    loading_thread.join()

    print("\nDone!")
