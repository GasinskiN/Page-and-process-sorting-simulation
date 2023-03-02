from queue import Queue


# Function checks if there are any processes coming at this time and if so it adds them to the queue
def queue_add(counter, q, data_array):
    for i in data_array:
        if i[1] == counter:
            q.append(i[0])
            q.append(i[1])
    return q


queue_to_remove = Queue()
capacity = 4
set_of_current_pages = set()


def fifo_main(data, number_of_items):
    index_for_queue = 0
    time_counter = 0
    queue_of_pages_and_their_times = []
    page_faults = 0
    # Increment by 2 times number of items because the data is held in one array
    while index_for_queue < number_of_items * 2:
        queue_of_pages_and_their_times = queue_add(time_counter, queue_of_pages_and_their_times, data)

        # Check if the set is full
        if len(set_of_current_pages) < capacity:
            # check if the current page is not in the set if so add it then increment page faults, add said page to
            # the queue to remove lastly increment index for queue
            try:
                if int(queue_of_pages_and_their_times[index_for_queue]) not in set_of_current_pages:
                    set_of_current_pages.add(queue_of_pages_and_their_times[index_for_queue])
                    queue_to_remove.put(queue_of_pages_and_their_times[index_for_queue])
                    page_faults += 1
                index_for_queue += 2
            except IndexError:
                pass
        else:
            # Check if current page is not in our set if so get the page to remove from set, remove it, add the waiting
            # page to set and to queue to remove
            try:
                if int(queue_of_pages_and_their_times[index_for_queue]) not in set_of_current_pages:
                    temp = queue_to_remove.get()
                    set_of_current_pages.remove(temp)
                    set_of_current_pages.add(queue_of_pages_and_their_times[index_for_queue])
                    queue_to_remove.put(queue_of_pages_and_their_times[index_for_queue])
                    page_faults += 1

                index_for_queue += 2
            except IndexError:
                pass

        time_counter += 1

    return page_faults
