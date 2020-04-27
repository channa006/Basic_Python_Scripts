# Multiprocessing and Multi Threading
#  Running Synchronously , one by one
# Spilt the tast up to other CPUs and run them at same time
# I/O Bound or CPU Bound
# I/O Bound - Things are waiting for input/output operations to be completed, they not using the CPU.
# CPU Bound - Crunching alot a number using the CPU
# Exampls Files system , Network Operaions Threading

# We wouldn't get much of speed using the threading on CPU bound tasks. because those threads are still running single CPU


import concurrent.futures
import time
import multiprocessing


start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')


# Without Multi Processing

# start = time.perf_counter()


# def do_something():
#     print('Sleeping  1 Second')
#     time.sleep(1)
#     print('Done Sleeping')


# do_something()

# finish = time.perf_counter()
# print(f'Finished in {round(finish-start,2)} second(s)')

# With Multi Processing


# start = time.perf_counter()


# def do_something():
#     print('Sleeping  1 Second')
#     time.sleep(1)
#     print('Done Sleeping')


# p1 = multiprocessing.Process(target=do_something())
# p2 = multiprocessing.Process(target=do_something())

# p1.start()
# p2.start()

# p1.join()
# p2.join()


# finish = time.perf_counter()

# print(f'Finished in {round(finish-start,2)} second(s)')
