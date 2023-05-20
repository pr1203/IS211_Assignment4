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


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


def main():
    random.seed(100)
    list_size = [500, 1000, 5000]
    total_time = 0

    for lists in list_size:
        for i in range(100):
            sorted_list = sorted(get_me_random_list(lists))
            start_time = time.time()
            sequential_search(sorted_list, 99999999)
            end_time = time.time()
            search_time = end_time - start_time
            total_time += search_time
        avg_time = total_time / 100
        print(f'Sequential Search of {lists} took {avg_time:10.7f} seconds to run, on average.')

    for lists in list_size:
        for i in range(100):
            sorted_list = sorted(get_me_random_list(lists))
            start_time = time.time()
            ordered_sequential_search(sorted_list, 99999999)
            end_time = time.time()
            search_time = end_time - start_time
            total_time += search_time
        avg_time = total_time / 100
        print(f'Ordered Sequential Search of {lists} took {avg_time:10.7f} seconds to run, on average.')

    for lists in list_size:
        for i in range(100):
            sorted_list = sorted(get_me_random_list(lists))
            start_time = time.time()
            binary_search_iterative(sorted_list, 99999999)
            end_time = time.time()
            search_time = end_time - start_time
            total_time += search_time
        avg_time = total_time / 100
        print(f'Binary Search Iterative of {lists} took {avg_time:10.7f} seconds to run, on average.')

    for lists in list_size:
        for i in range(100):
            sorted_list = sorted(get_me_random_list(lists))
            start_time = time.time()
            binary_search_recursive(sorted_list, 99999999)
            end_time = time.time()
            search_time = end_time - start_time
            total_time += search_time
        avg_time = total_time / 100
        print(f'Binary Search Recursive of {lists} took {avg_time:10.7f} seconds to run, on average.')


if __name__ == "__main__":
    """Main entry point"""
    parse = argparse.ArgumentParser()
    args = parse.parse_args()
    main()
