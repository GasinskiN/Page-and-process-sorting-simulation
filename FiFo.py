# Importujemy wszystkie potrzebny modul
from queue import Queue


# Funkcja sprawdza czy w danym momencie przychodza jakieś procesy jeśli przychodza dodaje je do kolejki
def queue_add(counter, q, data_array):
    for i in data_array:
        if i[1] == counter:
            q.append(i[0])
            q.append(i[1])
    return q


# funkcja  tworzy 2 listy czasu przychodzenia i stron
# przydadzą one się podczas zapisywania wyników
def make_lists_of_arrival_page_times(queue_of_pages_and_their_times, index_for_queue):
    pages_list.append(int(queue_of_pages_and_their_times[index_for_queue]))
    pages_arrival_time.append(int(queue_of_pages_and_their_times[index_for_queue+1]))
    return


# inicjalizujemy zmienne globalne
pages_list = []
pages_arrival_time = []
queue_to_remove = Queue()
capacity = 4
set_of_current_pages = set()


def fifo_main(data, number_of_items):
    index_for_queue = 0
    time_counter = 0
    queue_of_pages_and_their_times = []
    page_faults = 0
    # Iterujemy przez funkcje 2 razy wiecej razy niz mamy stron ponieważ trzymam
    # rzeczy w jedej liscie i inkrementuje co 2
    while index_for_queue < number_of_items * 2:
        # Wywołujemy funkcje dodawania do kolejki
        queue_of_pages_and_their_times = queue_add(time_counter, queue_of_pages_and_their_times, data)

        # Sprawdzamy czy nasz set jest pelny
        if len(set_of_current_pages) < capacity:
            # Jesli nie  to sprawdzamy czy dana strona jest w naszym secie jesli nie,
            # to dodajemy do setu strone, wywolujemy
            # funkcje obliczania czasu spędzonego w kolejce oraz dodajemy do kolejki do usuniecia dodana strone.
            # Inkrementujemy nasz indeks do kolejki oraz page_faults
            try:
                if int(queue_of_pages_and_their_times[index_for_queue]) not in set_of_current_pages:
                    set_of_current_pages.add(queue_of_pages_and_their_times[index_for_queue])
                    queue_to_remove.put(queue_of_pages_and_their_times[index_for_queue])
                    page_faults += 1
                    # Jeśli strony nie ma w naszym secie to tylko obliczamy
                    # czas spedzony w kolejce i inkrementujemy index do kolejki
                make_lists_of_arrival_page_times(queue_of_pages_and_their_times, index_for_queue)
                index_for_queue += 2
            except IndexError:
                pass
            # Set jest pelny
        else:
            # Sprawdzamy czy dana strona jest w naszym secie jesli nie, pobieramy wartość z kolejki do usuniecia,
            # funkcja get przy okazji usuwa tą wartość usuwamy z naszego setu tą wartość dodajemy nowa obliczamy czas
            # spedzony w kolejce dodajemy do kolejki do usuniecia wartość dodaną do setu
            # Na końcu inkrementujemy indeks i page faults
            try:
                if int(queue_of_pages_and_their_times[index_for_queue]) not in set_of_current_pages:
                    temp = queue_to_remove.get()
                    set_of_current_pages.remove(temp)
                    set_of_current_pages.add(queue_of_pages_and_their_times[index_for_queue])
                    queue_to_remove.put(queue_of_pages_and_their_times[index_for_queue])
                    page_faults += 1

                make_lists_of_arrival_page_times(queue_of_pages_and_their_times, index_for_queue)
                index_for_queue += 2
            except IndexError:
                pass

        # inkrementujemy licznik czasu po przejsciu naszej pętli jest to nasza jednostka czasu
        time_counter += 1

    return page_faults
