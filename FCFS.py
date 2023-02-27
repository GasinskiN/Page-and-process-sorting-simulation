# Funkcja sprawdza czy w danym momencie przychodza jakieś procesy jesli tak wrzuca je do kolejki
def queue_add(counter_low, counter_high, q, data_array):
    for x in range(counter_low, counter_high):
        for i in data_array:
            if i[1] == x:
                q.append(i[0])
                q.append(i[1])
                q.append(i[2])
    return q


# funkcja obliczajaca czas spedzony w kolejce danego procesu oraz zapisuje dane procesów do odpowiednich list aby
# wszystkie dane były w tej samej kolejności zwraca czas spędzony na procesowaniu aby dodać go do licznika czasu
def calculate_time_spent_in_queue(counter, queue_of_processes_and_their_times, index_for_queue):
    processes_list.append(queue_of_processes_and_their_times[index_for_queue])
    list_of_arrival_time.append(queue_of_processes_and_their_times[index_for_queue + 1])
    list_of_processing_times.append(queue_of_processes_and_their_times[index_for_queue + 2])
    time_spent_in_queue.append(counter - queue_of_processes_and_their_times[index_for_queue + 1] - 1)
    time_spent_on_processing = int(queue_of_processes_and_their_times[index_for_queue + 2])
    return time_spent_on_processing


# Inicjalizujemy globalne zmienne
time_spent_in_queue = []
processes_list = []
list_of_processing_times = []
list_of_arrival_time = []


def fcfs_main(data, number_of_items):
    # inicjalizacja zmiennych
    index_for_queue = 0
    time_counter = 0
    counter_min = 0
    queue_of_processes_and_their_times = []
    sum_of_time_spent_in_queue = 0
    while index_for_queue < number_of_items * 3:

        # Dodajemy procesy do kolejki
        queue_of_processes_and_their_times = queue_add(counter_min, time_counter,
                                                       queue_of_processes_and_their_times, data)

        # ustalamy wartosc licznika przed dodaniem czasu trwania procesu ponieważ do funkcji doodawania procesow
        # do kolejki potrzebne nam sa obie wartosci
        counter_min = time_counter
        # Obliczamy ile czasu dany proces spędził w kolejce i iterujemy indeks dla kolejki
        try:
            time_counter += calculate_time_spent_in_queue(time_counter, queue_of_processes_and_their_times,
                                                          index_for_queue)
            index_for_queue += 3
        except IndexError:
            pass

        # Zwiększamy licznik czasu
        time_counter += 1

    # Obliczamy ile proces średnio czasu spędza w kolejce
    for element in time_spent_in_queue:
        sum_of_time_spent_in_queue += element

    average_time_spent_in_queue = sum_of_time_spent_in_queue / len(time_spent_in_queue)

    # Formatujemy dane aby łatwiej je było wpisać do tabelek
    data_for_storing = [[0] * 4 for i in range(len(list_of_arrival_time))]

    for index in range(len(data_for_storing)):
        processes_list[index] = str(int(processes_list[index]))
        data_for_storing[index][0] = "P" + processes_list[index]
        data_for_storing[index][1] = list_of_arrival_time[index]
        data_for_storing[index][2] = list_of_processing_times[index]
        data_for_storing[index][3] = time_spent_in_queue[index]

    return average_time_spent_in_queue, data_for_storing
