import threading
import time
import queue

CAPACITY = 5
max_items=10
lock = threading.Lock()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)

queue_buffer = queue.Queue(CAPACITY)

class Producer(threading.Thread):
    def run(self):
        global CAPACITY

        items_produced = 0
        counter = 0

        while items_produced < max_items:
            empty.acquire()

            counter += 1
            with lock:
                queue_buffer.put(counter)
                print("\nProducer produced:", counter)
                print("Current buffer:", list(queue_buffer.queue))

            full.release()

            time.sleep(1)

            items_produced += 1

class Consumer(threading.Thread):
    def run(self):
        global CAPACITY

        items_consumed = 0

        while items_consumed < max_items:
            full.acquire()

            with lock:
                item = queue_buffer.get()
                print("\nConsumer consumed item:", item)
                print("Current buffer:", list(queue_buffer.queue))

            empty.release()

            time.sleep(2.5)

            items_consumed += 1

# Creating Threads
producer = Producer()
consumer = Consumer()

# Starting Threads
consumer.start()
producer.start()

producer.join()
consumer.join()
