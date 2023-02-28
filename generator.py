from numpy import random, stack, arange

# mean, standard deviation and number of pages and processes
mean_execution_time = 10
std_execution_time = 10
mean_arriving_time = 10
std_arriving_time = 10
number_of_items = 10

# array of processes from 1 to the number of items
processes = arange(1, number_of_items + 1)
# gamma distribution for generating pages
pages = []
while len(pages) < number_of_items:
    temp = round(random.gamma(4, 1))
    if 0 <= temp <= 9:
        pages.append(temp)
pages = random.randint(10, size=number_of_items)
# normal distribution of time of arrival and duration (not a real normal distribution,
# negative numbers are converted to positive, and there is a 1 added to the duration of
# processes so we always have a duration)
arriving_time = abs(random.normal(loc=mean_arriving_time, scale=std_arriving_time, size=number_of_items))
execution_time = abs(random.normal(loc=mean_execution_time, scale=std_execution_time, size=number_of_items))
arriving_time = arriving_time.round()
execution_time = execution_time.round()
# All the data is stored in one array
data_array_processes = stack((processes, arriving_time, execution_time), axis=1)
data_array_pages = stack((pages, arriving_time), axis=1)
