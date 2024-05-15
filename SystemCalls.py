import os

# Process related system calls: fork, wait
def process_related_system_calls():
    pid = os.fork()

    if pid == 0:
        # Child process
        print("Child process with PID:", os.getpid())
        os._exit(0)
    else:
        # Parent process
        print("Parent process with PID:", os.getpid())
        os.wait()
        print("Child process finished")


# File related system calls: open, read, write, close
def file_related_system_calls():
    file_name = "test.txt"
    fd = os.open(file_name, os.O_RDWR | os.O_CREAT)

    # Write to file
    os.write(fd, b"Hello, World!\n")

    # Reset file pointer to beginning
    os.lseek(fd, 0, os.SEEK_SET)

    # Read from file
    data = os.read(fd, 100)
    print("Data read from file:", data.decode())

    # Close file
    os.close(fd)


# Protection system call: chmod
def protection_system_call():
    file_name = "test.txt"
    mode = 0o644  # Read/write by owner, read by others
    os.chmod(file_name, mode)
    print("Changed permissions of", file_name, "to", oct(os.stat(file_name).st_mode)[-3:])


if __name__ == "__main__":
    print("Demonstrating process related system calls:")
    process_related_system_calls()

    print("\nDemonstrating file related system calls:")
    file_related_system_calls()

    print("\nDemonstrating protection system call:")
    protection_system_call()
