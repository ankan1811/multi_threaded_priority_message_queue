# Multi-Threaded Priority Message Queue Implementation

This project implements a multi-threaded priority message queue system where multiple threads can send messages to each other with varying priorities. Additionally, upon receiving a message, the receiving thread performs a simple action using a thread pool.

## Files

### priority_message_queue.py

#### Purpose

Defines the `PriorityMessageQueue` class, representing a priority message queue data structure.

#### Functionality

- Initializes a `PriorityQueue` to store messages with priorities.
- Provides methods to enqueue a message with a specified priority, dequeue the highest priority message, peek at the highest priority message without removing it, and check if the queue is empty.
- Ensures thread safety when accessing the queue using a `Lock`.

### thread_pool.py

#### Purpose

Defines the `ThreadPool` class, representing a thread pool with a fixed number of threads.

#### Functionality

- Initializes a `ThreadPoolExecutor` with a specified number of worker threads.
- Provides a method to submit tasks to the thread pool for asynchronous execution.

### message_functions.py

#### Purpose

Contains utility functions related to sending and processing messages.

#### Functionality

- Defines a `simple_action` function that prints a message.
- Defines a `send_message` function that sends a message with a specified priority from one queue to one or more recipient queues.

### main.py

#### Purpose

Main program file that orchestrates the usage of the other files and modules to demonstrate the functionality of the priority message queue system.

#### Functionality

- Creates multiple instances of `PriorityMessageQueue` to simulate message queues for different threads.
- Creates an instance of `ThreadPool` to manage a fixed number of worker threads.
- Spawns multiple threads, each responsible for receiving messages from a specific message queue and processing them asynchronously using the thread pool.
- Sends messages between threads using the `send_message` function.
- Demonstrates how to run the main logic of the program by calling the `main()` function.

## Usage

To run the program:

1. Ensure all Python files are in the same directory.
2. Run `main.py` using the Python interpreter.

## Data Structures and Algorithms

### Priority Message Queue (priority_message_queue.py)

- Data Structure: Priority queue (implemented using Python's `PriorityQueue` from the `queue` module).
- Algorithms:
  - Enqueue: Inserts a message into the priority queue based on its priority.
  - Dequeue: Removes and returns the highest priority message from the queue.
  - Peek: Returns the highest priority message without removing it from the queue.

### Thread Pool (thread_pool.py)

- Data Structure: ThreadPoolExecutor (from the `concurrent.futures` module).
- Algorithms:
  - Submit Task: Submits tasks to the thread pool for asynchronous execution by worker threads.

```bash
python main.py
```
