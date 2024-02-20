import queue
import threading


class PriorityMessageQueue:
    def __init__(self):
        self.queue = queue.PriorityQueue()
        self.lock = threading.Lock()

    def enqueue_message(self, message, priority):
        with self.lock:
            self.queue.put((priority, message))

    def dequeue_message(self):
        with self.lock:
            if not self.queue.empty():
                return self.queue.get()[1]

    def peek_message(self):
        with self.lock:
            if not self.queue.empty():
                return self.queue.queue[0][1]

    def is_empty(self):
        with self.lock:
            return self.queue.empty()
