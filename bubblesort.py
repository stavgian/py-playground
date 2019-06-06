import time


def bubble_sort(lst):
    num_swaps = 0

    if len(lst) < 2:
        return num_swaps

    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                num_swaps += 1

    return num_swaps


a = list(range(10, 0, -1))


start = time.time()
swaps = bubble_sort(a)
end = time.time()


print('Array is sorted in {0} swaps.'.format(swaps))
print('First Element: {0}'.format(a[0]))
print('Last Element: {0}'.format(a[-1]))
print('time passed:',end - start)
