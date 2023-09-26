def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # freq_counter = {}

    # for num in nums:
    #     num_freq = freq_counter.get(num,0)
    #     freq_counter[num] = num_freq + 1

    # # find max val, return that number

    # return freq_counter[key] for (key,value) in freq_counter


    freq = [nums.count(amount) for amount in nums ]
    index = freq.index(max(freq))

    return nums[index]

    # dictionary freq counter
    # use .get() with default value