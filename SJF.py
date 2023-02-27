# Funkcja sprawdza czy w danym momencie przychodza jakieś procesy jesli tak wrzuca je do kolejki
def queue_add(counter_low, counter_high, q, data_arrray):
    for i in data_arrray:
        for x in range(counter_low, counter_high):
            if i[1] == x:
                q.append(i[0])
                q.append(i[1])
                q.append(i[2])
    return q


# funkcja obliczajaca czas spedzony w kolejce danego procesu oraz zapisuje dane procesów do odpowiednich list aby
# wszystkie dane były w tej samej kolejności, usuwa z kolejki proces który już rozpatrzyliśmy
# zwraca czas spędzony na procesowaniu aby dodać go do licznika czasu
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


# Inicjalizujemy zmienne globalne
time_spent_in_queue = []
processes_list = []
list_of_processing_times = []
list_of_arrival_time = []


def sjf_main(data_array, number_of_items):
    time_counter = 0
    queue_of_processes_and_their_times = []
    time_for_while_loop_to_end = 0
    counter_min = 0
    index_of_lowest_processing_time = 0
    sum_of_time_spent_in_queue = 0
    while time_for_while_loop_to_end < number_of_items:

        # Dodajemy procesy do kolejki
        queue_of_processes_and_their_times = queue_add(counter_min, time_counter,
                                                       queue_of_processes_and_their_times, data_array)

        # ustalamy wartosc licznika przed dodaniem czasu trwania procesu ponieważ do funkcji doodawania procesow
        # do kolejki potrzebne nam sa obie wartosci
        counter_min = time_counter

        try:
            # Ustalamy najniższy czas na nieskończoność
            lowest_processing_time = float("inf")
            # Przechodzimy przez kolejkę procesów i sprawdzamy który
            # ma najkrótszy czas wykonywania pobieramy indeks tego
            # procesu, wywołujemy funkcje do obliczania czasu spędzonego w kolejce i usuwania tego procesu z kolejki
            # Inkrementujemy czas do którego pętla ma się skończyć bo będą wykonane wszystkie procesy
            for j in range(0, len(queue_of_processes_and_their_times), 3):
                if lowest_processing_time > queue_of_processes_and_their_times[j+2]:
                    lowest_processing_time = queue_of_processes_and_their_times[j+2]
                    index_of_lowest_processing_time = j
            time_counter += calculate_time_spent_in_queue(time_counter, queue_of_processes_and_their_times,
                                                          index_of_lowest_processing_time)
            time_for_while_loop_to_end += 1
        except IndexError:
            pass

        # Zwiększamy licznik czasu
        time_counter += 1

    # Obliczamy ile proces średnio czasu spędza w kolejce
    for element in time_spent_in_queue:
        sum_of_time_spent_in_queue += element

    average_time_spent_in_queue = sum_of_time_spent_in_queue/len(time_spent_in_queue)

    # Formatujemy dane aby łatwiej je było wpisać do tabelek
    data_for_storing = [[0] * 4 for i in range(len(list_of_arrival_time))]

    for index in range(len(data_for_storing)):
        processes_list[index] = str(int(processes_list[index]))
        data_for_storing[index][0] = "P" + processes_list[index]
        data_for_storing[index][1] = list_of_arrival_time[index]
        data_for_storing[index][2] = list_of_processing_times[index]
        data_for_storing[index][3] = time_spent_in_queue[index]

    return average_time_spent_in_queue, data_for_storing
