import random
import time

def selection_sort(list):

    count = 0
    length = len(list)
    for i in range(0, length):
        #count += 1
        min = i
        for j in range(i+1, length):
            count += 1
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
    return count



def insertion_sort(list):
    count = 0
    for x in range(1, len(list)):
        temp = list[x]
        y = x - 1

        while y >= 0 and temp < list[y]:
            list[y + 1] = list[y]
            y -= 1
            count += 1
        list[y + 1] = temp
        #count += 1
    return count



def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234)
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 32000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

