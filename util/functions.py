def linearSearch(array, target):
    for index, value in enumerate(array):
        if value >= target:
            return index
    return len(array)
