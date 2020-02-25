from threading import Lock
from sys import stdin

def linearSearch(array, target):
    for index, value in enumerate(array):
        if value >= target:
            return index
    return len(array)

lock = Lock()
def synchronizedInput(prompt):
    with lock:
    	print(prompt)
        return stdin.readline()