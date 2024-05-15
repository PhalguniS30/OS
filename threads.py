import threading

mutex = threading.Lock()
count_mutex = threading.Lock()

def reader(num, filename, barrier):
    with count_mutex:
        print(f"Reader {num} is waiting...")
    barrier.wait()
    with mutex:
        with open(filename, 'r') as file:
            data = file.read()
        print(f"Reader {num} acquired lock, reading data: {data.strip()}")

def writer(num, filename, barrier):
    with mutex:
        print(f"Writer {num} is waiting...")
    barrier.wait()
    with mutex:
        with open(filename, 'a') as file:
            file.write(f"\nHello written by writer {num}")
        print(f"Writer {num} acquired lock and wrote to file")

def main():
    filename = "sample.txt"
    reader_threads = []
    writer_threads = []

    
    open(filename, 'w').close()

    barrier = threading.Barrier(5)  

    for i in range(5):
        writer_threads.append(threading.Thread(target=writer, args=(i, filename, barrier)))
        reader_threads.append(threading.Thread(target=reader, args=(i, filename, barrier)))

    for thread in writer_threads + reader_threads:
        thread.start()

    for thread in writer_threads + reader_threads:
        thread.join()

if __name__ == "__main__":
    main()