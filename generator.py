from numpy import random, stack, arange

# średnie, odchylenia standardowe oraz ilość procesów bądź stron
mean_execution_time = 10
std_execution_time = 10
mean_arriving_time = 10
std_arriving_time = 10
number_of_items = 10

# procesy w kolejności od 1 do ilości procesów
processes = arange(1, number_of_items + 1)
# rozkład gamma dla stron
pages = []
while len(pages) < number_of_items:
    temp = round(random.gamma(4, 1))
    if 0 <= temp <= 9:
        pages.append(temp)
pages = random.randint(10, size=number_of_items)
# Rozkład normalny czasu przybycia oraz trwania (nie jest to prawdziwy rozkład normalny
# ponieważ liczby ujemne konwertuję na dodatnie
# a do czasu wykonania dodaję potem jeszcze jeden aby każdy z procesów miał czas wykonania większy niż 0)
arriving_time = abs(random.normal(loc=mean_arriving_time, scale=std_arriving_time, size=number_of_items))
execution_time = abs(random.normal(loc=mean_execution_time, scale=std_execution_time, size=number_of_items))
arriving_time = arriving_time.round()
execution_time = execution_time.round()
# Wszystkie te dane dajemy do jednej listy aby łatwno można było z nich skorzystać
data_array_processes = stack((processes, arriving_time, execution_time), axis=1)
data_array_pages = stack((pages, arriving_time), axis=1)
