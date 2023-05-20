import argparse
import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    for index in range(1, len(a_list)):

        currentvalue = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > currentvalue:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = currentvalue


def shell_sort(a_list):
    sublistcount = len(a_list) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gap_insertion_sort(a_list, startposition, sublistcount)

        #print("After increments of size", sublistcount, "The list is", a_list)

        sublistcount = sublistcount // 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):

        currentvalue = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > currentvalue:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = currentvalue


def python_sort(a_list):
    return sorted(a_list)


def main():
    random.seed(100)
    list_size = [500, 1000, 5000]
    total_time = 0

    for lists in list_size:
        for i in range(100):
            my_list = get_me_random_list(lists)
            start_time = time.time()
            insertion_sort(my_list)
            end_time = time.time()
            sort_time = end_time - start_time
            total_time += sort_time
        avg_time = total_time / 100
        print(f'Insertion Sort of {lists} took {avg_time:10.7f} seconds to run, on average.')

    for lists in list_size:
        for i in range(100):
            my_list = get_me_random_list(lists)
            start_time = time.time()
            shell_sort(my_list)
            end_time = time.time()
            sort_time = end_time - start_time
            total_time += sort_time
        avg_time = total_time / 100
        print(f'Shell Sort of {lists} took {avg_time:10.7f} seconds to run, on average.')

    for lists in list_size:
        for i in range(100):
            my_list = get_me_random_list(lists)
            start_time = time.time()
            python_sort(my_list)
            end_time = time.time()
            sort_time = end_time - start_time
            total_time += sort_time
        avg_time = total_time / 100
        print(f'Python Sort of  {lists} took {avg_time:10.7f} seconds to run, on average.')


if __name__ == "__main__":
    """Main entry point"""
    parse = argparse.ArgumentParser()
    args = parse.parse_args()
    main()
