import threading
import time


class MyThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print(f'Starting {self.name} \n')
        # only this thread can be active, rest is locked
        threadLock.acquire()
        print_time(self.name, 1, self.count)
        threadLock.release()
        print(f'Exiting {self.name} \n')


class MyThread2(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print(f'Starting {self.name} \n')
        # threads of this class can work at the same time
        threadLock.acquire()
        threadLock.release()
        print_time(self.name, 1, self.count)
        print(f'Exiting {self.name} \n')


def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1


# run thread2 after thread1 finishes its work
threadLock = threading.Lock()

# after thread1 finishes the rest cant work at the same time
thread1 = MyThread(1, "Payment", 5)
thread2 = MyThread2(2, "Sending email", 10)
thread3 = MyThread2(3, "Loading page", 3)

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("Done main thread")
