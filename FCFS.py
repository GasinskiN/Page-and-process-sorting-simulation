# Function checks if there are any processes coming at this time and if so it adds them to the queue
def queue_add(counter_low, counter_high, q, data_array):
    for x in range(counter_low, counter_high):
        for i in data_array:
            if i[1] == x:
                q.append(i[0])
                q.append(i[1])
                q.append(i[2])
    return q


# function calculates the time spent in queue by a process, saves all the data to appropriate lists, so they
# are all in the same order. It returns time spent on processing.
def calculate_time_spent_in_queue(counter, queue_of_processes_and_their_times, index_for_queue):
    processes_list.append(queue_of_processes_and_their_times[index_for_queue])
    list_of_arrival_time.append(queue_of_processes_and_their_times[index_for_queue + 1])
    list_of_processing_times.append(queue_of_processes_and_their_times[index_for_queue + 2])
    time_spent_in_queue.append(counter - queue_of_processes_and_their_times[index_for_queue + 1] - 1)
    time_spent_on_processing = int(queue_of_processes_and_their_times[index_for_queue + 2])
    return time_spent_on_processing


time_spent_in_queue = []
processes_list = []
list_of_processing_times = []
list_of_arrival_time = []


# Basically our main loop, returns average time spent in queue and an array with data for storing
def fcfs_main(data, number_of_items):
    index_for_queue = 0
    time_counter = 0
    counter_min = 0
    queue_of_processes_and_their_times = []
    sum_of_time_spent_in_queue = 0
    while index_for_queue < number_of_items * 3:

        # Add processes to queue
        queue_of_processes_and_their_times = queue_add(counter_min, time_counter,
                                                       queue_of_processes_and_their_times, data)

        # Keeping track of time before adding the duration of the process because we need to iterate over the
        # time in order to sort the coming processes appropriately
        counter_min = time_counter
        # Calculate time spent in queue and iterate index for our queue
        try:
            time_counter += calculate_time_spent_in_queue(time_counter, queue_of_processes_and_their_times,
                                                          index_for_queue)
            index_for_queue += 3
        except IndexError:
            pass
        time_counter += 1

    # Calculate average time spent in queue
    for element in time_spent_in_queue:
        sum_of_time_spent_in_queue += element

    average_time_spent_in_queue = sum_of_time_spent_in_queue / len(time_spent_in_queue)

    # Format the data for easier handling
    data_for_storing = [[0] * 4 for i in range(len(list_of_arrival_time))]

    for index in range(len(data_for_storing)):
        processes_list[index] = str(int(processes_list[index]))
        data_for_storing[index][0] = "P" + processes_list[index]
        data_for_storing[index][1] = list_of_arrival_time[index]
        data_for_storing[index][2] = list_of_processing_times[index]
        data_for_storing[index][3] = time_spent_in_queue[index]

    return average_time_spent_in_queue, data_for_storing
