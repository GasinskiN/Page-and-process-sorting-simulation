# Function checks if there are any processes coming at this time and if so it adds them to the queue
def queue_add(counter_low, counter_high, q, data_array):
    for i in data_array:
        for x in range(counter_low, counter_high):
            if i[1] == x:
                q.append(i[0])
                q.append(i[1])
                q.append(i[2])
    return q


# function calculates the time spent in queue by a process, saves all the data to appropriate lists, so they
# are all in the same order. Deletes the processes that we have already finished processing from the queue.
# It returns time spent on processing.
def calculate_time_spent_in_queue(counter, queue_of_processes_and_their_times, index_of_lowest_processing_time):
    processes_list.append(queue_of_processes_and_their_times[index_of_lowest_processing_time])
    list_of_arrival_time.append(queue_of_processes_and_their_times[index_of_lowest_processing_time + 1])
    list_of_processing_times.append(queue_of_processes_and_their_times[index_of_lowest_processing_time + 2])
    time_spent_in_queue.append(counter - queue_of_processes_and_their_times[index_of_lowest_processing_time + 1] - 1)
    time_spent_on_processing = queue_of_processes_and_their_times[index_of_lowest_processing_time + 2]
    time_spent_on_processing = int(time_spent_on_processing)
    for z in range(3):
        del queue_of_processes_and_their_times[index_of_lowest_processing_time]
    return time_spent_on_processing


time_spent_in_queue = []
processes_list = []
list_of_processing_times = []
list_of_arrival_time = []


# Basically our main loop
def sjf_main(data_array, number_of_items):
    time_counter = 0
    queue_of_processes_and_their_times = []
    time_for_while_loop_to_end = 0
    counter_min = 0
    index_of_lowest_processing_time = 0
    sum_of_time_spent_in_queue = 0
    while time_for_while_loop_to_end < number_of_items:

        # Add processes to the queue
        queue_of_processes_and_their_times = queue_add(counter_min, time_counter,
                                                       queue_of_processes_and_their_times, data_array)

        # Keeping track of time before adding the duration of the process because we need to iterate over the
        # time in order to sort the coming processes appropriately
        counter_min = time_counter

        try:
            # Set lowest time to the highest possible number
            lowest_processing_time = float("inf")
            # Get index of a process with the lowest processing time from the queue,
            # then we calculate time spent in queue, we get rid of that process from the queue and
            # increment the time for the while loop to end
            for j in range(0, len(queue_of_processes_and_their_times), 3):
                if lowest_processing_time > queue_of_processes_and_their_times[j+2]:
                    lowest_processing_time = queue_of_processes_and_their_times[j+2]
                    index_of_lowest_processing_time = j
            time_counter += calculate_time_spent_in_queue(time_counter, queue_of_processes_and_their_times,
                                                          index_of_lowest_processing_time)
            time_for_while_loop_to_end += 1
        except IndexError:
            pass
        time_counter += 1

    # Calculate average time spent in queue
    for element in time_spent_in_queue:
        sum_of_time_spent_in_queue += element

    average_time_spent_in_queue = sum_of_time_spent_in_queue/len(time_spent_in_queue)

    # Format the data for easier processing
    data_for_storing = [[0] * 4 for i in range(len(list_of_arrival_time))]

    for index in range(len(data_for_storing)):
        processes_list[index] = str(int(processes_list[index]))
        data_for_storing[index][0] = "P" + processes_list[index]
        data_for_storing[index][1] = list_of_arrival_time[index]
        data_for_storing[index][2] = list_of_processing_times[index]
        data_for_storing[index][3] = time_spent_in_queue[index]

    return average_time_spent_in_queue, data_for_storing
