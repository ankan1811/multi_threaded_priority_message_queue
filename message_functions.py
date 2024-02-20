def simple_action(message):
    print("Performed action with message:", message)


def send_message(sender_queue, receiver_queues, message, priority):
    sender_queue.enqueue_message((message, priority), priority)
    for queue in receiver_queues:
        queue.enqueue_message((message, priority), priority)
