# Funkcja sprawdza czy w danym momencie przychodza jakieś procesy jeśli przychodza dodaje je do kolejki
def queue_add(counter, q, data_array):
    for i in data_array:
        if i[1] == counter:
            q.append(i[0])
            q.append(i[1])
    return q


# funkcja  tworzy 2 listy czasu przychodzenia i stron
# przydadzą one się podczas zapisywania wyników
def make_page_and_arrival_time_list(queue_of_pages_and_their_times, index_for_queue):
    pages_list.append(int(queue_of_pages_and_their_times[index_for_queue]))
    pages_arrival_time.append(int(queue_of_pages_and_their_times[index_for_queue+1]))
    return


# inicjalizujemy zmienne globalne
pages_arrival_time = []
pages_list = []
capacity = 4


def lru_main(data, number_of_items):
    # inicjalizacja zmiennych
    index_for_queue = 0
    time_counter = 0
    queue_of_pages_and_their_times = []
    temp = -1
    page_faults = 0
    set_of_current_pages = set()
    indexes = {}
    # Iterujemy przez funkcje 2 razy wiecej razy niz mamy stron
    # ponieważ trzymam rzeczy w jedej liscie i inkrementuje co 2
    while index_for_queue < number_of_items * 2:
        # Wywołujemy funkcje dodawania do kolejki
        queue_of_pages_and_their_times = queue_add(time_counter, queue_of_pages_and_their_times, data)

        # Sprawdzamy czy nasz set jest pelny
        if len(set_of_current_pages) < capacity:
            try:
                # Sprawdzamy czy aktualna strona jest w naszym secie jeśli nie dodajmy ją
                # na końcu inkrementujemy page faults
                if int(queue_of_pages_and_their_times[index_for_queue]) not in set_of_current_pages:
                    set_of_current_pages.add(queue_of_pages_and_their_times[index_for_queue])
                    page_faults += 1
                make_page_and_arrival_time_list(queue_of_pages_and_their_times, index_for_queue)
                # Do indexów z których będziemy korzystać przy usuwaniu
                # jako klucz w słowniku wpisujemy stronę a jako wartość
                # dla tego klucza przypisujemy index_for_queue jest to tak jakby czas iteracji
                # im mniejszy indeks tym dawniej temu była ta strona wykorzystana
                # na końcu iterujemy index_for_queue
                indexes[queue_of_pages_and_their_times[index_for_queue]] = index_for_queue
                index_for_queue += 2
            except IndexError:
                pass
        # set nie jest pełny
        else:
            try:
                # Sprawdzamy czy aktualna strona jest w naszym secie jeśli nie ustalamy wartosc lru na maksimum po
                # czym iterujemy się przez każdą stronę w naszym secie i
                # sprawdzamy czy która z tych stron była najdawniej
                # używana, przypisujemy najdawniej używaną stronę tymaczasowej
                # zmiennej usuwamy z naszego setu najdawniej
                # używaną strone i dodajemy tą oczekującą,
                # obliczamy czas spedzony w kolejce, na końcu inkrementujemy page faults
                if int(queue_of_pages_and_their_times[index_for_queue]) not in set_of_current_pages:
                    lru = float("inf")
                    for page in set_of_current_pages:
                        if indexes[int(page)] < lru:
                            lru = indexes[int(page)]
                            temp = page

                    set_of_current_pages.remove(temp)
                    set_of_current_pages.add(queue_of_pages_and_their_times[index_for_queue])
                    page_faults += 1

                make_page_and_arrival_time_list(queue_of_pages_and_their_times, index_for_queue)

                # Do indexów z których będziemy korzystać przy usuwaniu
                # jako klucz w słowniku wpisujemy stronę a jako wartość
                # dla tego klucza przypisujemy index_for_queue jest to tak jakby czas iteracji
                # im mniejszy indeks tym dawniej temu była ta strona wykorzystana
                # na końcu iterujemy index_for_queue
                indexes[queue_of_pages_and_their_times[index_for_queue]] = index_for_queue
                index_for_queue += 2
            except IndexError:
                pass
        # Zwiększamy nasz licznik czasu
        time_counter += 1

    return page_faults
