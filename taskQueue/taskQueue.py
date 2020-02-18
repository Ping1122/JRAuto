from threading import Lock, Semaphore, Event
from error.invalidInsertIndexError import InvalidInsertIndexError
from error.invalidTaskReferenceError import InvalidTaskReferenceError

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
        self.nextTaskId = 1

    def __len__(self):
        return self.size

    def __str__(self):
        result = []
        index = self.head
        while index != self.tail:
            result.append(f"{str(self.buffer[index])} | ")
            index = (index+1) % self.capcity
        return "".join(result)

    def getHead(self):
        with self.queueLock:
            if self.size == 0:
                return None
            print(self)
            return self.buffer[self.head]

    def put(self, task, block):
        acquired = self.emptySlot.acquire(blocking = block)
        if not acquired:
            return False
        with self.queueLock:
            self.buffer[self.tail] = task
            self.tail = (self.tail+1) % self.capcity
            self.size += 1
            task.id = self.nextTaskId
            self.nextTaskId += 1
            if self.size == 1:
                task.isHead = True
                self.emptyEvent.clear()
                self.nonEmptyEvent.set()
        self.filledSlot.release()
        print(self)
        return task.id

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
            self.size += 1
            task.id = self.nextTaskId
            self.nextTaskId += 1
            if index == 0:
                task.isHead = True
            if self.size == 1:
                self.emptyEvent.clear()
                self.nonEmptyEvent.set()
            else:
                self.buffer[1].isHead = False
        self.filledSlot.release()
        print(self)
        return task.id

    def removeById(self, taskId):
        self.filledSlot.acquire(blocking = True)
        with self.queueLock:
            position = self.head;
            while position != self.tail:
                if self.buffer[position].id == taskId:
                    break
                position = (index+1) % self.capcity
            if index == self.head:
                self.filledSlot.release()
                raise InvalidTaskReferenceError
            self.removeFromPosition(position)
            self.size -= 1
            if task.isHead:
                task.isHead = False
            if self.size == 0:
                self.nonEmptyEvent.clear()
                self.emptyEvent.set()
            else:
                self.buffer[0].isHead = True
        self.emptySlot.release()
        print(self)
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
