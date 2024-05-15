from tabulate import tabulate

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0


def fcfs(processes):
    current_time = 0
    total_waiting_time = 0
    for process in processes:
        process.waiting_time = max(0, current_time - process.arrival_time)
        total_waiting_time += process.waiting_time
        process.start_time = max(current_time, process.arrival_time)
        current_time = process.start_time + process.burst_time
        process.completion_time = current_time
        process.turnaround_time = process.completion_time - process.arrival_time

    return total_waiting_time / len(processes), processes


def sjf(processes):
    processes.sort(key=lambda x: x.burst_time)
    return fcfs(processes)


def priority_scheduling(processes):
    processes.sort(key=lambda x: x.priority)
    return fcfs(processes)


def round_robin(processes, time_quantum):
    current_time = 0
    total_waiting_time = 0
    queue = processes.copy()
    while queue:
        current_process = queue.pop(0)
        if current_process.burst_time > time_quantum:
            current_process.waiting_time += max(0, current_time - current_process.arrival_time)
            total_waiting_time += current_process.waiting_time
            current_time += time_quantum
            current_process.burst_time -= time_quantum
            queue.append(current_process)
        else:
            current_process.waiting_time += max(0, current_time - current_process.arrival_time)
            total_waiting_time += current_process.waiting_time
            current_time += current_process.burst_time
            current_process.completion_time = current_time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time

    return total_waiting_time / len(processes), processes


def display_results(processes, print_arrival=False, print_priority=False):
    headers = ["Process", "Burst Time", "Waiting Time", "Turnaround Time"]
    if print_arrival:
        headers.insert(1, "Arrival Time")
    if print_priority:
        headers.insert(2, "Priority")
    
    table = []
    for process in processes:
        row = [process.pid, process.burst_time, process.waiting_time, process.turnaround_time]
        if print_arrival:
            row.insert(1, process.arrival_time)
        if print_priority:
            row.insert(2, process.priority)
        table.append(row)
    print(tabulate(table, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))

    processes = []
    for i in range(num_processes):
        pid = i + 1
        arrival_time = int(input("Enter arrival time for process {}: ".format(pid)))
        burst_time = int(input("Enter burst time for process {}: ".format(pid)))
        priority = int(input("Enter priority for process {}: ".format(pid)))
        processes.append(Process(pid, arrival_time, burst_time, priority))

    print("\nFirst Come First Serve (FCFS):")
    avg_fcfs, fcfs_processes = fcfs(processes.copy())
    display_results(fcfs_processes, print_arrival=True)
    print("Average Waiting Time (FCFS):", avg_fcfs)

    print("\nShortest Job First (SJF):")
    avg_sjf, sjf_processes = sjf(processes.copy())
    display_results(sjf_processes)
    print("Average Waiting Time (SJF):", avg_sjf)

    print("\nPriority Scheduling:")
    avg_priority, priority_processes = priority_scheduling(processes.copy())
    display_results(priority_processes, print_priority=True)
    print("Average Waiting Time (Priority Scheduling):", avg_priority)

    print("\nRound Robin Scheduling:")
    time_quantum = int(input("Enter time quantum for Round Robin Scheduling: "))
    avg_round_robin, rr_processes = round_robin(processes.copy(), time_quantum)
    display_results(rr_processes, print_arrival=True)
    print("Average Waiting Time (Round Robin Scheduling):", avg_round_robin)
