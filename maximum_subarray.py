#The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers


def max_sequence(arr):

    local_max = 0
    n = len(arr)
    global_max = 0

    for i in range(n):
        local_max = max(arr[i], (arr[i] + local_max))
        if local_max > global_max:
            global_max = local_max
    
    return global_max


print(max_sequence( [-2, 1, -3, 4, -1, 2, 1, -5, 4] ))
