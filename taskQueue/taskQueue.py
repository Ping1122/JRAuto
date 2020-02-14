from threading import Lock, Semaphore
from error.InvalidInsertIndexError import InvalidInsertIndexError

class TaskQueue:
    def __init__(self, capcity = 10):
        self.capcity = capcity
        self.buffer = [None] * self.capcity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.queueLock = Lock()
        self.empty = Semaphore(self.capcity)
        self.full = Semaphore(0)

    def __len__(self):
        with self.queueLock:
            length = self.size
        return length

    def get(self):
        self.full.acquire(blocking = True)
        with self.queueLock:
            task = self.buffer[self.head]
            self.head = (self.head+1) % self.capcity
            self.size -= 1
        self.empty.release()
        return task

    def put(self, task):
        acquired = self.empty.acquire(blocking = False)
        if not acquired:
            return False
        with self.queueLock:
            self.buffer[self.tail] = task
            self.tail = (self.tail+1) % self.capcity
            self.size += 1
        self.full.release()
        return True

    def insert(self, index, task):
        acquired = self.empty.acquire(blocking = False)
        if not acquired:
            return False
        with self.queueLock:
            position = self.calculatePosition(index)
            self.insertToPosition(position, task)
        self.full.release()
        return True

    def remove(self, index):
        acquired = self.full.acquire(blocking = False)
        if not acquired:
            return False
        with self.queueLock:
            position = self.calculatePosition(index)
            self.removeFromPosition(position)
        self.empty.release()
        return True

    def calculatePosition(self, index):
        if index >= self.size:
            raise InvalidInsertIndexError
        return (self.head+index) % self.capcity

    def insertToPosition(self, position, task):
        while position != self.tail:
            temp = self.buffer[position]
            self.buffer[position] = task
            task = temp
            position = (position+1) % self.capcity
        buffer[self.tail] = task
        self.tail = (self.tail+i) % self.capcity
        self.size += 1

    def removeFromPosition(self, position):
        while position != self.head:
            nextPosition = position-1 if position else self.capcity-1
            self.buffer[position] = self.buffer[nextPosition]
            position = nextPosition
        self.head = (self.head+1) % self.capcity
        self.size -= 1

    def toList(self):
        result = []
        with self.queueLock:
            index = self.head
            while index != self.tail:
                result.append(self.buffer[index])
                index = (index+1) % self.capcity
        return result
