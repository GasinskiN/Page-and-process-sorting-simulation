# import all the files
import SJF
from generator import *
import FCFS
import lru
import FiFo
import save_to_word_processes
# set a table with all the generator settings, average time spent in queue, page faults and page hits
table_with_miscellaneous = [["normal distribution time of arrival", mean_arriving_time],
                            ['standard deviation time of arrival', std_arriving_time],
                            ["normal distribution duration", mean_execution_time],
                            ["standard deviation duration", std_execution_time],
                            ['number of processes', number_of_items], ["average time in queue FCFS", 0],
                            ["Average time in queue LRU", 0], ["page faults FIFO", 0], ["page faults LRU", 0],
                            ["page hits FIFO", 0], ["page hits LRU", 0]]

file_name = f"Arrival_mean_{mean_arriving_time}_std_{std_arriving_time}_Processing time mean" \
               f"_{mean_execution_time}_std_{std_execution_time}_processes_{number_of_items}"

# run the process simulations
average_fcfs, table_fcfs = FCFS.fcfs_main(data_array_processes, number_of_items)
average_sjf, table_sjf = SJF.sjf_main(data_array_processes, number_of_items)

# input data into table with miscellaneous
table_with_miscellaneous[5][1] = average_fcfs
table_with_miscellaneous[6][1] = average_sjf

# run the page simulations
page_faults_lru = lru.lru_main(data_array_pages, number_of_items)
page_faults_fifo = FiFo.fifo_main(data_array_pages, number_of_items)

# insert page faults into table with miscellaneous
table_with_miscellaneous[7][1] = page_faults_fifo
table_with_miscellaneous[8][1] = page_faults_lru

# calculate page faults
page_hits_fifo = number_of_items - page_faults_fifo
page_hits_lru = number_of_items - page_faults_lru

# input page faults into table with miscellaneous
table_with_miscellaneous[9][1] = page_hits_fifo
table_with_miscellaneous[10][1] = page_hits_lru

# Save all the data to excel
save_to_word_processes.save_to_excel(data_array_processes, table_fcfs,
                                     table_sjf, file_name, table_with_miscellaneous)

print(page_faults_lru, page_faults_fifo)
