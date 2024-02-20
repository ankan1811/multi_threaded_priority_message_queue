import sys
import threading
from priority_message_queue import PriorityMessageQueue
from thread_pool import ThreadPool
from message_functions import send_message
import time


def simple_action(message):
    print(f"Performed action with message: {message}")


def receive_message(message_queue, thread_pool, thread_id, barrier, finished_flag):
    print(f"Thread {thread_id} started")
    # Wait until all threads have reached this point
    barrier.wait()
    print(f"Thread {thread_id} reached barrier")

    while not finished_flag.is_set():
        message = message_queue.dequeue_message()
        if message:
            print(
                f"Thread {thread_id} - Performed action with message: {message[0]}")
            thread_pool.submit_task(simple_action, message[0])
        time.sleep(1)  # Simulate processing time

    print(f"Thread {thread_id} finished")


def main():
    # Create message queues for each thread
    num_threads = 4
    message_queues = [PriorityMessageQueue() for _ in range(num_threads)]

    # Create a thread pool
    thread_pool = ThreadPool(num_threads)

    # Create barrier for synchronization
    barrier = threading.Barrier(num_threads)

    # Create finished flag
    finished_flag = threading.Event()

    # Create threads for receiving messages
    receive_threads = [threading.Thread(target=receive_message, args=(
        queue, thread_pool, i, barrier, finished_flag), daemon=False) for i, queue in enumerate(message_queues)]
    for thread in receive_threads:
        thread.start()

    # Send some messages
    send_message(message_queues[0], message_queues[1:], "Hello", 2)
    send_message(message_queues[1], message_queues[::2], "Hi", 1)
    send_message(message_queues[2], message_queues[0:2], "Greetings", 3)

    for thread in receive_threads:
        thread.join()

    # Set the finished flag
    finished_flag.set()
    print("Finished flag set")

    # Flush standard output buffer
    sys.stdout.flush()
    print("Output buffer flushed")

    print("All threads have finished. Exiting...")

    # Flush standard output buffer again
    sys.stdout.flush()
    print("Output buffer flushed again")

    # Print active threads after joining
    print("Active threads after joining:")
    for thread in threading.enumerate():
        print(thread)
    print("All threads have finished. Exiting...")


if __name__ == "__main__":
    main()
