import SJF
from generator import *
import FCFS
import lru
import FiFo
import save_to_word_processes

table_with_miscellaneous = [["średnia czas przybycia", mean_arriving_time], ['odchylenie czas przybycia', std_arriving_time],
                            ["średnia czas trwania", mean_execution_time], ["odchylenie czas trwania", std_execution_time],
                            ['Ilosc procesow', number_of_items], ["średni czas w kolejce fcfs", 0],
                            ["średni czas w kolejce lru", 0], ["page faults fifo", 0], ["page faults lru", 0],
                            ["page hits fifo", 0], ["page hits lru", 0]]

table_with_settings_pages = [["średnia czas przybycia", mean_arriving_time], ['odchylenie czas przybycia', std_arriving_time],
                             ['Ilosc procesow', number_of_items], ["Page faults fifo", 0], ["Page faults lru", 0]]

file_name = f"Arrival_mean_{mean_arriving_time}_std_{std_arriving_time}_Processing time mean" \
               f"_{mean_execution_time}_std_{std_execution_time}_processes_{number_of_items}"

my_data_processes = data_array_processes
my_data_pages = data_array_pages

average_fcfs, table_fcfs = FCFS.fcfs_main(my_data_processes, number_of_items)
average_sjf, table_sjf = SJF.sjf_main(my_data_processes, number_of_items)

table_with_miscellaneous[5][1] = average_fcfs
table_with_miscellaneous[6][1] = average_sjf

page_faults_lru = lru.lru_main(my_data_pages, number_of_items)
page_faults_fifo = FiFo.fifo_main(my_data_pages, number_of_items)

table_with_miscellaneous[7][1] = page_faults_fifo
table_with_miscellaneous[8][1] = page_faults_lru

page_hits_fifo = number_of_items - page_faults_fifo
page_hits_lru = number_of_items - page_faults_lru

table_with_miscellaneous[9][1] = page_hits_fifo
table_with_miscellaneous[10][1] = page_hits_lru


save_to_word_processes.save_to_excel(my_data_processes, table_fcfs,
                                     table_sjf, file_name, table_with_miscellaneous)
print(page_faults_lru, page_faults_fifo)
