from threading import Lock, Semaphore, Event
from error.InvalidInsertIndexError import InvalidInsertIndexError

class TaskQueue:
    def __init__(self, capcity = 10):
        self.capcity = capcity
        self.buffer = [None] * self.capcity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.queueLock = Lock()
        self.emptySlot = Semaphore(self.capcity)
        self.filledSlot = Semaphore(0)
        self.emptyEvent = Event()
        self.emptyEvent.set()
        self.nonEmptyEvent = Event()

    def __len__(self):
        with self.queueLock:
            length = self.size
        return length

    def get(self):
        self.filledSlot.acquire(blocking = True)
        with self.queueLock:
            task = self.buffer[self.head]
            self.head = (self.head+1) % self.capcity
            if self.size == 1:
                self.size -= 1
                self.nonEmptyEvent.clear()
                self.emptyEvent.set()
        self.emptySlot.release()
        return task

    def put(self, task, block):
        acquired = self.emptySlot.acquire(blocking = block)
        if not acquired:
            return False
        with self.queueLock:
            self.buffer[self.tail] = task
            self.tail = (self.tail+1) % self.capcity
            if self.size == 0:
                self.size += 1
                self.emptyEvent.clear()
                self.nonEmptyEvent.set()
        self.filledSlot.release()
        return True

    def insert(self, index, task, block):
        acquired = self.emptySlot.acquire(blocking = block)
        if not acquired:
            return False
        with self.queueLock:
            if index > self.size:
                self.emptySlot.release()
                raise InvalidInsertIndexError
            position = (self.head+index) % self.capcity
            self.insertToPosition(position, task)
            if self.size == 0:
                self.size += 1
                self.emptyEvent.clear()
                self.nonEmptyEvent.set()
        self.filledSlot.release()
        return True

    def remove(self, index):
        acquired = self.filledSlot.acquire(blocking = False)
        if not acquired:
            return False
        with self.queueLock:
            if index >= self.size:
                self.filledSlot.release()
                raise InvalidInsertIndexError
            position = (self.head+index) % self.capcity
            self.removeFromPosition(position)
            if self.size == 1:
                self.size -= 1
                self.nonEmptyEvent.clear()
                self.emptyEvent.set()
        self.emptySlot.release()
        return True

    def insertToPosition(self, position, task):
        while position != self.tail:
            temp = self.buffer[position]
            self.buffer[position] = task
            task = temp
            position = (position+1) % self.capcity
        buffer[self.tail] = task
        self.tail = (self.tail+i) % self.capcity

    def removeFromPosition(self, position):
        while position != self.head:
            nextPosition = position-1 if position else self.capcity-1
            self.buffer[position] = self.buffer[nextPosition]
            position = nextPosition
        self.head = (self.head+1) % self.capcity

    def toList(self):
        result = []
        with self.queueLock:
            index = self.head
            while index != self.tail:
                result.append(self.buffer[index])
                index = (index+1) % self.capcity
        return result
