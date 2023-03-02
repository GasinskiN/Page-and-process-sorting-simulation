# Function checks if there are any processes coming at this time and if so it adds them to the queue
def queue_add(counter, q, data_array):
    for i in data_array:
        if i[1] == counter:
            q.append(i[0])
            q.append(i[1])
    return q


capacity = 4


# Main function
def lru_main(data, number_of_items):

    index_for_queue = 0
    time_counter = 0
    queue_of_pages_and_their_times = []
    temp = -1
    page_faults = 0
    set_of_current_pages = set()
    indexes = {}

    # Increment by 2 times number of items because the data is held in one array
    while index_for_queue < number_of_items * 2:

        queue_of_pages_and_their_times = queue_add(time_counter, queue_of_pages_and_their_times, data)

        # Check if the set is full
        if len(set_of_current_pages) < capacity:
            try:
                # check if the current page is in the set if so add it then increment page faults
                if int(queue_of_pages_and_their_times[index_for_queue]) not in set_of_current_pages:
                    set_of_current_pages.add(queue_of_pages_and_their_times[index_for_queue])
                    page_faults += 1
                # To the indexes list which will be used when deleting pages from current set: as a key the current
                # page is used and for value the index value is used, so it is known how old that page is.
                indexes[queue_of_pages_and_their_times[index_for_queue]] = index_for_queue
                index_for_queue += 2
            except IndexError:
                pass
        else:
            try:
                # check if the current page is in set if not set lru to maximum after that iterate through every page
                # in our set and check which one was used least recently assign its value to a temporary variable, then
                # delete the least recently used value from the set and add the one from the queue, lastly calculate
                # time spent in queue
                if int(queue_of_pages_and_their_times[index_for_queue]) not in set_of_current_pages:
                    lru = float("inf")
                    for page in set_of_current_pages:
                        if indexes[int(page)] < lru:
                            lru = indexes[int(page)]
                            temp = page

                    set_of_current_pages.remove(temp)
                    set_of_current_pages.add(queue_of_pages_and_their_times[index_for_queue])
                    page_faults += 1

                # For explanation go to line 36
                indexes[queue_of_pages_and_their_times[index_for_queue]] = index_for_queue
                index_for_queue += 2
            except IndexError:
                pass
        time_counter += 1

    return page_faults
